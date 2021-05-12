import torch.nn as nn
import torch.nn.functional as F
from torchsummary import summary
import torch
import time
import os
from torch.autograd import Variable
from torch.utils.data import DataLoader, Dataset
import numpy
import torchvision.transforms as transforms
from PILDataset import PILDataset
from skimage import data, io
# from EncoderDecoder import SegNet1
from PIL import Image
from openpyxl import load_workbook
import pandas as pd
from utils import *
from torch.utils import model_zoo
from torchvision import models

from utils import Superimpose, PILImageUtility, PILImageSave, Threshold

from PIL import ImageOps as op
from UnetHED import UNetHED  ##New change
import sys


transform = transforms.Compose([
    transforms.ToPILImage()  # ,
    # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

# This the folder path where your data will reside.This folder will have three sub folders. a) original-- this folder will have your input image. b) label -- this folder will have the label image. c) Result -- this will have the output prediction
basepath = "/content/drive/My Drive/Deep Network Visualization"
foldername = "/Test/Result/" # this is a subfolder name where your results will reside.
modelpath  = sys.argv[1] # This is the path where your trained model is located

no_of_test_images = 5           # this is the number of images you want to test. this should be less then the number of images you have
test_subsample_size = 1024       # this is the image subsample size. If your image height and width is less than this reduce the value. 800 is a standard value




valid_image_name = [f for f in os.listdir(basepath + '/valid/original/') if '.JPG' in f] # this gets all the input image  name of that folder
valid_label_image_name = [f for f in os.listdir(basepath + '/valid/label_majorcrack/') if '.bmp' in f] # this gets all the label image  name of that folder

train_image_list = []
label_image_list = []
valid_image_list = []
valid_label_list = []

valid_image_name.sort()
valid_label_image_name.sort()


#segnet  = SegNetHEDKernel7(num_classes=1, filter_config=(4,8,16,32,64)).cuda() # the model is defined here

segnet = UNetHED(1, in_channels=3, depth=5,
                start_filts=8,
                merge_mode='concat').cuda()

segnet.load_state_dict(torch.load(modelpath)) # the trained model is loaded here

loss = 0
Res = []
count = 0
model = segnet


# The following piece of code selects a sample of an input image. Passes it to the model and saves the output and superimposed result
for i in range(0, no_of_test_images):
    valid_image_list = []
    valid_label_list = []
    image = Image.open(basepath + '/valid/original/' + valid_image_name[i])
    valid_image_list.append(image)
    label = Image.open(basepath + '/valid/label_majorcrack/' + valid_label_image_name[i])
    convert = ConvertBinary(label)
    label = convert.convert_binary_pillow()
    valid_label_list.append(label)
    train_set = PILDataset(valid_image_list, valid_label_list, len(valid_label_list), 1, image_size=(test_subsample_size, test_subsample_size))
    dataloaders = {'train': DataLoader(train_set, batch_size=1, shuffle=False, num_workers=0)}

    for i, data in enumerate(dataloaders['train']):
        torch.cuda.empty_cache()
        x = data['image']
        X = Variable(x).cuda()
        y = data['mask']
        Y = y
        Y = Variable(Y).cuda()


        output = model(X) # X is the input image and it is passed to the model.

        pre = output[0].cpu()
        pred = pre.detach()

        x_numpy = numpy.array(transform(x[0]))
        y_numpy = numpy.array(transform(y[0]))


        out_numpy = pred.numpy()

        out_numpy = out_numpy[0]

        threshold = Threshold(out_numpy)

        th_img = threshold.threshold(0.9)
        sp = Superimpose(x_numpy, y_numpy, th_img)

        sp_img, r = sp.superimpose_result_with_threshold()

        io.imsave(basepath+foldername + str(count) + "predicted_truth.png", th_img)  # this is the output of the network
        io.imsave(basepath+foldername + str(count) + "predicted_superimpose_proposed.png", sp_img) # this is the superimposed image with different colors

        print("Image processed")
        print(r)
        Res.append(r)
        count = count + 1
        del X, Y


del segnet, model

# The following piece of code is for  the quantitative results we reported. It will generate an excel file where you can see the statistical results.
Res = numpy.asarray(Res)

TP = sum(Res[:, 0].flatten())
FP = sum(Res[:, 1].flatten())
TN = sum(Res[:, 2].flatten())
FN = sum(Res[:, 3].flatten())
P_GT = sum(Res[:, 4].flatten())
N_GT = sum(Res[:, 5].flatten())

Accuracy = ((TP + TN) / (TP + FP + TN + FN)) * 100
Specificity = ((TN) / (TN + FP)) * 100
Recall = ((TP) / (TP + FN))
Error_rate = ((FP + FN) / (TP + FP + TN + FN))
Precision = (TP) / (TP + FP)
F1 = (2 * (Precision * Recall) / (Precision + Recall))
TPR = (TP/(TP+FN))*100
FPR = (FP/(FP+TN))*100
TNR = (TN/(TN+FP))*100
FNR = (TP/(TP+FN))*100
Result = []



Result.append(
    ["Proposed Network", "True Positive Percentage", "False Positive Percentage", "True Negative Percentage", "False Negative Percentage", "Accuracy","Error rate", "Specificity",
     "Precision", "Recall", "F1"])
Result.append(
    [foldername, TPR, FPR, TNR, FNR, Accuracy, Error_rate*100, Specificity,
     Precision*100, Recall*100, F1*100])


writer = pd.ExcelWriter('test.xlsx', engine='openpyxl')
wb = writer.book
df = pd.DataFrame(Result)

df.to_excel(writer, index=False)
wb.save(basepath + foldername+'Result.xlsx')