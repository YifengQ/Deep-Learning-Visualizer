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

from torch.utils import model_zoo
from torchvision import models
from unet import *
from utils import Superimpose, PILImageUtility, PILImageSave, Threshold
from SegnetSideoutput import  *
from SegnetTry import *
from unet import *
from PIL import ImageOps as op
from SegnetHED import *
from EncoderDecoder import *
#from UnetHED import *
from Visualize import  *
from utils import  *
#basepath = "/media/purba/New Volume/ICMLA/EncoderDecoder-16-32-64-128/EncoderDecoder4-8-16-32-64-128.pth"



def concatenate(basepath, count, size):
    imglist = []
    valid_image_name = [f for f in os.listdir(basepath+"superimpose/") if '.png' in f]
    valid_image_name.sort()

    padarray = numpy.ones(size)
    i = 0
    for j in range(0, int(len(valid_image_name)/count)):
        stiched_image = Image.new("RGB", (count* (size+10), count* size))
        segnet1 =  Image.open(basepath+"superimpose/"+valid_image_name[i+3])
        segnet2 = Image.open(basepath+"superimpose/"+valid_image_name[i+1])
        segnet_side1 = Image.open(basepath+"superimpose/"+valid_image_name[i+0])
        segnet_side2 = Image.open(basepath+"superimpose/"+valid_image_name[i+2])
        unet = Image.open(basepath+"superimpose/"+valid_image_name[i+4])

        unet = op.expand(unet, (0,0, 10, 0), fill="#FFF")
        segnet1 = op.expand(segnet1, (0,0, 10, 0), fill="#FFF")
        segnet2 = op.expand(segnet2, (0, 0, 10, 0), fill="#FFF")
        segnet_side1 = op.expand(segnet_side1, (0, 0, 10, 0), fill="#FFF")
        segnet_side2 = op.expand(segnet_side2, (0, 0, 10, 0), fill="#FFF")

        listofimg = [numpy.array(unet), numpy.array(segnet1), numpy.array(segnet2), numpy.array(segnet_side1), numpy.array(segnet_side2)]

        concat = numpy.concatenate(listofimg, axis=1)



        #unet.show()

        io.imsave(basepath+"concat/"+valid_image_name[i+1][0:4]+"concat.png", concat)
        i = i + count
        print(i)




transform = transforms.Compose([
    transforms.ToPILImage()  # ,
    # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

basepath = "/media/purba/New Volume/ICMLA/Test/"



foldername = "/////SegNet-HED-Sigmoid/Visualization//"

valid_image_name = [f for f in os.listdir(basepath + '//original_generated/') if '.png' in f]
valid_label_image_name = [f for f in os.listdir(basepath + '//label_filtered/') if '.bmp' in f]

train_image_list = []
label_image_list = []
valid_image_list = []
valid_label_list = []

valid_image_name.sort()
valid_label_image_name.sort()

"""
for i in range(0, len(valid_image_name)):
    image = Image.open(basepath + '/train/original/' + valid_image_name[i])
    valid_image_list.append(image)
    label = Image.open(basepath + '/train/label/' + valid_label_image_name[i])
    convert = ConvertBinary(label)
    label = convert.convert_binary_pillow()
    valid_label_list.append(label)
"""


#segnet = UNetHED(1, depth=param.unet_depth,
#                        start_filts=param.unet_start_filters,
#                        merge_mode='concat').cuda()


segnet  = SegNetHED(num_classes=1, filter_config=(8,16,32,64,64)).cuda()
#segnet  = SegNetHEDKernel7(num_classes=1, filter_config=(4,8,16,32,64), kernel_size=7, padding=3).cuda()
segnet.load_state_dict(torch.load("//media/purba/New Volume/ISVC/TestDataSet/Testset/SegnetHED_Soft_dim2_upsample_sigmoid.pth"))


tf = transforms.Compose([
    transforms.ToTensor()  # ,
    # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

loss = 0

Res = []
count = 0
model = segnet

encoders = segnet.encoders
decoders = segnet.decoders
classifier1 = segnet.classifier1
side_output = segnet.sides
for i in range(0, 100):
    valid_image_list = []
    valid_label_list = []
    image = Image.open(basepath + '//original_generated/' + valid_image_name[i])
    valid_image_list.append(image)
    #valid_image_list.append(image.rotate(90))
    label = Image.open(basepath + '//label_filtered/' + valid_label_image_name[i])
    label = convert_binary_pillow(label)
    valid_label_list.append(label)
    #valid_label_list.append(label.rotate(90))
    train_set = PILDataset(valid_image_list, valid_label_list, len(valid_label_list), 1, image_size=(1024, 1024))
    dataloaders = {'train': DataLoader(train_set, batch_size=1, shuffle=False, num_workers=0)}

    rotate = 0;
    for j, data in enumerate(dataloaders['train']):
        torch.cuda.empty_cache()
        x = data['image']
        # x = transform(x)
        X = Variable(x).cuda()  # [N, 1, H, W]
        # model.half()
        # X = X.half()
        y = data['mask']
        # y = transform(y)

        Y = y  # .type(torch.LongTensor)
        # Y = y.type(torch.LongTensor)
        Y = Variable(Y).cuda()
        # Y= Y.half()

        output = model(X)
        inp = X
        enc_indices = []
        Side = []
        Side_out_concat = []
        for k in range(0,5):
            module = encoders[k]
            viz = Visualize(module, inp, basepath+foldername+ valid_label_image_name[i].replace(".bmp", "encoder")+str(k)+".png")
            inp, indices = viz.visualize_encoder()#visualizemodule(model, input=inp, path=basepath+foldername+"image"+str(count)+"encoder"+str(k)+".png")
            Side.append(inp)
            enc_indices.append(indices)

        for k in range(0,5):
            module = side_output[k]
            inp1 = Side[k]
            viz = Visualize(module, inp1, basepath+foldername+ valid_label_image_name[i].replace(".bmp", "sides")+str(k)+".png")
            inp1 = viz.visualize_sides()#visualizemodule(model, input=inp, path=basepath+foldername+"image"+str(count)+"encoder"+str(k)+".png")
            Side_out_concat.append(inp1)

            #print(inp1.shape)

        for k in range(0,5):
            module = decoders[k]
            #inp = decoders[k].forward(inp, enc_indices[4-k])
            #inp = inp[1]
            viz = Visualize(module, inp,  basepath+foldername+ valid_label_image_name[i].replace(".bmp", "decoder")+str(k)+".png")
            out = viz.visualize_decoder(enc_indices[4-k])#visualizemodule(model, input=inp, path=basepath+foldername+"image"+str(count)+"encoder"+str(k)+".png")
            inp = out[1]

        concatenate_side_result = torch.cat([Side_out_concat[0], Side_out_concat[1]], dim = 1)

        output_image = concatenate_side_result[0].cpu().detach().numpy()
        out_im  = output_image[0]
        for k in range(1, output_image.shape[0]):
            out_im = numpy.concatenate((out_im, output_image[k]), axis=1)

        io.imsave(basepath+foldername+ valid_label_image_name[i].replace(".bmp", "concat_output")+".png", out_im)

        #classifier1_out = classifier1.forward(concatenate_side_result)

        #io.imsave(numpy.transpose(classifier1_out[0].cpu().detach(), (2,1,0)),basepath + foldername + valid_label_image_name[i].replace(".bmp", "classifier1_output") + ".png")

        pre = output[0].cpu()
        pred = pre.detach()

        out_numpy = pred.numpy()

        out_numpy = out_numpy[0]  # numpy.transpose(out_numpy, (2,1,0))

        #print(out_numpy)
        #output_image = out_numpy[0]
        #io.imsave(basepath+foldername+"image_no"+str(count)+"rotate_no"+str(rotate)+"output"+".png", out_numpy)

        #transform(pred*100).save( basepath+foldername+"image_no"+str(count)+"rotate_no"+str(rotate)+"output"+".png")

        x_numpy = numpy.array(transform(x[0]))
        y_numpy = numpy.array(transform(y[0]))
   # numpy.transpose(out_numpy, (2,1,0))

        threshold = Threshold(out_numpy)

        th_img = threshold.threshold(0.95, skip=3)

        sp = Superimpose(x_numpy, y_numpy, th_img)

        sp_img, r = sp.superimpose_result_with_threshold()

        #io.imsave(basepath+foldername + "image_no"+ str(count) + "rotate_no"+str(rotate)+ "predicted_truth.bmp", th_img)
        #io.imsave(basepath+foldername +"image_no"+ str(count) + "rotate_no"+str(rotate)+ "predicted_superimpose_proposed1_1500_1000.png", sp_img)
        io.imsave(basepath + foldername + valid_label_image_name[i].replace(".bmp", "predicted_truth.png"),th_img)
        io.imsave(basepath + foldername + valid_label_image_name[i].replace(".bmp", "predicted_superimpose_proposed.png"), sp_img)


        rotate = rotate +11

        del X, Y
    count = count + 1
"""

valid_image_name = [f for f in os.listdir("/media/purba/New Volume/ICMLA/Test/EncoderDecoder-4--8-16-32-64/Visualization") if 'decoder3' in f]


for j in range(len(valid_image_name)):
    image = io.imread("/media/purba/New Volume/ICMLA/Test/EncoderDecoder-4--8-16-32-64/Visualization/"+valid_image_name[j])

    image1 =(image[0:512, 0:512]/4)
    #image2 = image[0:512, 512:512+512]
    #io.imsave("/media/purba/New Volume/ICMLA/Test/EncoderDecoder-4--8-16-32-64/addition/decoder/"+valid_image_name[j],image)
    start = 0
    end = 512

    im =  image1
    count = 0
    #io.imsave("/media/purba/New Volume/ICMLA/Test/EncoderDecoder-4--8-16-32-64/addition/"+valid_image_name[j].replace(".png", "")+"decoder_out_"+str(count)+".png", image[0: end, start: end])
    for i in range (0,3):
        count = count + 1
        start= start + 512
        end = end++512
        im = (im + (image[0: end, start: end]/4.0))

        #io.imsave("/media/purba/New Volume/ICMLA/Test/EncoderDecoder-4--8-16-32-64/addition/"+valid_image_name[j].replace(".png", "")+"decoder_out_"+str(count)+".png", image[0: end, start: end])

    threshold = Threshold(im)

    thr = 5
    th_img = threshold.threshold(thr)

    #io.imsave("/media/purba/New Volume/ICMLA/Test/EncoderDecoder-4--8-16-32-64/addition/"+valid_image_name[j].replace(".png", "final")+str(count)+".png", im)
    io.imsave("/media/purba/New Volume/ICMLA/Test/EncoderDecoder-4--8-16-32-64/addition/"+valid_image_name[j].replace(".png", "thresholded")+str(thr)+"_"+str(count)+".png", th_img)
"""
