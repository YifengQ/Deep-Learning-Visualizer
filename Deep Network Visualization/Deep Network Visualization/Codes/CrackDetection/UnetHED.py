import os
import random
import shutil

from multiprocessing.dummy import Pool

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from PIL import Image

from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

from skimage.morphology import binary_opening, disk, label
from skimage import data
from torchsummary import summary

import torch
import torch.nn as nn
import torch.nn.functional as F
import time
from torch.autograd import Variable
from torch.utils.data import DataLoader, Dataset
import numpy
import torchvision.transforms as transforms
from PILDataset import  PILDataset
from skimage import data, io
from PIL import Image
import  skimage.morphology

from skimage.morphology import disk
from skimage.filters import median
from PIL import ImageDraw
from skimage.morphology import square
#from segnet import SegNet
from sklearn.preprocessing import OneHotEncoder
import mpu.ml
from openpyxl import load_workbook
import pandas as pd

from utils import Superimpose, PILImageUtility, PILImageSave, Threshold
def conv1x1(in_channels, out_channels, groups=1):
    return nn.Conv2d(in_channels,
                     out_channels,
                     kernel_size=1,
                     groups=groups,
                     stride=1)

def conv3x3(in_channels, out_channels, stride=1, padding=1, bias=True, groups=1):
    return nn.Conv2d(in_channels,
                     out_channels,
                     kernel_size=3,
                     stride=stride,
                     padding=padding,
                     bias=bias,
                     groups=groups)

def upconv2x2(in_channels, out_channels, mode='transpose'):
    if mode == 'transpose':
        return nn.ConvTranspose2d(in_channels,
                                  out_channels,
                                  kernel_size=2,
                                  stride=2)
    else:
        return nn.Sequential(
            nn.Upsample(mode='bilinear', scale_factor=2),
            conv1x1(in_channels, out_channels))
def side_output( filter, kernel, factor):

   return nn.Sequential(
    #nn.Conv2d(filter,filter, kernel_size=kernel, stride=1, padding=3),
    nn.UpsamplingBilinear2d(scale_factor=factor))
    #nn.UpsamplingBilinear2d(scale_factor=factor))
    #nn.ConvTranspose2d(filter, filter, kernel_size=factor, stride=factor, padding=0))

class Sideoutput(nn.Module):
    def __init__(self, filter, kernel, factor):

        super(Sideoutput, self).__init__()


        self.features = side_output(filter, kernel, factor)


            #if n_blocks == 3:
                #layers += [nn.Dropout(drop_rate)]


    def forward(self, x):
        output = self.features(x)

        return  output
class DownConv(nn.Module):

    def __init__(self, in_channels, out_channels, pooling=True):
        super(DownConv, self).__init__()

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.pooling = pooling

        self.conv1 = conv3x3(self.in_channels, self.out_channels)
        self.conv2 = conv3x3(self.out_channels, self.out_channels)

        if self.pooling:
            self.pool = nn.MaxPool2d(kernel_size=2, stride=2)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        before_pool = x
        if self.pooling:
            x = self.pool(x)
        return x, before_pool

class UpConv(nn.Module):

    def __init__(self,
                 in_channels,
                 out_channels,
                 merge_mode='concat',
                 up_mode='transpose'):
        super(UpConv, self).__init__()

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.merge_mode = merge_mode
        self.up_mode = up_mode

        self.upconv = upconv2x2(self.in_channels,
                                self.out_channels,
                                mode=self.up_mode)

        if self.merge_mode == 'concat':
            self.conv1 = conv3x3(2*self.out_channels,
                                 self.out_channels)
        else:
            # num of input channels to conv2 is same
            self.conv1 = conv3x3(self.out_channels, self.out_channels)

        self.conv2 = conv3x3(self.out_channels, self.out_channels)

    def forward(self, from_down, from_up):

        from_up = self.upconv(from_up)
        if self.merge_mode == 'concat':
            x = torch.cat((from_up, from_down), 1)
        else:
            x = from_up + from_down
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        return x

class UNetHED(nn.Module):


    def __init__(self, num_classes=1, in_channels=3, depth=5, filter_config=(8, 16, 32, 64, 128),
                 start_filts=64, up_mode='transpose',
                 merge_mode='concat'):

        super(UNetHED, self).__init__()

        if up_mode in ('transpose', 'upsample'):
            self.up_mode = up_mode
        else:
            raise ValueError("\"{}\" is not a valid mode for "
                             "upsampling. Only \"transpose\" and "
                             "\"upsample\" are allowed.".format(up_mode))

        if merge_mode in ('concat', 'add'):
            self.merge_mode = merge_mode
        else:
            raise ValueError("\"{}\" is not a valid mode for"
                             "merging up and down paths. "
                             "Only \"concat\" and "
                             "\"add\" are allowed.".format(up_mode))

        # NOTE: up_mode 'upsample' is incompatible with merge_mode 'add'
        if self.up_mode == 'upsample' and self.merge_mode == 'add':
            raise ValueError("up_mode \"upsample\" is incompatible "
                             "with merge_mode \"add\" at the moment "
                             "because it doesn't make sense to use "
                             "nearest neighbour to reduce "
                             "depth channels (by half).")

        self.num_classes = num_classes
        self.in_channels = in_channels
        self.start_filts = start_filts
        self.depth = depth

        self.down_convs = []#nn.ModuleList()
        self.up_convs = []#nn.ModuleList()
        self.sides = nn.ModuleList()

        factor = [2, 4, 8, 16, 16]
        kernel = [4, 8, 16, 32, 32]

        # create the encoder pathway and add to a list
        for i in range(depth):
            ins = self.in_channels if i == 0 else outs
            outs = self.start_filts*(2**i)
            pooling = True if i < depth-1 else False

            down_conv = DownConv(ins, outs, pooling=pooling)
            side =  Sideoutput(filter_config[i], kernel=3,factor=factor[i])
            #print(down_conv)
            #print(side)
            self.down_convs.append(down_conv)
            self.sides.append(side)


        # create the decoder pathway and add to a list
        # - careful! decoding only requires depth-1 blocks
        for i in range(depth-1):
            ins = outs
            outs = ins // 2
            up_conv = UpConv(ins, outs, up_mode=up_mode,
                merge_mode=merge_mode)
            self.up_convs.append(up_conv)

        self.conv_final = conv1x1(outs, self.num_classes)

        final_filter = sum(filter_config)+filter_config[0]
        #print(final_filter)
        self.classifier1 = nn.Sequential(nn.Conv2d(final_filter, num_classes, 1, 1, 0),
                         nn.BatchNorm2d(num_classes),
                         nn.ReLU(inplace=True))

        # add the list of modules to current module
        self.down_convs = nn.ModuleList(self.down_convs)
        self.up_convs = nn.ModuleList(self.up_convs)
        #self.side_out = nn.ModuleList(self.sides)

        self.reset_params()

    @staticmethod
    def weight_init(m):
        if isinstance(m, nn.Conv2d):
            nn.init.xavier_normal(m.weight)
            nn.init.constant(m.bias, 0)


    def reset_params(self):
        for i, m in enumerate(self.modules()):
            self.weight_init(m)

    def forward(self, x):
        encoder_outs = []
        side= []
        # encoder pathway, save outputs for merging
        s = None
        for i , module in enumerate(self.down_convs):#in range(0,len(self.down_convs)):
            x, before_pool = self.down_convs[i](x)
            if i == 0:
                s = torch.nn.Sigmoid()(self.sides[i](x))
            else:
                s = torch.cat([torch.nn.Sigmoid()(self.sides[i](x)),s],dim=1)
            #side.append(s)
            #print(before_pool)
            #print(s.shape)
            #side_outs.append(side)

            encoder_outs.append(before_pool)

        #print(len(encoder_outs))
        #print(s.size())
        for i , module in enumerate(self.up_convs):#in range(0, len(self.up_convs)):
            before_pool = encoder_outs[-(i+2)]
            x = self.up_convs[i](before_pool, x)


        #x = self.conv_final(x)

        xx = torch.cat([s,x], dim=1)
        #print(xx.size())
        #print(xx.size())
        #del encoder_outs, before_pool
        #xx = self.classifier1(torch.cat([side[0], side[1], side[2], side[3], side[4], x], dim=1))

        #xx  = torch.cat([x,xx], dim=1)
        #print(xx.size())
        #x = x.view(x.shape[0], x.shape[1],x.shape[2]*x.shape[3])#feat.size[0], feat.size[1], feat.size[2]*feat.size[3])
        return F.softmax(self.classifier1(xx), dim=2)

class UNet(nn.Module):


    def __init__(self, num_classes=2, in_channels=3, depth=5,
                 start_filts=64, up_mode='transpose',
                 merge_mode='concat'):

        super(UNet, self).__init__()

        if up_mode in ('transpose', 'upsample'):
            self.up_mode = up_mode
        else:
            raise ValueError("\"{}\" is not a valid mode for "
                             "upsampling. Only \"transpose\" and "
                             "\"upsample\" are allowed.".format(up_mode))

        if merge_mode in ('concat', 'add'):
            self.merge_mode = merge_mode
        else:
            raise ValueError("\"{}\" is not a valid mode for"
                             "merging up and down paths. "
                             "Only \"concat\" and "
                             "\"add\" are allowed.".format(up_mode))

        # NOTE: up_mode 'upsample' is incompatible with merge_mode 'add'
        if self.up_mode == 'upsample' and self.merge_mode == 'add':
            raise ValueError("up_mode \"upsample\" is incompatible "
                             "with merge_mode \"add\" at the moment "
                             "because it doesn't make sense to use "
                             "nearest neighbour to reduce "
                             "depth channels (by half).")

        self.num_classes = num_classes
        self.in_channels = in_channels
        self.start_filts = start_filts
        self.depth = depth

        self.down_convs = []
        self.up_convs = []

        # create the encoder pathway and add to a list
        for i in range(depth):
            ins = self.in_channels if i == 0 else outs
            outs = self.start_filts*(2**i)
            pooling = True if i < depth-1 else False

            down_conv = DownConv(ins, outs, pooling=pooling)
            self.down_convs.append(down_conv)

        # create the decoder pathway and add to a list
        # - careful! decoding only requires depth-1 blocks
        for i in range(depth-1):
            ins = outs
            outs = ins // 2
            up_conv = UpConv(ins, outs, up_mode=up_mode,
                merge_mode=merge_mode)
            self.up_convs.append(up_conv)

        self.conv_final = conv1x1(outs, self.num_classes)

        # add the list of modules to current module
        self.down_convs = nn.ModuleList(self.down_convs)
        self.up_convs = nn.ModuleList(self.up_convs)

        self.reset_params()

    @staticmethod
    def weight_init(m):
        if isinstance(m, nn.Conv2d):
            nn.init.xavier_normal(m.weight)
            nn.init.constant(m.bias, 0)


    def reset_params(self):
        for i, m in enumerate(self.modules()):
            self.weight_init(m)

    def forward(self, x):
        encoder_outs = []

        # encoder pathway, save outputs for merging
        for i, module in enumerate(self.down_convs):
            x, before_pool = module(x)
            encoder_outs.append(before_pool)

        for i, module in enumerate(self.up_convs):
            before_pool = encoder_outs[-(i+2)]
            x = module(before_pool, x)


        x = self.conv_final(x)

        #x = x.view(x.shape[0], x.shape[1],x.shape[2]*x.shape[3])#feat.size[0], feat.size[1], feat.size[2]*feat.size[3])
        return F.softmax(x, dim=2)

class param:
    img_size = (512, 512)
    bs = 4
    num_workers = 4
    lr = 0.001
    epochs = 60
    unet_depth = 5
    unet_start_filters = 8
    log_interval = 350


criterion = torch.nn.BCELoss()
transform = transforms.Compose([
    transforms.ToPILImage()  # ,
    # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

def get_loss(dl, model, epoch, basepath):
    loss = 0
    val_batch = 0
    for i, data in enumerate(dl):
        torch.cuda.empty_cache()
        x = data['image']
        # x = transform(x)
        X = Variable(x).cuda()  # [N, 1, H, W]
        y = data['mask']
        # y = transform(y)

        Y = y  # .type(torch.LongTensor)
        Y = Variable(Y).cuda()

        output = model(X)

        curr_loss = criterion(output, Y).item()
        # print(torch.argmax(output[0], dim=0))
        loss += curr_loss

        val = transform(x[0])
        lab = transform(data['mask'][0])

        pre = output[0].cpu()
        pred = pre.detach()
        # print(pred)
        # print(pred)
        out = transform(pred)

        pil = PILImageUtility(val, lab, out)

        # print(out)
        # label = pil.convert_2dto3d_pillow()
        # label = pil.convert_threshold_pillow(0.8)

        pilsave = PILImageSave(val, lab, out)

        final = pilsave.save_images(w=512)

        # pred_path_3 = "/media/purba/New Volume/CNN/label/SegNet-PIL/train/Result/epoch_" + str(
        #    epoch + 1) + "_batch_" + str(count) + "predicted_thresholded_numpy_" + str(loss.item()) + ".png"

        # label.save(pred_path_3)

        pred_path_4 = basepath+"/valid/Result/epoch_merged_" + str(
            epoch + 1) + "_batch_" + str(val_batch) + "predicted_thresholded_numpy_" + str(curr_loss) + ".png"

        final.save(pred_path_4)

        val_batch = val_batch + 1
        del X, Y

    loss = loss / len(dl)
    return loss


def convert_binary(image):
    label = numpy.zeros([image.shape[0], image.shape[1]], dtype='uint8')

    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            R = image[i][j][0]
            G = image[i][j][1]
            B = image[i][j][2]

            if R == 255 and G == 255 and B == 255:
                label[i][j] = 1
    return label


def convert_binary_pillow(image):
    pixels = image.load()  # create the pixel map
    Label = Image.new(mode='1', size=image.size)
    labelpixel = Label.load()

    for i in range(image.size[0]):  # for every pixel:
        for j in range(image.size[1]):
            if pixels[i, j] == (255, 255, 255):
                labelpixel[i, j] = 1
    return Label




def train():
    from skimage import data
    basepath = "/media/purba/New Volume/ICMLA/Unet-HED/"

    basepath1 = "/media/purba/New Volume/ICMLA/"
    train_image_name = [f for f in os.listdir(basepath1 + '/train/original/') if '.JPG' in f]
    label_image_name = [f for f in os.listdir(basepath1 + '/train/label/') if '.bmp' in f]

    valid_image_name = [f for f in os.listdir(basepath1 + '/valid/original/') if '.JPG' in f]
    valid_label_image_name = [f for f in os.listdir(basepath1 + '/valid/label/') if '.bmp' in f]

    train_image_list = []
    label_image_list = []
    valid_image_list = []
    valid_label_list = []
    train_image_name.sort()
    label_image_name.sort()
    valid_image_name.sort()
    valid_label_image_name.sort()

    t_train_start = time.time()
    for i in range(0, len(train_image_name)):
        image = Image.open(basepath1 + '/train/original/' + train_image_name[i])  # .convert('RGB')
        train_image_list.append(image)
        label = Image.open(basepath1 + '/train/label/' + label_image_name[i])
        label = convert_binary_pillow(label)
        label_image_list.append(label)

    for i in range(0, len(valid_image_name)):
        image = Image.open(basepath1 + '/valid/original/' + valid_image_name[i])
        valid_image_list.append(image)
        label = Image.open(basepath1 + '/valid/label/' + valid_label_image_name[i])
        label = convert_binary_pillow(label)
        valid_label_list.append(label)

    # """
    model = UNetHED(1, depth=param.unet_depth,
                        start_filts=param.unet_start_filters,
                        merge_mode='concat').cuda()
    #testmodel = model

    optim = torch.optim.Adam(model.parameters())

    #summary(model,(3, 256, 256))

    iters = []
    train_losses = []
    val_losses = []

    it = 0
    min_loss = numpy.inf

    # os.makedirs(os.path.dirname(bst_model_fpath), exist_ok=True)

    model.train()
    count = 0
    label = None

    output = None
    val_loss = None
    # onehotencoder = OneHotEncoder(categorical_features=[1])
    torch.cuda.empty_cache()
    for epoch in range(0, 100):
        torch.cuda.empty_cache()

        t_start = time.time()
        train_set = PILDataset(train_image_list, label_image_list, len(train_image_list), 3000, image_size=param.img_size)
        valid_set = PILDataset(valid_image_list, valid_label_list, len(valid_image_list), 1000, image_size=param.img_size)

        # net.fit(train_set, epochs =2)
        dataloaders = {'train': DataLoader(train_set, batch_size=param.bs, shuffle=False, num_workers=0),
                       'validate': DataLoader(valid_set, batch_size=param.bs, shuffle=False, num_workers=0)}

        # for i, data in enumerate(dataloaders['train']):
        count = 0
        for i, data in enumerate(dataloaders['train']):
            torch.cuda.empty_cache()
            x = data['image']
            # x = transform(x)
            X = Variable(x).cuda()  # [N, 1, H, W]
            # model.half()
            # X = X.half()
            y = data['mask']
            # y = transform(y)

            Y = y#.type(torch.LongTensor)
            #Y = y.type(torch.LongTensor)
            Y = Variable(Y).cuda()
            # Y= Y.half()

            output = model(X)


            loss = criterion(output, Y)

            # model.float()
            optim.zero_grad()
            loss.backward()
            # model.float()
            optim.step()

            # print(loss.item())
            # print((i+1)%param.log_interval)


            if (epoch + 1) % 30 == 0:
                val = transform(x[0])
                lab = transform(data['mask'][0])

                pre = output[0].cpu()
                pred = pre.detach()


                out = transform(pred)

                pil = PILImageUtility(val, lab, out)


                pilsave = PILImageSave(val, lab, out)

                final = pilsave.save_images(w=512)


                pred_path_4 = basepath+"/train/Result/epoch_merged_" + str(
                    epoch + 1) + "_batch_" + str(count) + "predicted_thresholded_numpy_" + str(loss.item()) + ".png"

                #final.save(pred_path_4)


            #"""

            if (count + 1) % param.log_interval == 0:
                #print("got it")
                it += param.log_interval * param.bs
                iters.append(it)
                train_losses.append(loss.item())

                model.eval()
                val_loss = get_loss(dataloaders['validate'], model, epoch, basepath)
                # print(val_loss)
                model.train()
                val_losses.append(val_loss)

                if val_loss <= min_loss:
                    min_loss = val_loss

                    print(val_loss)
                    torch.save(model.state_dict(), basepath+"/UNET_HED.pth")
            #"""
            del X,Y

            count = count + 1

            #del X, Y, loss
        delta = time.time() - t_start

        print("Epoch #[{}/{}]\t\t Time: {:.2f}s current loss: {:.4f}s".format(epoch + 1, param.epochs, delta, min_loss))

    writer = pd.ExcelWriter('test.xlsx', engine='openpyxl')
    wb = writer.book
    df = pd.DataFrame({'Train_loss': train_losses,
                       'Val_loss': val_losses})

    df.to_excel(writer, index=False)
    wb.save(basepath+'/UNet-HED.xlsx')