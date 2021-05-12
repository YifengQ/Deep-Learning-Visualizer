import torch.nn as nn
import torch.nn.functional as F
from torchsummary import summary
import  torch
import time
import  os
from torch.autograd import Variable
from torch.utils.data import DataLoader, Dataset
import numpy
import torchvision.transforms as transforms
from PILDataset import  PILDataset
from skimage import  data,io
from PIL import Image
from openpyxl import load_workbook
import pandas as pd
from utils import  *
from skimage import data
from SegnetHED import *

# Here we define the loss function
criterion = torch.nn.BCELoss()
transform = transforms.Compose([
    transforms.ToPILImage()  # ,
    # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

# This class sets the parameters for training.
class param:
    img_size = (512, 512)
    bs = 16 # This the number of batches. You can reduce the number of batches by dividing it by 2/
    num_workers = 4
    lr = 0.001
    epochs = 100 # This is the number of epochs. The training will run for this number of time.
    unet_depth = 5
    unet_start_filters = 8
    log_interval = 300


print("test??")


# This function calculates the loss and performs validation and returns the loss value
def get_loss(dl, model, epoch, p):
    loss = 0
    val_batch = 0
    for i, data in enumerate(dl):
        torch.cuda.empty_cache()
        x = data['image']

        X = Variable(x).cuda()  # [N, 1, H, W]
        y = data['mask']

        Y = y  # .type(torch.LongTensor)
        Y = Variable(Y).cuda()

        output = model(X)

        curr_loss = criterion(output, Y).item()

        loss += curr_loss

        val = transform(x[0])
        lab = transform(data['mask'][0])

        pre = output[0].cpu()
        pred = pre.detach()

        out = transform(pred)

        pil = PILImageUtility(val, lab, out)


        pilsave = PILImageSave(val, lab, out)

        final = pilsave.save_images(w=512)


        pred_path_4 = p+"/valid/Result/epoch_merged_" + str(
            epoch + 1) + "_batch_" + str(val_batch) + "predicted_thresholded_numpy_" + str(curr_loss) + ".png"

        final.save(pred_path_4)


    loss = loss / len(dl)
    return loss
basepath = "///media/purba/New Volume/ICMLA/" # This the folder path where your training will happen and you will put your data here.
foldername = "//Japan Data/" # This is the folder where you put your data and save the model

train_image_name = [f for f in os.listdir(basepath + foldername+ '/train/original/') if '.jpg' in f] # It reads the image
label_image_name = [f for f in os.listdir(basepath + foldername+'/train/label/') if '.png' in f] # It reads image label

valid_image_name = [f for f in os.listdir(basepath + foldername+'/valid/original/') if '.jpg' in f]
valid_label_image_name = [f for f in os.listdir(basepath + foldername+'/valid/label/') if '.png' in f]

train_image_list = []
label_image_list = []
valid_image_list = []
valid_label_list = []
train_image_name.sort()
label_image_name.sort()
valid_image_name.sort()
valid_label_image_name.sort()

t_train_start = time.time()
# This for loop takes an image and converts it to binary.
for i in range(0, len(train_image_name)):
    image = Image.open(basepath + foldername+ '/train/original/' + train_image_name[i])  # .convert('RGB')
    train_image_list.append(image)
    label = Image.open(basepath + foldername+ '/train/label/' + label_image_name[i])
    convert = ConvertBinary(label)
    label = convert.convert_binary_pillow()
    label_image_list.append(label)

# This for loop takes an image and converts it to binary.
for i in range(0, len(valid_image_name)):
    image = Image.open(basepath + foldername+'/valid/original/' + valid_image_name[i])
    valid_image_list.append(image)
    label = Image.open(basepath + foldername+'/valid/label/' + valid_label_image_name[i])
    convert = ConvertBinary(label)
    label = convert.convert_binary_pillow()
    valid_label_list.append(label)

# The model is called here. Dont change anything here.
model = SegNetHEDKernel7(num_classes=1, filter_config=(4, 8, 16, 32, 64)).cuda()
testmodel = model

optim = torch.optim.Adam(model.parameters())

iters = []
train_losses = []
val_losses = []

it = 0
min_loss = numpy.inf

#The model is set to training mode here.
model.train()
count = 0
label = None

output = None
val_loss = None
# onehotencoder = OneHotEncoder(categorical_features=[1])
torch.cuda.empty_cache()

for epoch in range(0, param.epochs):
    torch.cuda.empty_cache()

    t_start = time.time()
    # The following two lines generate 10,000 data for training each time and 1000 for validation
    train_set = PILDataset(train_image_list, label_image_list, len(train_image_list), 10000, image_size=param.img_size)
    valid_set = PILDataset(valid_image_list, valid_label_list, len(valid_image_list), 1000, image_size=param.img_size)

    dataloaders = {'train': DataLoader(train_set, batch_size=param.bs, shuffle=False, num_workers=0),
                   'validate': DataLoader(valid_set, batch_size=param.bs, shuffle=False, num_workers=0)}

    count = 0
    for i, data in enumerate(dataloaders['train']):
        torch.cuda.empty_cache()
        x = data['image']

        X = Variable(x).cuda()  # [N, 1, H, W]

        y = data['mask']

        Y = y  # .type(torch.LongTensor)
        # Y = y.type(torch.LongTensor)
        Y = Variable(Y).cuda()
        # Y= Y.half()

        output = model(X)

        loss = criterion(output, Y)

        # model.float()
        optim.zero_grad()
        loss.backward()
        # model.float()
        optim.step()


        #This piece of code saves the training result
        if (epoch + 1) % 30 == 0:
            val = transform(x[0])
            lab = transform(data['mask'][0])

            pre = output[0].cpu()
            pred = pre.detach()

            out = transform(pred)

            pil = PILImageUtility(val, lab, out)

            pilsave = PILImageSave(val, lab, out)

            final = pilsave.save_images(w=512)

            pred_path_4 = basepath + foldername + "/train/Result/epoch_merged_" + str(
                epoch + 1) + "_batch_" + str(count) + "predicted_thresholded_numpy_" + str(loss.item()) + ".png"

            # final.save(pred_path_4)

        # This piece of code performes validation and calculates loss and saves the model.
        if (count + 1) % param.log_interval == 0:
            # print("got it")
            it += param.log_interval * param.bs
            iters.append(it)
            train_losses.append(loss.item())

            model.eval()
            val_loss = get_loss(dataloaders['validate'], model, epoch, basepath + foldername)
            # print(val_loss)
            model.train()
            val_losses.append(val_loss)

            if val_loss <= min_loss:
                min_loss = val_loss

                print(val_loss)
                torch.save(model.state_dict(),
                           basepath + foldername + "/SegnetHEDkernel7_sigmoid4-8-16-32-fourlayer.pth")
        # """

        count = count + 1

        # del X, Y, loss
    delta = time.time() - t_start

    print("Epoch #[{}/{}]\t\t Time: {:.2f}s current loss: {:.4f}s".format(epoch + 1, param.epochs, delta, min_loss))

writer = pd.ExcelWriter('test.xlsx', engine='openpyxl')
wb = writer.book
df = pd.DataFrame({'Train_loss': train_losses,
                   'Val_loss': val_losses})

df.to_excel(writer, index=False)
wb.save(basepath + foldername + '/SegnetHEDkernel7_sigmoid4-8-16-32-fourlayer.xlsx')

