imageLength=512
imageWidth=512
numEpochs=100
numBatches=16
trainData="/home/yifeng/Documents/Network/Validation"
labelData="/home/yifeng/Documents/Network/Validation"
numWorkers=4
learningRate=.001
logInterval=300
startFilters=8
inputImageType="png"
outputImageType="png"
kernel=[4,8,16,32,32]
numClasses=3
depth=5
nInitFeatures=3
factor=[2,4,8,16,32]
dropRate=.5
filterConfig=(4, 8, 16, 32, 64)
encoderLayers=(2, 2, 3, 3, 3)
decoderLayers=(3, 3, 3, 2, 2)
EL1numBlocks=1
EL1convLevel="7 x 7"
EL1activationFunc="Batch Normalization and ReLU"
EL1inChannel=3
EL1outChannel=4
EL1bias=True
EL1stride=1
EL1padding=0
EL1groups=1
EL2numBlocks=1
EL2convLevel="7 x 7"
EL2activationFunc="Batch Normalization and ReLU"
EL2inChannel=4
EL2outChannel=8
EL2bias=True
EL2stride=1
EL2padding=0
EL2groups=1
EL3numBlocks=1
EL3convLevel="7 x 7"
EL3activationFunc="Batch Normalization and ReLU"
EL3inChannel=8
EL3outChannel=16
EL3bias=True
EL3stride=1
EL3padding=0
EL3groups=1
EL4numBlocks=1
EL4convLevel="7 x 7"
EL4activationFunc="Batch Normalization and ReLU"
EL4inChannel=16
EL4outChannel=32
EL4bias=True
EL4stride=1
EL4padding=0
EL4groups=1
EL5numBlocks=1
EL5convLevel="7 x 7"
EL5activationFunc="Batch Normalization and ReLU"
EL5inChannel=32
EL5outChannel=64
EL5bias=True
EL5stride=1
EL5padding=0
EL5groups=1
DL1numBlocks=1
DL1convLevel="7 x 7"
DL1activationFunc="Batch Normalization and ReLU"
DL1inChannel=3
DL1outChannel=4
DL1bias=True
DL1stride=1
DL1padding=0
DL1groups=1
DL2numBlocks=1
DL2convLevel="7 x 7"
DL2activationFunc="Batch Normalization and ReLU"
DL2inChannel=4
DL2outChannel=8
DL2bias=True
DL2stride=1
DL2padding=0
DL2groups=1
DL3numBlocks=1
DL3convLevel="7 x 7"
DL3activationFunc="Batch Normalization and ReLU"
DL3inChannel=8
DL3outChannel=16
DL3bias=True
DL3stride=1
DL3padding=0
DL3groups=1
DL4numBlocks=1
DL4convLevel="7 x 7"
DL4activationFunc="Batch Normalization and ReLU"
DL4inChannel=16
DL4outChannel=32
DL4bias=True
DL4stride=1
DL4padding=0
DL4groups=1
DL5numBlocks=1
DL5convLevel="7 x 7"
DL5activationFunc="Batch Normalization and ReLU"
DL5inChannel=32
DL5outChannel=64
DL5bias=True
DL5stride=1
DL5padding=0
DL5groups=1
