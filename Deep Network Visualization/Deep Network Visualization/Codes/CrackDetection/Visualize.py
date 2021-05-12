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

class Visualize():
    def __init__(self, model, input, path):
        super(Visualize, self).__init__()
        self.model = model
        self.input = input
        self.path = path

    def visualize_encoder(self):
        output = self.model.forward(self.input)
        pre = output[0].cpu()
        pred = pre.detach()

        out_numpy = pred.numpy()

        out_numpy = out_numpy[0]  # numpy.transpose(out_numpy, (2,1,0))

        output_image = out_numpy[0]
        for k in range(1, out_numpy.shape[0]):
            output_image = numpy.concatenate((output_image, out_numpy[k]), axis=1)
        io.imsave(self.path, output_image)

        return output[0],output[1]

    def visualize_sides(self):
        output = self.model.forward(self.input)
        #print(output)

        pre = output[0].cpu()
        #print(pre)
        pred = pre.detach()

        out_numpy = pred.numpy()

        out_numpy = out_numpy  # numpy.transpose(out_numpy, (2,1,0))

        output_image = numpy.transpose(out_numpy, (2,1,0))

        out = out_numpy[0]
        print(output_image.shape)
        for k in range(1, out_numpy.shape[0]):
            out = numpy.concatenate((out, out_numpy[k]), axis=1)
        #print(out.shape)
        io.imsave(self.path, out)
        #io.imsave(self.path, output_image)

        return output

    def visualize_decoder(self, index):
        output = self.model.forward(self.input, index)
        pre = output[1].cpu()
        pred = pre.detach()

        out_numpy = pred.numpy()

        out_numpy = out_numpy[0]  # numpy.transpose(out_numpy, (2,1,0))

        output_image = out_numpy[0]
        for k in range(1, out_numpy.shape[0]):
            output_image = numpy.concatenate((output_image, out_numpy[k]), axis=1)
        io.imsave(self.path, output_image)

        return output

