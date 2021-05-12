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
#from EncoderDecoder import SegNet1
from PIL import Image
from openpyxl import load_workbook
import pandas as pd
from unet import  *
from utils import Superimpose, PILImageUtility, PILImageSave
def conv3x3(in_channels, out_channels, stride=1, padding=1, bias=True, groups=1):
    return nn.Conv2d(in_channels,
                     out_channels,
                     kernel_size=3,
                     stride=stride,
                     padding=padding,
                     bias=bias,
                     groups=groups)
def Upconv(in_channels, out_channels, stride=1, padding=1):
    return nn.Sequential(conv3x3(in_channels, out_channels, stride, padding),
                         nn.BatchNorm2d(out_channels),
                         nn.ReLU(inplace=True)

    )


class SegNet(nn.Module):

    def __init__(self, num_classes=3, n_init_features=3, drop_rate=0.5,
                 filter_config=(8, 16, 32, 64, 64)):
        super(SegNet, self).__init__()

        self.encoders = nn.ModuleList()
        self.decoders = nn.ModuleList()
        # setup number of conv-bn-relu blocks per module and number of filters
        encoder_n_layers = (2, 2, 3, 3, 3)
        encoder_filter_config = (n_init_features,) + filter_config
        decoder_n_layers = (3, 3, 3, 2, 2)
        decoder_filter_config = filter_config[::-1] + (filter_config[0],)
        #print(encoder_filter_config)

        for i in range(0, 5):
            # encoder architecture
            #print(encoder_filter_config[i])
            self.encoders.append(_Encoder(encoder_filter_config[i],
                                          encoder_filter_config[i + 1],
                                          encoder_n_layers[i], drop_rate))

            # decoder architecture
            self.decoders.append(_Decoder(decoder_filter_config[i],
                                          decoder_filter_config[i +1],
                                          decoder_n_layers[i], drop_rate))

        # final classifier (equivalent to a fully connected layer)
        self.classifier = nn.Conv2d(filter_config[0], num_classes, 3, 1, 1)
        #self.enc = nn.ModuleList(self.encoders)
        #self.dec = nn.ModuleList(self.decoders)

    def forward(self, x):
        indice = []
        unpool_sizes = []
        feat = x
        ind = None
        # encoder path, keep track of pooling indices and features size
        for i in range(0, 5):
            #print(self.encoders[i])
            feat,ind = self.encoders[i](feat)
            #feat = nn.Upsample(feat, scale_factor= 2)
            #print(ind.shape)
            #print(size)
            indice.append(ind)
            #print(len(indices))
            #print("size {}").format(shapes)

            #unpool_sizes.append(size)
        #print(unpool_sizes[0])
        # decoder path, upsampling with corresponding indices and size

        for i in range(0, 5):
            #feat = F.max_unpool2d(feat, indices=indice[4-i], kernel_size=2)
            #print(self.decoders[i])
            feat = self.decoders[i](feat, indice[4-i])
            #feat = F.max_unpool2d(feat, indices=indice[i], kernel_size=2)


        return F.softmax(F.relu(self.classifier(feat)), dim=2)


class _Encoder(nn.Module):
    def __init__(self, n_in_feat, n_out_feat, n_blocks=2, drop_rate=0.5):
        """Encoder layer follows VGG rules + keeps pooling indices
        Args:
            n_in_feat (int): number of input features
            n_out_feat (int): number of output features
            n_blocks (int): number of conv-batch-relu block inside the encoder
            drop_rate (float): dropout rate to use
        """
        super(_Encoder, self).__init__()


        if n_blocks  ==2:
            self.features= nn.Sequential(Upconv(n_in_feat,n_out_feat),
                                         Upconv(n_out_feat, n_out_feat)
            )
        elif n_blocks == 3:
            self.features = nn.Sequential(
                Upconv(n_in_feat, n_out_feat),
                Upconv(n_out_feat, n_out_feat),
                Upconv(n_out_feat, n_out_feat)
            )
        elif n_blocks==1:

            self.features = nn.Sequential(Upconv(n_in_feat, n_out_feat))


            #if n_blocks == 3:
                #layers += [nn.Dropout(drop_rate)]


    def forward(self, x):
        output = self.features(x)

        #print(F.max_pool2d(output, 2, 2, return_indices=True))
        output, ind = F.max_pool2d(output, 2,2, return_indices = True)
        return output, ind#F.max_pool2d(output, 2, 2, return_indices=True), output.shape


class _Decoder(nn.Module):
    """Decoder layer decodes the features by unpooling with respect to
    the pooling indices of the corresponding decoder part.
    Args:
        n_in_feat (int): number of input features
        n_out_feat (int): number of output features
        n_blocks (int): number of conv-batch-relu block inside the decoder
        drop_rate (float): dropout rate to use
    """
    def __init__(self, n_in_feat, n_out_feat, n_blocks=2, drop_rate=0.5):
        super(_Decoder, self).__init__()
        if n_blocks  ==2:
            self.features= nn.Sequential(Upconv(n_in_feat,n_out_feat),
                                         Upconv(n_out_feat, n_out_feat))
        elif n_blocks == 3:
            self.features = nn.Sequential(
                Upconv(n_in_feat, n_out_feat),
                Upconv(n_out_feat, n_out_feat),
                Upconv(n_out_feat, n_out_feat)
            )
        elif n_blocks==1:
            self.features = nn.Sequential(Upconv(n_in_feat, n_out_feat))


    def forward(self, x, ind):#, indices, size):
        unpooled = F.max_unpool2d(x, indices=ind, kernel_size=2)
        return self.features(unpooled)


"""
from torchsummary import  summary
model = SegNet().cuda()
summary(model, (3, 256, 256))
"""


class param:
    img_size = (512, 512)
    bs = 16
    num_workers = 4
    lr = 0.001
    epochs = 60
    unet_depth = 5
    unet_start_filters = 8
    log_interval = 30


criterion = torch.nn.BCELoss()
transform = transforms.Compose([
    transforms.ToPILImage()  # ,
    # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])


def get_loss(dl, model, epoch, count):
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

        curr_loss = F.binary_cross_entropy(output, Y).item()
        # print(torch.argmax(output[0], dim=0))
        loss += curr_loss

        val = transform(x[0])

        lab = transform(y[0])
        val = numpy.array(val)
        lab = numpy.array(lab)
        orig = val
        final1 = numpy.concatenate((orig, lab), axis=1)
        # print(lab)
        # print(torch.argmax(output[0], dim=0))
        pred = output[0].cpu()

        # pred = pred.view(param.img_size, param.img_size, 3)

        p = (pred.detach()).numpy()

        p = numpy.transpose(p, (1, 2, 0))
        p_out = numpy_threshold(p, 0.5)

        super = Superimpose(val, lab, p_out)

        p_super_impose, _ = super.superimpose_result()

        final2 = numpy.concatenate((p_out, p_super_impose), axis=1)
        final = numpy.concatenate((final1, final2), axis=0)

        pred_path_1 = "/media/purba/New Volume/CNN/label/SegNet-PIL/valid/Result/epoch_" + str(epoch) + "_batch_" + str(
            val_batch) + "predicted_thresholded_"+str(curr_loss)+".bmp"

        io.imsave(pred_path_1, final)

        val_batch = val_batch + 1
        #del X, Y, loss

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
    Label = Image.new(mode='RGB', size=image.size)
    labelpixel = Label.load()

    for i in range(image.size[0]):  # for every pixel:
        for j in range(image.size[1]):
            if pixels[i, j] == (255, 255, 255):
                labelpixel[i, j] = (1, 1, 1)
    return Label


def numpy_threshold(img, th):
    img1 = img
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            if img[i][j][0] >= th and img[i][j][1] >= th and img[i][j][2] >= th:
                img1[i, j, :] = 255
            else:
                img1[i, j, :] = 0
    return img1


def train():
    from skimage import data
    basepath = "/media/purba/New Volume/CNN/label/SegNet-PIL/"

    train_image_name = [f for f in os.listdir(basepath + '/train/original/') if '.JPG' in f]
    label_image_name = [f for f in os.listdir(basepath + '/train/label/') if '.bmp' in f]

    valid_image_name = [f for f in os.listdir(basepath + '/valid/original/') if '.JPG' in f]
    valid_label_image_name = [f for f in os.listdir(basepath + '/valid/label/') if '.bmp' in f]

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
        image = Image.open(basepath + '/train/original/' + train_image_name[i])  # .convert('RGB')
        train_image_list.append(image)
        label = Image.open(basepath + '/train/label/' + label_image_name[i])
        # label = convert_binary_pillow(label)
        label_image_list.append(label)

    for i in range(0, len(valid_image_name)):
        image = Image.open(basepath + '/valid/original/' + valid_image_name[i])
        valid_image_list.append(image)
        label = Image.open(basepath + '/valid/label/' + valid_label_image_name[i])
        # label = convert_binary_pillow(label)
        valid_label_list.append(label)

    # """
    model = SegNet().cuda()
    testmodel = model

    optim = torch.optim.Adam(model.parameters())

    # summary(model,(3, 256, 256))

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
    for epoch in range(0, 15):
        torch.cuda.empty_cache()

        t_start = time.time()
        train_set = PILDataset(train_image_list, label_image_list, 3, 200, image_size=param.img_size)
        valid_set = PILDataset(valid_image_list, valid_label_list, 1, 100, image_size=param.img_size)

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

            Y = y  # .type(torch.LongTensor)
            Y = Variable(Y).cuda()
            # Y= Y.half()

            output = model(X)


                # pred.save(pred_path)

            # print(i)

            count = count + 1
            # print(output.shape)
            # output = output.view(output.shape[0], output.shape[1] * output.shape[2] * output.shape[3])
            # y = y.view(y.shape[0], y.shape[1] * y.shape[2] * y.shape[3])

            loss = F.binary_cross_entropy(output, Y)  # criterion(output, Y)

            # model.float()
            optim.zero_grad()
            loss.backward()
            # model.float()
            optim.step()

            # print(loss.item())
            # print((i+1)%param.log_interval)

            if (epoch + 1) % 1 == 0:

                val = transform(x[0])
                lab = transform(y[0])

                pre =  output[0].cpu()
                pred = pre.detach()

                out = transform(pred)

                pil = PILImageUtility(val, lab, out)

                label = pil.convert_threshold_pillow(0.7)

                pilsave = PILImageSave(val, lab, label)

                final = pilsave.save_images(w=512)

                pred_path_3 = "/media/purba/New Volume/CNN/label/SegNet-PIL/train/Result/epoch_" + str(
                    epoch + 1) + "_batch_" + str(count) + "predicted_thresholded_numpy_" + str(loss.item()) + ".png"

                label.save(pred_path_3)

                pred_path_4 = "/media/purba/New Volume/CNN/label/SegNet-PIL/train/Result/epoch_merged_" + str(
                    epoch + 1) + "_batch_" + str(count) + "predicted_thresholded_numpy_" + str(loss.item()) + ".png"

                final.save(pred_path_4)

                """
                
                val = transform(x[0])

                lab = transform(y[0])
                val = numpy.array(val)
                lab = numpy.array(lab)
                orig = val

                final1  =  numpy.concatenate((orig, lab), axis=1)
                # print(lab)
                # print(torch.argmax(output[0], dim=0))

                pred = output[0].cpu()

                # pred = pred.view(param.img_size, param.img_size, 3)

                p = (pred.detach()).numpy()

                p = numpy.transpose(p, (1, 2, 0))
                p_out = numpy_threshold(p, 0.8)



                p_super_impose, _ = superimpose_result(val, lab, p_out)

                final2 = numpy.concatenate((p_out, p_super_impose), axis=1)
                final = numpy.concatenate((final1, final2), axis=0)

                pred_path_3 = "/media/purba/New Volume/CNN/label/SegNet-8-16-32-64-Japan/train/Result/epoch_" + str(
                    epoch+1) + "_batch_" + str(count) + "predicted_thresholded_numpy_"+str(loss.item())+".bmp"

                io.imsave(pred_path_3, final)
                                
                """

            """
            if (count + 1) % param.log_interval == 0:
                # print("got it")
                it += param.log_interval * param.bs
                iters.append(it)
                train_losses.append(loss.item())

                model.eval()
                val_loss = get_loss(dataloaders['validate'], model, epoch, count)
                # print(val_loss)
                model.train()
                val_losses.append(val_loss)

                if val_loss < min_loss:
                    min_loss = val_loss

                    # print(val_loss)
                    torch.save(model.state_dict(), "/home/purba/Documents/SegNet-8-16-32-64-Japan.pth")
            """

            count = count + 1

            #del X, Y, loss
        delta = time.time() - t_start

        print("Epoch #[{}/{}]\t\t Time: {:.2f}s current loss: {:.4f}s".format(epoch + 1, param.epochs, delta, min_loss))


    writer = pd.ExcelWriter('test.xlsx', engine='openpyxl')
    wb = writer.book
    df = pd.DataFrame({'Train_loss': train_losses,
                       'Val_loss': val_losses})

    df.to_excel(writer, index=False)
    wb.save('/home/purba/Documents/SegNet-8-16-32-64-Japan.xlsx')



def testandsave(testmodel, dl, basepath, batchsize):

    tf = transforms.Compose([
        transforms.ToTensor()  # ,
        # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    testmodel.eval()
    Result_Table = []

    for i, data in enumerate(dl):
        torch.cuda.empty_cache()
        x = data['image']
        # x = transform(x)
        X = Variable(x).cuda()  # [N, 1, H, W]
        y = data['mask']
        # y = transform(y)

        Y = y  # .type(torch.LongTensor)
        Y = Variable(Y).cuda()

        output = testmodel(X)

        val_batch = 0
        for i in range(0, batchsize):
            val = transform(x[val_batch])

            lab = transform(y[val_batch])
            val = numpy.array(val)
            lab = numpy.array(lab)
            orig = val
            final1 = numpy.concatenate((orig, lab), axis=1)
            # print(lab)
            # print(torch.argmax(output[0], dim=0))
            pred = output[val_batch].cpu()

            # pred = pred.view(param.img_size, param.img_size, 3)

            p = (pred.detach()).numpy()

            p = numpy.transpose(p, (1, 2, 0))
            p_out = numpy_threshold(p, 0.8)

            super = Superimpose(val,lab, p_out)
            p_super, a = super.superimpose_result()

            #print(p_super.shape)
            #print(a)

            Result_Table.append(a)
            final2 = numpy.concatenate((p_out, p_super), axis=1)
            final_segnet = numpy.concatenate((final1, final2), axis=0)

            pred_path_1 = basepath+"//valid//epoch_" + str(
                1) + "_batch_" + str(
                val_batch) + "predicted_thresholded_new_" + str(0) + ".png"

            io.imsave(pred_path_1, final_segnet)

            val_batch = val_batch + 1
    return Result_Table


def test():
    basepath = "/media/purba/New Volume/CNN/label/SegNet-8-16-32-64//"



    valid_image_name = [f for f in os.listdir(basepath + '/valid/original/') if '.JPG' in f]
    valid_label_image_name = [f for f in os.listdir(basepath + '/valid/label/') if '.bmp' in f]

    train_image_list = []
    label_image_list = []
    valid_image_list = []
    valid_label_list = []

    valid_image_name.sort()
    valid_label_image_name.sort()


    for i in range(0, len(valid_image_name)):
        image = Image.open(basepath + '/valid/original/' + valid_image_name[i])
        valid_image_list.append(image)
        label = Image.open(basepath + '/valid/label/' + valid_label_image_name[i])
        # label = convert_binary_pillow(label)
        valid_label_list.append(label)


    segnet= SegNet().cuda()
    segnet.load_state_dict(torch.load("/home/purba/Documents/Segnet_8_16_32_64_64.pth"))


    tf = transforms.Compose([
        transforms.ToTensor()  # ,
        # transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    unet = UNet(3, depth=param.unet_depth,
                     start_filts=param.unet_start_filters,
                     merge_mode='concat').cuda()
    unet.load_state_dict(torch.load("/home/purba/Documents/Unet_val_1000_new.pth"))




    train_set = PILDataset(valid_image_list, valid_label_list, len(valid_image_list), 2, image_size=[2048,2048])


    # net.fit(train_set, epochs =2)
    dataloaders = {'train': DataLoader(train_set, batch_size=2, shuffle=False, num_workers=0)}

    loss = 0
    dl = dataloaders['train']
    basepath = "/media/purba/New Volume/CNN/label/SegNet-8-16-32-64//"
    Result_Table = testandsave(segnet, dl, basepath, 2)
    Result_Table_Unet = testandsave(unet, dl, "/media/purba/New Volume/CNN/label/UNet/", 2)

    Result = []

    for i in range(0, len(Result_Table)):
        Result.append(["Segnet", Result_Table[i][0], Result_Table[i][1], Result_Table[i][2], Result_Table[i][3], Result_Table[i][4], Result_Table[i][5],
                      (Result_Table[i][0]/Result_Table[i][4])*100, (Result_Table[i][1]/Result_Table[i][5])*100,
                      (Result_Table[i][2]/Result_Table[i][5])*100, (Result_Table[i][3]/Result_Table[i][4])*100])
        Result.append(["Unet", Result_Table_Unet[i][0], Result_Table_Unet[i][1], Result_Table_Unet[i][2], Result_Table_Unet[i][3], Result_Table_Unet[i][4], Result_Table_Unet[i][5],
                      (Result_Table_Unet[i][0]/Result_Table_Unet[i][4])*100, (Result_Table_Unet[i][1]/Result_Table_Unet[i][5])*100,
                      (Result_Table_Unet[i][2]/Result_Table_Unet[i][5])*100, (Result_Table_Unet[i][3]/Result_Table_Unet[i][4])*100])

    writer = pd.ExcelWriter('test.xlsx', engine='openpyxl')
    wb = writer.book
    df = pd.DataFrame(Result)

    df.to_excel(writer, index=False)
    wb.save('/home/purba/Documents/Result1.xlsx')

        # del X, Y, loss
"""

writer = pd.ExcelWriter('test.xlsx', engine='openpyxl')
wb = writer.book
df = pd.DataFrame(Result)

df.to_excel(writer, index=False)
wb.save('/home/purba/Documents/Result.xlsx')

"""