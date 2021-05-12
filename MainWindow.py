# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets


# noinspection PyAttributeOutsideInit
from PyQt5.QtWidgets import QSizePolicy
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

# noinspection PyAttributeOutsideInit
from PyQt5.QtWidgets import QSizePolicy

from test import TestingWindow
from train import TrainingWindow
from functools import partial


class Ui_MainWindow(object):

    def setupUi(self, MainWindow, trainInput, validInput):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2065, 1409)
        MainWindow.setStyleSheet("QMainWindow {background: #99AAB5;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_216 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_216.setObjectName("verticalLayout_216")
        self.horizontalLayout_73 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_73.setObjectName("horizontalLayout_73")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.label_selectNetwork = QtWidgets.QLabel(self.centralwidget)
        self.label_selectNetwork.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_selectNetwork.setObjectName("label_selectNetwork")
        self.verticalLayout.addWidget(self.label_selectNetwork)

        spacerItem = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.networkErrorLabel = QtWidgets.QLabel(self.centralwidget)
        self.networkErrorLabel.setMinimumSize(QtCore.QSize(0, 30))
        self.networkErrorLabel.setText("")
        self.networkErrorLabel.setObjectName("networkErrorLabel")
        self.networkErrorLabel.setStyleSheet('color: red')
        self.networkErrorLabel.setWordWrap(True)
        self.verticalLayout.addWidget(self.networkErrorLabel)

        spacerItem1 = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.networkComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.networkComboBox.setObjectName("networkComboBox")
        self.networkComboBox.addItem("")
        self.networkComboBox.addItem("")
        self.networkComboBox.setCurrentIndex(1)
        self.verticalLayout.addWidget(self.networkComboBox)
        self.verticalLayout_5.addLayout(self.verticalLayout)

        spacerItem2 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)

        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)

        spacerItem3 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)

        self.imageSizeError = QtWidgets.QLabel(self.centralwidget)
        self.imageSizeError.setText("")
        self.imageSizeError.setObjectName("imageSizeError")
        self.imageSizeError.setStyleSheet('color: red')
        self.imageSizeError.setWordWrap(True)
        self.verticalLayout_4.addWidget(self.imageSizeError)
        spacerItem4 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.imageLength = QtWidgets.QLineEdit(self.centralwidget)
        self.imageLength.setObjectName("imageLength")
        self.imageLength.setText("512");
        self.horizontalLayout_2.addWidget(self.imageLength)
        spacerItem5 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)

        self.ImageWidth = QtWidgets.QLineEdit(self.centralwidget)
        self.ImageWidth.setObjectName("ImageWidth")
        self.ImageWidth.setText("512")
        self.horizontalLayout_2.addWidget(self.ImageWidth)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem6 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_numOfEpochs = QtWidgets.QLabel(self.centralwidget)
        self.label_numOfEpochs.setObjectName("label_numOfEpochs")
        self.verticalLayout_2.addWidget(self.label_numOfEpochs)
        spacerItem7 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)

        self.epochErrorLabel = QtWidgets.QLabel(self.centralwidget)
        self.epochErrorLabel.setText("")
        self.epochErrorLabel.setObjectName("epochErrorLabel")
        self.epochErrorLabel.setStyleSheet('color: red')
        self.epochErrorLabel.setWordWrap(True)
        self.verticalLayout_2.addWidget(self.epochErrorLabel)
        spacerItem8 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem8)

        self.numEpochs = QtWidgets.QLineEdit(self.centralwidget)
        self.numEpochs.setObjectName("numEpochs")
        self.numEpochs.setText("100")
        self.verticalLayout_2.addWidget(self.numEpochs)
        spacerItem9 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem9)

        self.label_numOfBatches = QtWidgets.QLabel(self.centralwidget)
        self.label_numOfBatches.setObjectName("label_numOfBatches")
        self.verticalLayout_2.addWidget(self.label_numOfBatches)
        spacerItem10 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)

        self.batchErrorLabel = QtWidgets.QLabel(self.centralwidget)
        self.batchErrorLabel.setText("")
        self.batchErrorLabel.setObjectName("batchErrorLabel")
        self.batchErrorLabel.setStyleSheet('color: red')
        self.batchErrorLabel.setWordWrap(True)
        self.verticalLayout_2.addWidget(self.batchErrorLabel)
        spacerItem11 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem11)

        self.numBatches = QtWidgets.QLineEdit(self.centralwidget)
        self.numBatches.setObjectName("numBatches")
        self.numBatches.setText("16")
        self.verticalLayout_2.addWidget(self.numBatches)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem12 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)

        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_trainData = QtWidgets.QLabel(self.centralwidget)
        self.label_trainData.setObjectName("label_trainData")
        self.verticalLayout_3.addWidget(self.label_trainData)
        spacerItem13 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem13)

        self.trainingErrorLabel = QtWidgets.QLabel(self.centralwidget)
        self.trainingErrorLabel.setText("")
        self.trainingErrorLabel.setObjectName("trainingErrorLabel")
        self.trainingErrorLabel.setStyleSheet('color: red')
        self.trainingErrorLabel.setWordWrap(True)
        self.verticalLayout_3.addWidget(self.trainingErrorLabel)
        spacerItem14 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem14)

        self.trainDataLocation = QtWidgets.QLineEdit(self.centralwidget)
        self.trainDataLocation.setObjectName("trainDataLocation")
        self.trainDataLocation.setText(trainInput)
        self.verticalLayout_3.addWidget(self.trainDataLocation)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        spacerItem15 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem15)

        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_labeledData_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_labeledData_2.setObjectName("label_labeledData_2")
        self.verticalLayout_6.addWidget(self.label_labeledData_2)
        spacerItem16 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem16)

        self.labeledErrorLabel = QtWidgets.QLabel(self.centralwidget)
        self.labeledErrorLabel.setText("")
        self.labeledErrorLabel.setObjectName("labeledErrorLabel")
        self.labeledErrorLabel.setStyleSheet('color: red')
        self.labeledErrorLabel.setWordWrap(True)
        self.verticalLayout_6.addWidget(self.labeledErrorLabel)
        spacerItem17 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem17)

        self.labeledDataFileLocation = QtWidgets.QLineEdit(self.centralwidget)
        self.labeledDataFileLocation.setObjectName("labeledDataFileLocation")
        self.labeledDataFileLocation.setText(validInput)
        self.verticalLayout_6.addWidget(self.labeledDataFileLocation)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        spacerItem18 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem18)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        spacerItem19 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem19)

        self.numWorkersErrorLabel = QtWidgets.QLabel(self.centralwidget)
        self.numWorkersErrorLabel.setText("")
        self.numWorkersErrorLabel.setObjectName("numWorkersErrorLabel")
        self.numWorkersErrorLabel.setStyleSheet('color: red')
        self.numWorkersErrorLabel.setWordWrap(True)
        self.verticalLayout_8.addWidget(self.numWorkersErrorLabel)
        spacerItem20 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem20)

        self.numWorkers = QtWidgets.QLineEdit(self.centralwidget)
        self.numWorkers.setObjectName("numWorkers")
        self.numWorkers.setText("4")
        self.verticalLayout_8.addWidget(self.numWorkers)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        spacerItem21 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem21)

        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3)
        spacerItem22 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem22)

        self.LRErrorLabel = QtWidgets.QLabel(self.centralwidget)
        self.LRErrorLabel.setText("")
        self.LRErrorLabel.setObjectName("LRErrorLabel")
        self.LRErrorLabel.setStyleSheet('color: red')
        self.LRErrorLabel.setWordWrap(True)
        self.verticalLayout_9.addWidget(self.LRErrorLabel)
        spacerItem23 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem23)

        self.LREntry = QtWidgets.QLineEdit(self.centralwidget)
        self.LREntry.setObjectName("LREntry")
        self.LREntry.setText(".001")
        self.verticalLayout_9.addWidget(self.LREntry)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem24 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem24)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_12.addWidget(self.label_6)
        spacerItem25 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem25)

        self.logIntervalsErrLabel = QtWidgets.QLabel(self.centralwidget)
        self.logIntervalsErrLabel.setText("")
        self.logIntervalsErrLabel.setObjectName("logIntervalsErrLabel")
        self.logIntervalsErrLabel.setStyleSheet('color: red')
        self.logIntervalsErrLabel.setWordWrap(True)
        self.verticalLayout_12.addWidget(self.logIntervalsErrLabel)
        spacerItem26 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem26)

        self.LogIntervals = QtWidgets.QLineEdit(self.centralwidget)
        self.LogIntervals.setObjectName("LogIntervals")
        self.LogIntervals.setText("300")
        self.verticalLayout_12.addWidget(self.LogIntervals)
        self.horizontalLayout_4.addLayout(self.verticalLayout_12)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        spacerItem27 = QtWidgets.QSpacerItem(13, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem27)

        self.trainButton = QtWidgets.QPushButton(self.centralwidget)
        self.trainButton.setObjectName("trainButton")
        self.verticalLayout_5.addWidget(self.trainButton)
        self.horizontalLayout_73.addLayout(self.verticalLayout_5)
        spacerItem28 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_73.addItem(spacerItem28)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(1400, 1000))
        self.tabWidget.setObjectName("tabWidget")
        self.networkOverview = QtWidgets.QWidget()
        self.networkOverview.setObjectName("networkOverview")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.networkOverview)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout()
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")

        self.networkOverviewPicture = QtWidgets.QLabel(self.networkOverview)
        self.networkOverviewPicture.setMinimumSize(QtCore.QSize(0, 150))
        self.networkOverviewPicture.setAutoFillBackground(True)
        self.networkOverviewPicture.setObjectName("networkOverviewPicture")



        self.verticalLayout_10.addWidget(self.networkOverviewPicture)
        spacerItem29 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_10.addItem(spacerItem29)

        self.networkOverviewDescription = QtWidgets.QLabel(self.networkOverview)
        self.networkOverviewDescription.setMinimumSize(QtCore.QSize(0, 150))
        self.networkOverviewDescription.setAutoFillBackground(True)
        self.networkOverviewDescription.setObjectName("networkOverviewDescription")
        self.verticalLayout_10.addWidget(self.networkOverviewDescription)
        self.verticalLayout_36.addLayout(self.verticalLayout_10)
        spacerItem30 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_36.addItem(spacerItem30)

        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.startFilters = QtWidgets.QLabel(self.networkOverview)
        self.startFilters.setObjectName("startFilters")
        self.verticalLayout_11.addWidget(self.startFilters)
        spacerItem31 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_11.addItem(spacerItem31)

        self.startFiltersErr = QtWidgets.QLabel(self.networkOverview)
        self.startFiltersErr.setText("")
        self.startFiltersErr.setObjectName("startFiltersErr")
        self.startFiltersErr.setStyleSheet('color: red')
        self.startFiltersErr.setWordWrap(True)
        self.verticalLayout_11.addWidget(self.startFiltersErr)
        spacerItem32 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_11.addItem(spacerItem32)

        self.startFiltersInput = QtWidgets.QLineEdit(self.networkOverview)
        self.startFiltersInput.setObjectName("startFiltersInput")
        self.startFiltersInput.setText("8")
        self.verticalLayout_11.addWidget(self.startFiltersInput)
        self.horizontalLayout_9.addLayout(self.verticalLayout_11)
        spacerItem33 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem33)

        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.inputImageFileType = QtWidgets.QLabel(self.networkOverview)
        self.inputImageFileType.setObjectName("inputImageFileType")
        self.verticalLayout_13.addWidget(self.inputImageFileType)
        spacerItem34 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_13.addItem(spacerItem34)

        self.inputImageFileTypeErr = QtWidgets.QLabel(self.networkOverview)
        self.inputImageFileTypeErr.setText("")
        self.inputImageFileTypeErr.setObjectName("inputImageFileTypeErr")
        self.inputImageFileTypeErr.setStyleSheet('color: red')
        self.inputImageFileTypeErr.setWordWrap(True)
        self.verticalLayout_13.addWidget(self.inputImageFileTypeErr)
        spacerItem35 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_13.addItem(spacerItem35)

        self.inputImageFileInput = QtWidgets.QLineEdit(self.networkOverview)
        self.inputImageFileInput.setObjectName("inputImageFileInput")
        self.inputImageFileInput.setText("png")
        self.verticalLayout_13.addWidget(self.inputImageFileInput)
        self.horizontalLayout_9.addLayout(self.verticalLayout_13)
        spacerItem36 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem36)

        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.outputImageFileType = QtWidgets.QLabel(self.networkOverview)
        self.outputImageFileType.setObjectName("outputImageFileType")
        self.verticalLayout_19.addWidget(self.outputImageFileType)
        spacerItem37 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_19.addItem(spacerItem37)

        self.outputImageFileTypeErr = QtWidgets.QLabel(self.networkOverview)
        self.outputImageFileTypeErr.setText("")
        self.outputImageFileTypeErr.setObjectName("outputImageFileTypeErr")
        self.outputImageFileTypeErr.setStyleSheet('color: red')
        self.outputImageFileTypeErr.setWordWrap(True)
        self.verticalLayout_19.addWidget(self.outputImageFileTypeErr)
        spacerItem38 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_19.addItem(spacerItem38)

        self.outputImageFileTypeInput = QtWidgets.QLineEdit(self.networkOverview)
        self.outputImageFileTypeInput.setObjectName("outputImageFileTypeInput")
        self.outputImageFileTypeInput.setText("png")
        self.verticalLayout_19.addWidget(self.outputImageFileTypeInput)
        self.horizontalLayout_9.addLayout(self.verticalLayout_19)
        spacerItem39 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem39)

        self.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.kernel = QtWidgets.QLabel(self.networkOverview)
        self.kernel.setObjectName("kernel")
        self.verticalLayout_26.addWidget(self.kernel)
        spacerItem40 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_26.addItem(spacerItem40)

        self.kernelErr = QtWidgets.QLabel(self.networkOverview)
        self.kernelErr.setText("")
        self.kernelErr.setObjectName("kernelErr")
        self.kernelErr.setStyleSheet('color: red')
        self.kernelErr.setWordWrap(True)
        self.verticalLayout_26.addWidget(self.kernelErr)
        spacerItem41 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_26.addItem(spacerItem41)

        self.kernelInput = QtWidgets.QLineEdit(self.networkOverview)
        self.kernelInput.setObjectName("kernelInput")
        self.kernelInput.setText("[4,8,16,32,32]")
        self.verticalLayout_26.addWidget(self.kernelInput)
        self.horizontalLayout_9.addLayout(self.verticalLayout_26)
        self.verticalLayout_36.addLayout(self.horizontalLayout_9)
        spacerItem42 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_36.addItem(spacerItem42)

        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.numberOfClasses = QtWidgets.QLabel(self.networkOverview)
        self.numberOfClasses.setObjectName("numberOfClasses")
        self.verticalLayout_17.addWidget(self.numberOfClasses)
        spacerItem43 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_17.addItem(spacerItem43)

        self.numberOfClassesErr = QtWidgets.QLabel(self.networkOverview)
        self.numberOfClassesErr.setText("")
        self.numberOfClassesErr.setObjectName("numberOfClassesErr")
        self.numberOfClassesErr.setStyleSheet('color: red')
        self.numberOfClassesErr.setWordWrap(True)
        self.verticalLayout_17.addWidget(self.numberOfClassesErr)
        spacerItem44 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_17.addItem(spacerItem44)

        self.numberOfClassesInput = QtWidgets.QLineEdit(self.networkOverview)
        self.numberOfClassesInput.setObjectName("numberOfClassesInput")
        self.numberOfClassesInput.setText("3")
        self.verticalLayout_17.addWidget(self.numberOfClassesInput)
        self.horizontalLayout_10.addLayout(self.verticalLayout_17)
        spacerItem45 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem45)

        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.depth = QtWidgets.QLabel(self.networkOverview)
        self.depth.setObjectName("depth")
        self.verticalLayout_18.addWidget(self.depth)
        spacerItem46 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_18.addItem(spacerItem46)

        self.depthErr = QtWidgets.QLabel(self.networkOverview)
        self.depthErr.setText("")
        self.depthErr.setObjectName("depthErr")
        self.depthErr.setStyleSheet('color: red')
        self.depthErr.setWordWrap(True)
        self.verticalLayout_18.addWidget(self.depthErr)
        spacerItem47 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_18.addItem(spacerItem47)

        self.depthInput = QtWidgets.QLineEdit(self.networkOverview)
        self.depthInput.setObjectName("depthInput")
        self.depthInput.setText("5")
        self.verticalLayout_18.addWidget(self.depthInput)
        self.horizontalLayout_10.addLayout(self.verticalLayout_18)
        spacerItem48 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem48)

        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.nInitFeatures = QtWidgets.QLabel(self.networkOverview)
        self.nInitFeatures.setObjectName("nInitFeatures")
        self.verticalLayout_20.addWidget(self.nInitFeatures)
        spacerItem49 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_20.addItem(spacerItem49)

        self.nInitFeaturesErr = QtWidgets.QLabel(self.networkOverview)
        self.nInitFeaturesErr.setText("")
        self.nInitFeaturesErr.setObjectName("nInitFeaturesErr")
        self.nInitFeaturesErr.setStyleSheet('color: red')
        self.nInitFeaturesErr.setWordWrap(True)
        self.verticalLayout_20.addWidget(self.nInitFeaturesErr)
        spacerItem50 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_20.addItem(spacerItem50)

        self.nInitFeaturesInput = QtWidgets.QLineEdit(self.networkOverview)
        self.nInitFeaturesInput.setObjectName("nInitFeaturesInput")
        self.nInitFeaturesInput.setText("3")
        self.verticalLayout_20.addWidget(self.nInitFeaturesInput)
        self.horizontalLayout_10.addLayout(self.verticalLayout_20)
        spacerItem51 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem51)

        self.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.factor = QtWidgets.QLabel(self.networkOverview)
        self.factor.setObjectName("factor")
        self.verticalLayout_25.addWidget(self.factor)
        spacerItem52 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_25.addItem(spacerItem52)

        self.factorErr = QtWidgets.QLabel(self.networkOverview)
        self.factorErr.setText("")
        self.factorErr.setObjectName("factorErr")
        self.factorErr.setStyleSheet('color: red')
        self.factorErr.setWordWrap(True)
        self.verticalLayout_25.addWidget(self.factorErr)
        spacerItem53 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_25.addItem(spacerItem53)

        self.factorInput = QtWidgets.QLineEdit(self.networkOverview)
        self.factorInput.setObjectName("factorInput")
        self.factorInput.setText("[2,4,8,16,32]")
        self.verticalLayout_25.addWidget(self.factorInput)
        self.horizontalLayout_10.addLayout(self.verticalLayout_25)
        self.verticalLayout_36.addLayout(self.horizontalLayout_10)
        spacerItem54 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_36.addItem(spacerItem54)

        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.dropRate = QtWidgets.QLabel(self.networkOverview)
        self.dropRate.setObjectName("dropRate")
        self.verticalLayout_21.addWidget(self.dropRate)
        spacerItem55 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_21.addItem(spacerItem55)

        self.dropRateErr = QtWidgets.QLabel(self.networkOverview)
        self.dropRateErr.setText("")
        self.dropRateErr.setObjectName("dropRateErr")
        self.dropRateErr.setStyleSheet('color: red')
        self.dropRateErr.setWordWrap(True)
        self.verticalLayout_21.addWidget(self.dropRateErr)
        spacerItem56 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_21.addItem(spacerItem56)

        self.dropRateInput = QtWidgets.QLineEdit(self.networkOverview)
        self.dropRateInput.setObjectName("dropRateInput")
        self.dropRateInput.setText(".5")
        self.verticalLayout_21.addWidget(self.dropRateInput)
        self.horizontalLayout_8.addLayout(self.verticalLayout_21)
        spacerItem57 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem57)

        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.filterConfiguration = QtWidgets.QLabel(self.networkOverview)
        self.filterConfiguration.setObjectName("filterConfiguration")
        self.verticalLayout_22.addWidget(self.filterConfiguration)
        spacerItem58 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_22.addItem(spacerItem58)

        self.filterConfigurationErr = QtWidgets.QLabel(self.networkOverview)
        self.filterConfigurationErr.setText("")
        self.filterConfigurationErr.setObjectName("filterConfigurationErr")
        self.filterConfigurationErr.setStyleSheet('color: red')
        self.filterConfigurationErr.setWordWrap(True)
        self.verticalLayout_22.addWidget(self.filterConfigurationErr)
        spacerItem59 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_22.addItem(spacerItem59)

        self.filterConfigurationInput = QtWidgets.QLineEdit(self.networkOverview)
        self.filterConfigurationInput.setObjectName("filterConfigurationInput")
        self.filterConfigurationInput.setText("(4, 8, 16, 32, 64)")
        self.verticalLayout_22.addWidget(self.filterConfigurationInput)
        self.horizontalLayout_8.addLayout(self.verticalLayout_22)
        spacerItem60 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem60)

        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.encoderLayers = QtWidgets.QLabel(self.networkOverview)
        self.encoderLayers.setObjectName("encoderLayers")
        self.verticalLayout_23.addWidget(self.encoderLayers)
        spacerItem61 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_23.addItem(spacerItem61)

        self.encoderLayersErr = QtWidgets.QLabel(self.networkOverview)
        self.encoderLayersErr.setText("")
        self.encoderLayersErr.setObjectName("encoderLayersErr")
        self.encoderLayersErr.setStyleSheet('color: red')
        self.encoderLayersErr.setWordWrap(True)
        self.verticalLayout_23.addWidget(self.encoderLayersErr)
        spacerItem62 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_23.addItem(spacerItem62)

        self.encoderLayersInput = QtWidgets.QLineEdit(self.networkOverview)
        self.encoderLayersInput.setObjectName("encoderLayersInput")
        self.encoderLayersInput.setText("(2, 2, 3, 3, 3)")
        self.verticalLayout_23.addWidget(self.encoderLayersInput)
        self.horizontalLayout_8.addLayout(self.verticalLayout_23)
        spacerItem63 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem63)

        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.decoderLayers = QtWidgets.QLabel(self.networkOverview)
        self.decoderLayers.setObjectName("decoderLayers")
        self.verticalLayout_24.addWidget(self.decoderLayers)
        spacerItem64 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_24.addItem(spacerItem64)

        self.decoderLayersErr = QtWidgets.QLabel(self.networkOverview)
        self.decoderLayersErr.setText("")
        self.decoderLayersErr.setObjectName("decoderLayersErr")
        self.decoderLayersErr.setStyleSheet('color: red')
        self.decoderLayersErr.setWordWrap(True)
        self.verticalLayout_24.addWidget(self.decoderLayersErr)
        spacerItem65 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_24.addItem(spacerItem65)

        self.decoderLayersInput = QtWidgets.QLineEdit(self.networkOverview)
        self.decoderLayersInput.setObjectName("decoderLayersInput")
        self.decoderLayersInput.setText("(3, 3, 3, 2, 2)")
        self.verticalLayout_24.addWidget(self.decoderLayersInput)
        self.horizontalLayout_8.addLayout(self.verticalLayout_24)
        self.verticalLayout_36.addLayout(self.horizontalLayout_8)
        self.verticalLayout_37.addLayout(self.verticalLayout_36)

        self.tabWidget.addTab(self.networkOverview, "")
        self.encoderLayer = QtWidgets.QWidget()
        self.encoderLayer.setObjectName("encoderLayer")
        self.verticalLayout_215 = QtWidgets.QVBoxLayout(self.encoderLayer)
        self.verticalLayout_215.setObjectName("verticalLayout_215")
        self.scrollArea = QtWidgets.QScrollArea(self.encoderLayer)
        self.scrollArea.setMinimumSize(QtCore.QSize(1200, 0))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1362, 1483))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_217 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_217.setObjectName("verticalLayout_217")
        self.verticalLayout_198 = QtWidgets.QVBoxLayout()
        self.verticalLayout_198.setObjectName("verticalLayout_198")
        self.verticalLayout_189 = QtWidgets.QVBoxLayout()
        self.verticalLayout_189.setObjectName("verticalLayout_189")
        self.verticalLayout_164 = QtWidgets.QVBoxLayout()
        self.verticalLayout_164.setObjectName("verticalLayout_164")
        self.verticalLayout_138 = QtWidgets.QVBoxLayout()
        self.verticalLayout_138.setObjectName("verticalLayout_138")
        self.verticalLayout_139 = QtWidgets.QVBoxLayout()
        self.verticalLayout_139.setObjectName("verticalLayout_139")



        self.encoderPicture = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.encoderPicture.setMinimumSize(QtCore.QSize(0, 100))
        self.encoderPicture.setAutoFillBackground(True)
        self.encoderPicture.setObjectName("encoderPicture")
        self.encoderPicture.setFixedHeight(900)
        self.verticalLayout_139.addWidget(self.encoderPicture)
        spacerItem66 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_139.addItem(spacerItem66)

        self.line_11 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout_139.addWidget(self.line_11)
        self.encoderDescription = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.encoderDescription.setMinimumSize(QtCore.QSize(0, 100))
        self.encoderDescription.setAutoFillBackground(True)
        self.encoderDescription.setObjectName("encoderDescription")
        self.verticalLayout_139.addWidget(self.encoderDescription)
        spacerItem67 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_139.addItem(spacerItem67)

        self.verticalLayout_138.addLayout(self.verticalLayout_139)
        spacerItem68 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_138.addItem(spacerItem68)

        self.line_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_138.addWidget(self.line_3)
        spacerItem69 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_138.addItem(spacerItem69)

        self.horizontalLayout_46 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_46.setObjectName("horizontalLayout_46")
        self.verticalLayout_140 = QtWidgets.QVBoxLayout()
        self.verticalLayout_140.setObjectName("verticalLayout_140")
        self.EL1topLbl_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL1topLbl_4.setObjectName("EL1topLbl_4")
        self.verticalLayout_140.addWidget(self.EL1topLbl_4)
        spacerItem70 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_140.addItem(spacerItem70)

        self.EL1convLevel_5 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.EL1convLevel_5.setObjectName("EL1convLevel_5")
        self.EL1convLevel_5.addItem("")
        self.EL1convLevel_5.addItem("")
        self.EL1convLevel_5.addItem("")
        self.EL1convLevel_5.addItem("")
        self.EL1convLevel_5.addItem("")
        self.EL1convLevel_5.setCurrentIndex(3)
        self.verticalLayout_140.addWidget(self.EL1convLevel_5)
        spacerItem71 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_140.addItem(spacerItem71)

        self.EL1activationFunc_5 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.EL1activationFunc_5.setObjectName("EL1activationFunc_5")
        self.EL1activationFunc_5.addItem("")
        self.EL1activationFunc_5.addItem("")
        self.EL1activationFunc_5.setCurrentIndex(1)
        self.verticalLayout_140.addWidget(self.EL1activationFunc_5)
        self.horizontalLayout_46.addLayout(self.verticalLayout_140)
        self.verticalLayout_141 = QtWidgets.QVBoxLayout()
        self.verticalLayout_141.setObjectName("verticalLayout_141")
        self.horizontalLayout_47 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_47.setObjectName("horizontalLayout_47")
        self.EL1numBlocks = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL1numBlocks.setObjectName("EL1numBlocks")
        self.horizontalLayout_47.addWidget(self.EL1numBlocks)
        spacerItem72 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_47.addItem(spacerItem72)

        self.EL1NumBlocks = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL1NumBlocks.setObjectName("EL1NumBlocks")
        self.EL1NumBlocks.setText("1")
        self.horizontalLayout_47.addWidget(self.EL1NumBlocks)
        spacerItem73 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_47.addItem(spacerItem73)

        self.verticalLayout_141.addLayout(self.horizontalLayout_47)
        spacerItem74 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_141.addItem(spacerItem74)

        self.horizontalLayout_48 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_48.setObjectName("horizontalLayout_48")
        self.verticalLayout_142 = QtWidgets.QVBoxLayout()
        self.verticalLayout_142.setObjectName("verticalLayout_142")
        self.EL1inputChannel = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL1inputChannel.setObjectName("EL1inputChannel")
        self.verticalLayout_142.addWidget(self.EL1inputChannel)
        spacerItem75 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_142.addItem(spacerItem75)

        self.EL1inputChannelErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL1inputChannelErr.setText("")
        self.EL1inputChannelErr.setObjectName("EL1inputChannelErr")
        self.EL1inputChannelErr.setStyleSheet('color: red')
        self.EL1inputChannelErr.setWordWrap(True)
        self.verticalLayout_142.addWidget(self.EL1inputChannelErr)
        spacerItem76 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_142.addItem(spacerItem76)

        self.EL1inputChannelInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL1inputChannelInput.setObjectName("EL1inputChannelInput")
        self.EL1inputChannelInput.setText("3")
        self.verticalLayout_142.addWidget(self.EL1inputChannelInput)
        self.horizontalLayout_48.addLayout(self.verticalLayout_142)
        spacerItem77 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_48.addItem(spacerItem77)

        self.verticalLayout_143 = QtWidgets.QVBoxLayout()
        self.verticalLayout_143.setObjectName("verticalLayout_143")
        self.EL1outputChannel = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL1outputChannel.setObjectName("EL1outputChannel")
        self.verticalLayout_143.addWidget(self.EL1outputChannel)
        spacerItem78 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_143.addItem(spacerItem78)

        self.EL1outputChannelErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL1outputChannelErr.setText("")
        self.EL1outputChannelErr.setObjectName("EL1outputChannelErr")
        self.EL1outputChannelErr.setStyleSheet('color: red')
        self.EL1outputChannelErr.setWordWrap(True)
        self.verticalLayout_143.addWidget(self.EL1outputChannelErr)
        spacerItem79 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_143.addItem(spacerItem79)

        self.EL1outputChannelInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL1outputChannelInput.setObjectName("EL1outputChannelInput")
        self.EL1outputChannelInput.setText("4")
        self.verticalLayout_143.addWidget(self.EL1outputChannelInput)
        self.horizontalLayout_48.addLayout(self.verticalLayout_143)
        spacerItem80 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_48.addItem(spacerItem80)

        self.verticalLayout_144 = QtWidgets.QVBoxLayout()
        self.verticalLayout_144.setObjectName("verticalLayout_144")
        self.EL1bias = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL1bias.setObjectName("EL1bias")
        self.verticalLayout_144.addWidget(self.EL1bias)
        spacerItem81 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_144.addItem(spacerItem81)

        self.EL1biasErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL1biasErr.setText("")
        self.EL1biasErr.setObjectName("EL1biasErr")
        self.EL1biasErr.setStyleSheet('color: red')
        self.EL1biasErr.setWordWrap(True)
        self.verticalLayout_144.addWidget(self.EL1biasErr)
        spacerItem82 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_144.addItem(spacerItem82)

        self.EL1biasInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL1biasInput.setObjectName("EL1biasInput")
        self.EL1biasInput.setText("True")
        self.verticalLayout_144.addWidget(self.EL1biasInput)
        self.horizontalLayout_48.addLayout(self.verticalLayout_144)
        spacerItem83 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_48.addItem(spacerItem83)

        self.verticalLayout_145 = QtWidgets.QVBoxLayout()
        self.verticalLayout_145.setObjectName("verticalLayout_145")
        self.EL1stride = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL1stride.setObjectName("EL1stride")
        self.verticalLayout_145.addWidget(self.EL1stride)
        spacerItem84 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_145.addItem(spacerItem84)

        self.EL1strideErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL1strideErr.setText("")
        self.EL1strideErr.setObjectName("EL1strideErr")
        self.EL1strideErr.setStyleSheet('color: red')
        self.EL1strideErr.setWordWrap(True)
        self.verticalLayout_145.addWidget(self.EL1strideErr)
        spacerItem85 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_145.addItem(spacerItem85)

        self.EL1strideInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL1strideInput.setObjectName("EL1strideInput")
        self.EL1strideInput.setText("1")
        self.verticalLayout_145.addWidget(self.EL1strideInput)
        self.horizontalLayout_48.addLayout(self.verticalLayout_145)
        spacerItem86 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_48.addItem(spacerItem86)

        self.verticalLayout_146 = QtWidgets.QVBoxLayout()
        self.verticalLayout_146.setObjectName("verticalLayout_146")
        self.EL1padding = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL1padding.setObjectName("EL1padding")
        self.verticalLayout_146.addWidget(self.EL1padding)
        spacerItem87 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_146.addItem(spacerItem87)

        self.EL1paddingErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL1paddingErr.setText("")
        self.EL1paddingErr.setObjectName("EL1paddingErr")
        self.EL1paddingErr.setStyleSheet('color: red')
        self.EL1paddingErr.setWordWrap(True)
        self.verticalLayout_146.addWidget(self.EL1paddingErr)
        spacerItem88 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_146.addItem(spacerItem88)

        self.EL1paddingInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL1paddingInput.setObjectName("EL1paddingInput")
        self.EL1paddingInput.setText("0")
        self.verticalLayout_146.addWidget(self.EL1paddingInput)
        self.horizontalLayout_48.addLayout(self.verticalLayout_146)
        spacerItem89 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_48.addItem(spacerItem89)

        self.verticalLayout_147 = QtWidgets.QVBoxLayout()
        self.verticalLayout_147.setObjectName("verticalLayout_147")
        self.EL1groups = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL1groups.setObjectName("EL1groups")
        self.verticalLayout_147.addWidget(self.EL1groups)
        spacerItem90 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_147.addItem(spacerItem90)

        self.EL1groupsErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL1groupsErr.setText("")
        self.EL1groupsErr.setObjectName("EL1groupsErr")
        self.EL1groupsErr.setStyleSheet('color: red')
        self.EL1groupsErr.setWordWrap(True)
        self.verticalLayout_147.addWidget(self.EL1groupsErr)
        spacerItem91 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_147.addItem(spacerItem91)

        self.EL1groupsInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL1groupsInput.setObjectName("EL1groupsInput")
        self.EL1groupsInput.setText("1")
        self.verticalLayout_147.addWidget(self.EL1groupsInput)
        self.horizontalLayout_48.addLayout(self.verticalLayout_147)
        self.verticalLayout_141.addLayout(self.horizontalLayout_48)
        self.horizontalLayout_46.addLayout(self.verticalLayout_141)
        self.verticalLayout_138.addLayout(self.horizontalLayout_46)
        self.verticalLayout_164.addLayout(self.verticalLayout_138)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_164.addWidget(self.line)
        spacerItem92 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_164.addItem(spacerItem92)

        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_164.addWidget(self.line_2)
        self.horizontalLayout_52 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_52.setObjectName("horizontalLayout_52")
        self.verticalLayout_156 = QtWidgets.QVBoxLayout()
        self.verticalLayout_156.setObjectName("verticalLayout_156")
        self.EL2topLbl = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL2topLbl.setObjectName("EL2topLbl")
        self.verticalLayout_156.addWidget(self.EL2topLbl)
        spacerItem93 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_156.addItem(spacerItem93)
        self.EL2convLevel = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.EL2convLevel.setObjectName("EL2convLevel")
        self.EL2convLevel.addItem("")
        self.EL2convLevel.addItem("")
        self.EL2convLevel.addItem("")
        self.EL2convLevel.addItem("")
        self.EL2convLevel.addItem("")
        self.EL2convLevel.setCurrentIndex(3)
        self.verticalLayout_156.addWidget(self.EL2convLevel)
        spacerItem94 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_156.addItem(spacerItem94)

        self.EL2activationFunc = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.EL2activationFunc.setObjectName("EL2activationFunc")
        self.EL2activationFunc.addItem("")
        self.EL2activationFunc.addItem("")
        self.EL2activationFunc.setCurrentIndex(1)
        self.verticalLayout_156.addWidget(self.EL2activationFunc)
        self.horizontalLayout_52.addLayout(self.verticalLayout_156)
        self.verticalLayout_157 = QtWidgets.QVBoxLayout()
        self.verticalLayout_157.setObjectName("verticalLayout_157")
        self.horizontalLayout_53 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_53.setObjectName("horizontalLayout_53")
        self.EL2numBlocks = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL2numBlocks.setObjectName("EL2numBlocks")
        self.horizontalLayout_53.addWidget(self.EL2numBlocks)
        spacerItem95 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_53.addItem(spacerItem95)

        self.EL2NumBlocks = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL2NumBlocks.setObjectName("EL2NumBlocks")
        self.EL2NumBlocks.setText("1")
        self.horizontalLayout_53.addWidget(self.EL2NumBlocks)
        spacerItem96 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_53.addItem(spacerItem96)
        self.verticalLayout_157.addLayout(self.horizontalLayout_53)
        spacerItem97 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_157.addItem(spacerItem97)

        self.horizontalLayout_54 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_54.setObjectName("horizontalLayout_54")
        self.verticalLayout_158 = QtWidgets.QVBoxLayout()
        self.verticalLayout_158.setObjectName("verticalLayout_158")
        self.EL2inputChannel = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL2inputChannel.setObjectName("EL2inputChannel")
        self.verticalLayout_158.addWidget(self.EL2inputChannel)
        spacerItem98 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_158.addItem(spacerItem98)

        self.EL2inputChannelErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL2inputChannelErr.setText("")
        self.EL2inputChannelErr.setObjectName("EL2inputChannelErr")
        self.EL2inputChannelErr.setStyleSheet('color: red')
        self.EL2inputChannelErr.setWordWrap(True)
        self.verticalLayout_158.addWidget(self.EL2inputChannelErr)
        spacerItem99 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_158.addItem(spacerItem99)

        self.EL2inputChannelInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL2inputChannelInput.setObjectName("EL2inputChannelInput")
        self.EL2inputChannelInput.setText("4")
        self.verticalLayout_158.addWidget(self.EL2inputChannelInput)
        self.horizontalLayout_54.addLayout(self.verticalLayout_158)
        spacerItem100 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_54.addItem(spacerItem100)

        self.verticalLayout_159 = QtWidgets.QVBoxLayout()
        self.verticalLayout_159.setObjectName("verticalLayout_159")
        self.EL2outputChannel = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL2outputChannel.setObjectName("EL2outputChannel")
        self.verticalLayout_159.addWidget(self.EL2outputChannel)
        spacerItem101 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_159.addItem(spacerItem101)

        self.EL2outputChannelErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL2outputChannelErr.setText("")
        self.EL2outputChannelErr.setObjectName("EL2outputChannelErr")
        self.EL2outputChannelErr.setStyleSheet('color: red')
        self.EL2outputChannelErr.setWordWrap(True)
        self.verticalLayout_159.addWidget(self.EL2outputChannelErr)
        spacerItem102 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_159.addItem(spacerItem102)

        self.EL2outputChannelInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL2outputChannelInput.setObjectName("EL2outputChannelInput")
        self.EL2outputChannelInput.setText("8")
        self.verticalLayout_159.addWidget(self.EL2outputChannelInput)
        self.horizontalLayout_54.addLayout(self.verticalLayout_159)
        spacerItem103 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_54.addItem(spacerItem103)

        self.verticalLayout_160 = QtWidgets.QVBoxLayout()
        self.verticalLayout_160.setObjectName("verticalLayout_160")
        self.EL2bias = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL2bias.setObjectName("EL2bias")
        self.verticalLayout_160.addWidget(self.EL2bias)
        spacerItem104 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_160.addItem(spacerItem104)

        self.EL2biasErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL2biasErr.setText("")
        self.EL2biasErr.setObjectName("EL2biasErr")
        self.EL2biasErr.setStyleSheet('color: red')
        self.EL2biasErr.setWordWrap(True)
        self.verticalLayout_160.addWidget(self.EL2biasErr)
        spacerItem105 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_160.addItem(spacerItem105)

        self.EL2biasInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL2biasInput.setObjectName("EL2biasInput")
        self.EL2biasInput.setText("True")
        self.verticalLayout_160.addWidget(self.EL2biasInput)
        self.horizontalLayout_54.addLayout(self.verticalLayout_160)
        spacerItem106 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_54.addItem(spacerItem106)

        self.verticalLayout_161 = QtWidgets.QVBoxLayout()
        self.verticalLayout_161.setObjectName("verticalLayout_161")
        self.EL2stride = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL2stride.setObjectName("EL2stride")
        self.verticalLayout_161.addWidget(self.EL2stride)
        spacerItem107 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_161.addItem(spacerItem107)

        self.EL2strideErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL2strideErr.setText("")
        self.EL2strideErr.setObjectName("EL2strideErr")
        self.EL2strideErr.setStyleSheet('color: red')
        self.EL2strideErr.setWordWrap(True)
        self.verticalLayout_161.addWidget(self.EL2strideErr)
        spacerItem108 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_161.addItem(spacerItem108)

        self.EL2strideInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL2strideInput.setObjectName("EL2strideInput")
        self.EL2strideInput.setText("1")
        self.verticalLayout_161.addWidget(self.EL2strideInput)
        self.horizontalLayout_54.addLayout(self.verticalLayout_161)
        spacerItem109 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_54.addItem(spacerItem109)

        self.verticalLayout_162 = QtWidgets.QVBoxLayout()
        self.verticalLayout_162.setObjectName("verticalLayout_162")
        self.EL2padding = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL2padding.setObjectName("EL2padding")
        self.verticalLayout_162.addWidget(self.EL2padding)
        spacerItem110 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_162.addItem(spacerItem110)

        self.EL2paddingErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL2paddingErr.setText("")
        self.EL2paddingErr.setObjectName("EL2paddingErr")
        self.EL2paddingErr.setStyleSheet('color: red')
        self.EL2paddingErr.setWordWrap(True)
        self.verticalLayout_162.addWidget(self.EL2paddingErr)
        spacerItem111 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_162.addItem(spacerItem111)

        self.EL2paddingInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL2paddingInput.setObjectName("EL2paddingInput")
        self.EL2paddingInput.setText("0")
        self.verticalLayout_162.addWidget(self.EL2paddingInput)
        self.horizontalLayout_54.addLayout(self.verticalLayout_162)
        spacerItem112 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_54.addItem(spacerItem112)

        self.verticalLayout_163 = QtWidgets.QVBoxLayout()
        self.verticalLayout_163.setObjectName("verticalLayout_163")
        self.EL2groups = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL2groups.setObjectName("EL2groups")
        self.verticalLayout_163.addWidget(self.EL2groups)
        spacerItem113 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_163.addItem(spacerItem113)

        self.EL2groupsErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL2groupsErr.setText("")
        self.EL2groupsErr.setObjectName("EL2groupsErr")
        self.EL2groupsErr.setStyleSheet('color: red')
        self.EL2groupsErr.setWordWrap(True)
        self.verticalLayout_163.addWidget(self.EL2groupsErr)
        spacerItem114 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_163.addItem(spacerItem114)
        self.EL2groupsInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL2groupsInput.setObjectName("EL2groupsInput")
        self.EL2groupsInput.setText("1")

        self.verticalLayout_163.addWidget(self.EL2groupsInput)
        self.horizontalLayout_54.addLayout(self.verticalLayout_163)
        self.verticalLayout_157.addLayout(self.horizontalLayout_54)
        self.horizontalLayout_52.addLayout(self.verticalLayout_157)
        self.verticalLayout_164.addLayout(self.horizontalLayout_52)
        self.verticalLayout_189.addLayout(self.verticalLayout_164)
        self.line_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_189.addWidget(self.line_5)
        spacerItem115 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_189.addItem(spacerItem115)

        self.line_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_189.addWidget(self.line_6)
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.verticalLayout_165 = QtWidgets.QVBoxLayout()
        self.verticalLayout_165.setObjectName("verticalLayout_165")
        self.EL3topLbl = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL3topLbl.setObjectName("EL3topLbl")
        self.verticalLayout_165.addWidget(self.EL3topLbl)
        spacerItem116 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_165.addItem(spacerItem116)
        self.EL3convLevel = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.EL3convLevel.setObjectName("EL3convLevel")
        self.EL3convLevel.addItem("")
        self.EL3convLevel.addItem("")
        self.EL3convLevel.addItem("")
        self.EL3convLevel.addItem("")
        self.EL3convLevel.addItem("")
        self.EL3convLevel.setCurrentIndex(3)
        self.verticalLayout_165.addWidget(self.EL3convLevel)
        spacerItem117 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_165.addItem(spacerItem117)

        self.EL3activationFunc = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.EL3activationFunc.setObjectName("EL3activationFunc")
        self.EL3activationFunc.addItem("")
        self.EL3activationFunc.addItem("")
        self.EL3activationFunc.setCurrentIndex(1)
        self.verticalLayout_165.addWidget(self.EL3activationFunc)
        self.horizontalLayout_55.addLayout(self.verticalLayout_165)
        self.verticalLayout_166 = QtWidgets.QVBoxLayout()
        self.verticalLayout_166.setObjectName("verticalLayout_166")
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.EL3numBlocks = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL3numBlocks.setObjectName("EL3numBlocks")
        self.horizontalLayout_56.addWidget(self.EL3numBlocks)
        spacerItem118 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_56.addItem(spacerItem118)
        self.EL3NumBlocks = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL3NumBlocks.setObjectName("EL3NumBlocks")
        self.EL3NumBlocks.setText("1")
        self.horizontalLayout_56.addWidget(self.EL3NumBlocks)
        spacerItem119 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_56.addItem(spacerItem119)
        self.verticalLayout_166.addLayout(self.horizontalLayout_56)
        spacerItem120 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_166.addItem(spacerItem120)

        self.horizontalLayout_57 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_57.setObjectName("horizontalLayout_57")
        self.verticalLayout_167 = QtWidgets.QVBoxLayout()
        self.verticalLayout_167.setObjectName("verticalLayout_167")
        self.EL3inputChannel = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL3inputChannel.setObjectName("EL3inputChannel")
        self.verticalLayout_167.addWidget(self.EL3inputChannel)
        spacerItem121 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_167.addItem(spacerItem121)
        self.EL3inputChannelErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL3inputChannelErr.setText("")
        self.EL3inputChannelErr.setObjectName("EL3inputChannelErr")
        self.EL3inputChannelErr.setStyleSheet('color: red')
        self.EL3inputChannelErr.setWordWrap(True)
        self.verticalLayout_167.addWidget(self.EL3inputChannelErr)
        spacerItem122 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_167.addItem(spacerItem122)
        self.EL3inputChannelInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL3inputChannelInput.setObjectName("EL3inputChannelInput")
        self.EL3inputChannelInput.setText("8")
        self.verticalLayout_167.addWidget(self.EL3inputChannelInput)
        self.horizontalLayout_57.addLayout(self.verticalLayout_167)
        spacerItem123 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_57.addItem(spacerItem123)

        self.verticalLayout_168 = QtWidgets.QVBoxLayout()
        self.verticalLayout_168.setObjectName("verticalLayout_168")
        self.EL3outputChannel = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL3outputChannel.setObjectName("EL3outputChannel")
        self.verticalLayout_168.addWidget(self.EL3outputChannel)
        spacerItem124 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_168.addItem(spacerItem124)
        self.EL3outputChannelErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL3outputChannelErr.setText("")
        self.EL3outputChannelErr.setObjectName("EL3outputChannelErr")
        self.EL3outputChannelErr.setStyleSheet('color: red')
        self.EL3outputChannelErr.setWordWrap(True)
        self.verticalLayout_168.addWidget(self.EL3outputChannelErr)
        spacerItem125 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_168.addItem(spacerItem125)
        self.EL3outputChannelInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL3outputChannelInput.setObjectName("EL3outputChannelInput")
        self.EL3outputChannelInput.setText("16")
        self.verticalLayout_168.addWidget(self.EL3outputChannelInput)
        self.horizontalLayout_57.addLayout(self.verticalLayout_168)
        spacerItem126 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_57.addItem(spacerItem126)

        self.verticalLayout_169 = QtWidgets.QVBoxLayout()
        self.verticalLayout_169.setObjectName("verticalLayout_169")
        self.EL3bias = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL3bias.setObjectName("EL3bias")
        self.verticalLayout_169.addWidget(self.EL3bias)
        spacerItem127 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_169.addItem(spacerItem127)
        self.EL3biasErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL3biasErr.setText("")
        self.EL3biasErr.setObjectName("EL3biasErr")
        self.EL3biasErr.setStyleSheet('color: red')
        self.EL3biasErr.setWordWrap(True)
        self.verticalLayout_169.addWidget(self.EL3biasErr)
        spacerItem128 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_169.addItem(spacerItem128)
        self.EL3biasInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL3biasInput.setObjectName("EL3biasInput")
        self.EL3biasInput.setText("True")
        self.verticalLayout_169.addWidget(self.EL3biasInput)
        self.horizontalLayout_57.addLayout(self.verticalLayout_169)
        spacerItem129 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_57.addItem(spacerItem129)

        self.verticalLayout_170 = QtWidgets.QVBoxLayout()
        self.verticalLayout_170.setObjectName("verticalLayout_170")
        self.EL3stride = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL3stride.setObjectName("EL3stride")
        self.verticalLayout_170.addWidget(self.EL3stride)
        spacerItem130 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_170.addItem(spacerItem130)
        self.EL3strideErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL3strideErr.setText("")
        self.EL3strideErr.setObjectName("EL3strideErr")
        self.EL3strideErr.setStyleSheet('color: red')
        self.EL3strideErr.setWordWrap(True)
        self.verticalLayout_170.addWidget(self.EL3strideErr)
        spacerItem131 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_170.addItem(spacerItem131)
        self.EL3strideInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL3strideInput.setObjectName("EL3strideInput")
        self.EL3strideInput.setText("1")
        self.verticalLayout_170.addWidget(self.EL3strideInput)
        self.horizontalLayout_57.addLayout(self.verticalLayout_170)
        spacerItem132 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_57.addItem(spacerItem132)

        self.verticalLayout_171 = QtWidgets.QVBoxLayout()
        self.verticalLayout_171.setObjectName("verticalLayout_171")
        self.EL3padding = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL3padding.setObjectName("EL3padding")
        self.verticalLayout_171.addWidget(self.EL3padding)
        spacerItem133 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_171.addItem(spacerItem133)
        self.EL3paddingErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL3paddingErr.setText("")
        self.EL3paddingErr.setObjectName("EL3paddingErr")
        self.EL3paddingErr.setStyleSheet('color: red')
        self.EL3paddingErr.setWordWrap(True)
        self.verticalLayout_171.addWidget(self.EL3paddingErr)
        spacerItem134 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_171.addItem(spacerItem134)
        self.EL3paddingInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL3paddingInput.setObjectName("EL3paddingInput")
        self.EL3paddingInput.setText("0")
        self.verticalLayout_171.addWidget(self.EL3paddingInput)
        self.horizontalLayout_57.addLayout(self.verticalLayout_171)
        spacerItem135 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_57.addItem(spacerItem135)

        self.verticalLayout_188 = QtWidgets.QVBoxLayout()
        self.verticalLayout_188.setObjectName("verticalLayout_188")
        self.EL3groups = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL3groups.setObjectName("EL3groups")
        self.verticalLayout_188.addWidget(self.EL3groups)
        spacerItem136 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_188.addItem(spacerItem136)
        self.EL3groupsErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL3groupsErr.setText("")
        self.EL3groupsErr.setObjectName("EL3groupsErr")
        self.EL3groupsErr.setStyleSheet('color: red')
        self.EL3groupsErr.setWordWrap(True)
        self.verticalLayout_188.addWidget(self.EL3groupsErr)
        spacerItem137 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_188.addItem(spacerItem137)
        self.EL3groupsInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL3groupsInput.setObjectName("EL3groupsInput")
        self.EL3groupsInput.setText("1")
        self.verticalLayout_188.addWidget(self.EL3groupsInput)
        self.horizontalLayout_57.addLayout(self.verticalLayout_188)
        self.verticalLayout_166.addLayout(self.horizontalLayout_57)
        self.horizontalLayout_55.addLayout(self.verticalLayout_166)
        self.verticalLayout_189.addLayout(self.horizontalLayout_55)
        self.line_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_189.addWidget(self.line_7)
        self.verticalLayout_198.addLayout(self.verticalLayout_189)
        spacerItem138 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_198.addItem(spacerItem138)


        self.line_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_198.addWidget(self.line_8)
        self.horizontalLayout_64 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_64.setObjectName("horizontalLayout_64")
        self.verticalLayout_190 = QtWidgets.QVBoxLayout()
        self.verticalLayout_190.setObjectName("verticalLayout_190")
        self.EL4topLbl = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL4topLbl.setObjectName("EL4topLbl")
        self.verticalLayout_190.addWidget(self.EL4topLbl)
        spacerItem139 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_190.addItem(spacerItem139)
        self.EL4convLevel = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.EL4convLevel.setObjectName("EL4convLevel")
        self.EL4convLevel.addItem("")
        self.EL4convLevel.addItem("")
        self.EL4convLevel.addItem("")
        self.EL4convLevel.addItem("")
        self.EL4convLevel.addItem("")
        self.EL4convLevel.setCurrentIndex(3)
        self.verticalLayout_190.addWidget(self.EL4convLevel)
        spacerItem140 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_190.addItem(spacerItem140)


        self.EL4activationFunc = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.EL4activationFunc.setObjectName("EL4activationFunc")
        self.EL4activationFunc.addItem("")
        self.EL4activationFunc.addItem("")
        self.EL4activationFunc.setCurrentIndex(1)
        self.verticalLayout_190.addWidget(self.EL4activationFunc)
        self.horizontalLayout_64.addLayout(self.verticalLayout_190)
        self.verticalLayout_191 = QtWidgets.QVBoxLayout()
        self.verticalLayout_191.setObjectName("verticalLayout_191")
        self.horizontalLayout_65 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_65.setObjectName("horizontalLayout_65")
        self.EL4numBlocks = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL4numBlocks.setObjectName("EL4numBlocks")
        self.horizontalLayout_65.addWidget(self.EL4numBlocks)
        spacerItem141 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_65.addItem(spacerItem141)
        self.EL4NumBlocks = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL4NumBlocks.setObjectName("EL4NumBlocks")
        self.EL4NumBlocks.setText("1")
        self.horizontalLayout_65.addWidget(self.EL4NumBlocks)
        spacerItem142 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_65.addItem(spacerItem142)
        self.verticalLayout_191.addLayout(self.horizontalLayout_65)
        spacerItem143 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_191.addItem(spacerItem143)


        self.horizontalLayout_66 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_66.setObjectName("horizontalLayout_66")
        self.verticalLayout_192 = QtWidgets.QVBoxLayout()
        self.verticalLayout_192.setObjectName("verticalLayout_192")
        self.EL4inputChannel = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL4inputChannel.setObjectName("EL4inputChannel")
        self.verticalLayout_192.addWidget(self.EL4inputChannel)
        spacerItem144 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_192.addItem(spacerItem144)
        self.EL4inputChannelErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL4inputChannelErr.setText("")
        self.EL4inputChannelErr.setObjectName("EL4inputChannelErr")
        self.EL4inputChannelErr.setStyleSheet('color: red')
        self.EL4inputChannelErr.setWordWrap(True)
        self.verticalLayout_192.addWidget(self.EL4inputChannelErr)
        spacerItem145 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_192.addItem(spacerItem145)
        self.EL4inputChannelInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL4inputChannelInput.setObjectName("EL4inputChannelInput")
        self.EL4inputChannelInput.setText("16")
        self.verticalLayout_192.addWidget(self.EL4inputChannelInput)
        self.horizontalLayout_66.addLayout(self.verticalLayout_192)
        spacerItem146 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_66.addItem(spacerItem146)

        self.verticalLayout_193 = QtWidgets.QVBoxLayout()
        self.verticalLayout_193.setObjectName("verticalLayout_193")
        self.EL4outputChannel = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL4outputChannel.setObjectName("EL4outputChannel")
        self.verticalLayout_193.addWidget(self.EL4outputChannel)
        spacerItem147 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_193.addItem(spacerItem147)
        self.EL4outputChannelErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL4outputChannelErr.setText("")
        self.EL4outputChannelErr.setObjectName("EL4outputChannelErr")
        self.EL4outputChannelErr.setStyleSheet('color: red')
        self.EL4outputChannelErr.setWordWrap(True)
        self.verticalLayout_193.addWidget(self.EL4outputChannelErr)
        spacerItem148 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_193.addItem(spacerItem148)
        self.EL4outputChannelInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL4outputChannelInput.setObjectName("EL4outputChannelInput")
        self.EL4outputChannelInput.setText("32")
        self.verticalLayout_193.addWidget(self.EL4outputChannelInput)
        self.horizontalLayout_66.addLayout(self.verticalLayout_193)
        spacerItem149 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_66.addItem(spacerItem149)


        self.verticalLayout_194 = QtWidgets.QVBoxLayout()
        self.verticalLayout_194.setObjectName("verticalLayout_194")
        self.EL4bias = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL4bias.setObjectName("EL4bias")
        self.verticalLayout_194.addWidget(self.EL4bias)
        spacerItem150 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_194.addItem(spacerItem150)
        self.EL4biasErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL4biasErr.setText("")
        self.EL4biasErr.setObjectName("EL4biasErr")
        self.EL4biasErr.setStyleSheet('color: red')
        self.EL4biasErr.setWordWrap(True)
        self.verticalLayout_194.addWidget(self.EL4biasErr)
        spacerItem151 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_194.addItem(spacerItem151)
        self.EL4biasInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL4biasInput.setObjectName("EL4biasInput")
        self.EL4biasInput.setText("True")
        self.verticalLayout_194.addWidget(self.EL4biasInput)
        self.horizontalLayout_66.addLayout(self.verticalLayout_194)
        spacerItem152 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_66.addItem(spacerItem152)


        self.verticalLayout_195 = QtWidgets.QVBoxLayout()
        self.verticalLayout_195.setObjectName("verticalLayout_195")
        self.EL4stride = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL4stride.setObjectName("EL4stride")
        self.verticalLayout_195.addWidget(self.EL4stride)
        spacerItem153 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_195.addItem(spacerItem153)
        self.EL4strideErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL4strideErr.setText("")
        self.EL4strideErr.setObjectName("EL4strideErr")
        self.EL4strideErr.setStyleSheet('color: red')
        self.EL4strideErr.setWordWrap(True)
        self.verticalLayout_195.addWidget(self.EL4strideErr)
        spacerItem154 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_195.addItem(spacerItem154)
        self.EL4strideInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL4strideInput.setObjectName("EL4strideInput")
        self.EL4strideInput.setText("1")
        self.verticalLayout_195.addWidget(self.EL4strideInput)
        self.horizontalLayout_66.addLayout(self.verticalLayout_195)
        spacerItem155 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_66.addItem(spacerItem155)


        self.verticalLayout_196 = QtWidgets.QVBoxLayout()
        self.verticalLayout_196.setObjectName("verticalLayout_196")
        self.EL4padding = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL4padding.setObjectName("EL4padding")
        self.verticalLayout_196.addWidget(self.EL4padding)
        spacerItem156 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_196.addItem(spacerItem156)
        self.EL4paddingErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL4paddingErr.setText("")
        self.EL4paddingErr.setObjectName("EL4paddingErr")
        self.EL4paddingErr.setStyleSheet('color: red')
        self.EL4paddingErr.setWordWrap(True)
        self.verticalLayout_196.addWidget(self.EL4paddingErr)
        spacerItem157 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_196.addItem(spacerItem157)
        self.EL4paddingInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL4paddingInput.setObjectName("EL4paddingInput")
        self.EL4paddingInput.setText("0")
        self.verticalLayout_196.addWidget(self.EL4paddingInput)
        self.horizontalLayout_66.addLayout(self.verticalLayout_196)
        spacerItem158 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_66.addItem(spacerItem158)


        self.verticalLayout_197 = QtWidgets.QVBoxLayout()
        self.verticalLayout_197.setObjectName("verticalLayout_197")
        self.EL4groups = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL4groups.setObjectName("EL4groups")
        self.verticalLayout_197.addWidget(self.EL4groups)
        spacerItem159 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_197.addItem(spacerItem159)
        self.EL4groupsErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL4groupsErr.setText("")
        self.EL4groupsErr.setObjectName("EL4groupsErr")
        self.EL4groupsErr.setStyleSheet('color: red')
        self.EL4groupsErr.setWordWrap(True)
        self.verticalLayout_197.addWidget(self.EL4groupsErr)
        spacerItem160 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_197.addItem(spacerItem160)
        self.EL4groupsInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL4groupsInput.setObjectName("EL4groupsInput")
        self.EL4groupsInput.setText("1")
        self.verticalLayout_197.addWidget(self.EL4groupsInput)
        self.horizontalLayout_66.addLayout(self.verticalLayout_197)
        self.verticalLayout_191.addLayout(self.horizontalLayout_66)
        self.horizontalLayout_64.addLayout(self.verticalLayout_191)
        self.verticalLayout_198.addLayout(self.horizontalLayout_64)
        self.verticalLayout_217.addLayout(self.verticalLayout_198)
        self.line_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_217.addWidget(self.line_9)
        spacerItem161 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_217.addItem(spacerItem161)
        self.line_10 = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.verticalLayout_217.addWidget(self.line_10)
        self.horizontalLayout_70 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_70.setObjectName("horizontalLayout_70")
        self.verticalLayout_199 = QtWidgets.QVBoxLayout()
        self.verticalLayout_199.setObjectName("verticalLayout_199")
        self.EL5topLbl = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL5topLbl.setObjectName("EL5topLbl")
        self.verticalLayout_199.addWidget(self.EL5topLbl)
        spacerItem162 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_199.addItem(spacerItem162)


        self.EL5convLevel = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.EL5convLevel.setObjectName("EL5convLevel")
        self.EL5convLevel.addItem("")
        self.EL5convLevel.addItem("")
        self.EL5convLevel.addItem("")
        self.EL5convLevel.addItem("")
        self.EL5convLevel.addItem("")
        self.EL5convLevel.setCurrentIndex(3)
        self.verticalLayout_199.addWidget(self.EL5convLevel)
        spacerItem163 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_199.addItem(spacerItem163)
        self.EL5activationFunc = QtWidgets.QComboBox(self.scrollAreaWidgetContents_3)
        self.EL5activationFunc.setObjectName("EL5activationFunc")
        self.EL5activationFunc.addItem("")
        self.EL5activationFunc.addItem("")
        self.EL5activationFunc.setCurrentIndex(1)
        self.verticalLayout_199.addWidget(self.EL5activationFunc)
        self.horizontalLayout_70.addLayout(self.verticalLayout_199)
        self.verticalLayout_208 = QtWidgets.QVBoxLayout()
        self.verticalLayout_208.setObjectName("verticalLayout_208")
        self.horizontalLayout_71 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_71.setObjectName("horizontalLayout_71")
        self.EL5numBlocks = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL5numBlocks.setObjectName("EL5numBlocks")
        self.horizontalLayout_71.addWidget(self.EL5numBlocks)
        spacerItem164 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_71.addItem(spacerItem164)
        self.EL5NumBlocks = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL5NumBlocks.setObjectName("EL5NumBlocks")
        self.EL5NumBlocks.setText("1")
        self.horizontalLayout_71.addWidget(self.EL5NumBlocks)
        spacerItem165 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_71.addItem(spacerItem165)
        self.verticalLayout_208.addLayout(self.horizontalLayout_71)
        spacerItem166 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_208.addItem(spacerItem166)


        self.horizontalLayout_72 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_72.setObjectName("horizontalLayout_72")
        self.verticalLayout_209 = QtWidgets.QVBoxLayout()
        self.verticalLayout_209.setObjectName("verticalLayout_209")
        self.EL5inputChannel = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL5inputChannel.setObjectName("EL5inputChannel")
        self.verticalLayout_209.addWidget(self.EL5inputChannel)
        spacerItem167 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_209.addItem(spacerItem167)
        self.EL5inputChannelErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL5inputChannelErr.setText("")
        self.EL5inputChannelErr.setObjectName("EL5inputChannelErr")
        self.EL5inputChannelErr.setStyleSheet('color: red')
        self.EL5inputChannelErr.setWordWrap(True)
        self.verticalLayout_209.addWidget(self.EL5inputChannelErr)
        spacerItem168 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_209.addItem(spacerItem168)
        self.EL5inputChannelInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL5inputChannelInput.setObjectName("EL5inputChannelInput")
        self.EL5inputChannelInput.setText("32")
        self.verticalLayout_209.addWidget(self.EL5inputChannelInput)
        self.horizontalLayout_72.addLayout(self.verticalLayout_209)
        spacerItem169 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_72.addItem(spacerItem169)


        self.verticalLayout_210 = QtWidgets.QVBoxLayout()
        self.verticalLayout_210.setObjectName("verticalLayout_210")
        self.EL5outputChannel = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL5outputChannel.setObjectName("EL5outputChannel")
        self.verticalLayout_210.addWidget(self.EL5outputChannel)
        spacerItem170 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_210.addItem(spacerItem170)
        self.EL5outputChannelErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL5outputChannelErr.setText("")
        self.EL5outputChannelErr.setObjectName("EL5outputChannelErr")
        self.EL5outputChannelErr.setStyleSheet('color: red')
        self.EL5outputChannelErr.setWordWrap(True)
        self.verticalLayout_210.addWidget(self.EL5outputChannelErr)
        spacerItem171 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_210.addItem(spacerItem171)
        self.EL5outputChannelInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL5outputChannelInput.setObjectName("EL5outputChannelInput")
        self.EL5outputChannelInput.setText("64")
        self.verticalLayout_210.addWidget(self.EL5outputChannelInput)
        self.horizontalLayout_72.addLayout(self.verticalLayout_210)
        spacerItem172 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_72.addItem(spacerItem172)


        self.verticalLayout_211 = QtWidgets.QVBoxLayout()
        self.verticalLayout_211.setObjectName("verticalLayout_211")
        self.EL5bias = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL5bias.setObjectName("EL5bias")
        self.verticalLayout_211.addWidget(self.EL5bias)
        spacerItem173 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_211.addItem(spacerItem173)
        self.EL5biasErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL5biasErr.setText("")
        self.EL5biasErr.setObjectName("EL5biasErr")
        self.EL5biasErr.setStyleSheet('color: red')
        self.EL5biasErr.setWordWrap(True)
        self.verticalLayout_211.addWidget(self.EL5biasErr)
        spacerItem174 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_211.addItem(spacerItem174)
        self.EL5biasInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL5biasInput.setObjectName("EL5biasInput")
        self.EL5biasInput.setText("True")
        self.verticalLayout_211.addWidget(self.EL5biasInput)
        self.horizontalLayout_72.addLayout(self.verticalLayout_211)
        spacerItem175 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_72.addItem(spacerItem175)


        self.verticalLayout_212 = QtWidgets.QVBoxLayout()
        self.verticalLayout_212.setObjectName("verticalLayout_212")
        self.EL5stride = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL5stride.setObjectName("EL5stride")
        self.verticalLayout_212.addWidget(self.EL5stride)
        spacerItem176 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_212.addItem(spacerItem176)
        self.EL5strideErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL5strideErr.setText("")
        self.EL5strideErr.setObjectName("EL5strideErr")
        self.EL5strideErr.setStyleSheet('color: red')
        self.EL5strideErr.setWordWrap(True)
        self.verticalLayout_212.addWidget(self.EL5strideErr)
        spacerItem177 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_212.addItem(spacerItem177)
        self.EL5strideInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL5strideInput.setObjectName("EL5strideInput")
        self.EL5strideInput.setText("1")
        self.verticalLayout_212.addWidget(self.EL5strideInput)
        self.horizontalLayout_72.addLayout(self.verticalLayout_212)
        spacerItem178 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_72.addItem(spacerItem178)


        self.verticalLayout_213 = QtWidgets.QVBoxLayout()
        self.verticalLayout_213.setObjectName("verticalLayout_213")
        self.EL5padding = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL5padding.setObjectName("EL5padding")
        self.verticalLayout_213.addWidget(self.EL5padding)
        spacerItem179 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_213.addItem(spacerItem179)
        self.EL5paddingErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL5paddingErr.setText("")
        self.EL5paddingErr.setObjectName("EL5paddingErr")
        self.EL5paddingErr.setStyleSheet('color: red')
        self.EL5paddingErr.setWordWrap(True)
        self.verticalLayout_213.addWidget(self.EL5paddingErr)
        spacerItem180 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_213.addItem(spacerItem180)
        self.EL5paddingInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL5paddingInput.setObjectName("EL5paddingInput")
        self.EL5paddingInput.setText("0")
        self.verticalLayout_213.addWidget(self.EL5paddingInput)
        self.horizontalLayout_72.addLayout(self.verticalLayout_213)
        spacerItem181 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_72.addItem(spacerItem181)


        self.verticalLayout_214 = QtWidgets.QVBoxLayout()
        self.verticalLayout_214.setObjectName("verticalLayout_214")
        self.EL5groups = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL5groups.setObjectName("EL5groups")
        self.verticalLayout_214.addWidget(self.EL5groups)
        spacerItem182 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_214.addItem(spacerItem182)
        self.EL5groupsErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.EL5groupsErr.setText("")
        self.EL5groupsErr.setObjectName("EL5groupsErr")
        self.EL5groupsErr.setStyleSheet('color: red')
        self.EL5groupsErr.setWordWrap(True)
        self.verticalLayout_214.addWidget(self.EL5groupsErr)
        spacerItem183 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_214.addItem(spacerItem183)
        self.EL5groupsInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_3)
        self.EL5groupsInput.setObjectName("EL5groupsInput")
        self.EL5groupsInput.setText("1")
        self.verticalLayout_214.addWidget(self.EL5groupsInput)


        self.horizontalLayout_72.addLayout(self.verticalLayout_214)
        self.verticalLayout_208.addLayout(self.horizontalLayout_72)
        self.horizontalLayout_70.addLayout(self.verticalLayout_208)
        self.verticalLayout_217.addLayout(self.horizontalLayout_70)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_215.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.encoderLayer, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_264 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_264.setObjectName("verticalLayout_264")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab)
        self.scrollArea_2.setMinimumSize(QtCore.QSize(1200, 0))
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 1362, 1480))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_218 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_218.setObjectName("verticalLayout_218")
        self.verticalLayout_219 = QtWidgets.QVBoxLayout()
        self.verticalLayout_219.setObjectName("verticalLayout_219")
        self.verticalLayout_220 = QtWidgets.QVBoxLayout()
        self.verticalLayout_220.setObjectName("verticalLayout_220")
        self.verticalLayout_221 = QtWidgets.QVBoxLayout()
        self.verticalLayout_221.setObjectName("verticalLayout_221")
        self.verticalLayout_222 = QtWidgets.QVBoxLayout()
        self.verticalLayout_222.setObjectName("verticalLayout_222")
        self.verticalLayout_223 = QtWidgets.QVBoxLayout()
        self.verticalLayout_223.setObjectName("verticalLayout_223")


        self.DecoderPicture = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DecoderPicture.setFixedHeight(800)
        self.DecoderPicture.setAutoFillBackground(True)
        self.DecoderPicture.setObjectName("DecoderPicture")
        self.verticalLayout_223.addWidget(self.DecoderPicture)
        spacerItem184 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_223.addItem(spacerItem184)
        self.line_12 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout_223.addWidget(self.line_12)


        self.decoderDescription = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.decoderDescription.setMinimumSize(QtCore.QSize(0, 100))
        self.decoderDescription.setAutoFillBackground(True)
        self.decoderDescription.setObjectName("decoderDescription")
        self.verticalLayout_223.addWidget(self.decoderDescription)
        spacerItem185 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_223.addItem(spacerItem185)
        self.verticalLayout_222.addLayout(self.verticalLayout_223)
        spacerItem186 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_222.addItem(spacerItem186)
        self.line_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_222.addWidget(self.line_4)
        spacerItem187 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_222.addItem(spacerItem187)


        self.horizontalLayout_74 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_74.setObjectName("horizontalLayout_74")
        self.verticalLayout_224 = QtWidgets.QVBoxLayout()
        self.verticalLayout_224.setObjectName("verticalLayout_224")
        self.DL1topLbl = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL1topLbl.setObjectName("DL1topLbl")
        self.verticalLayout_224.addWidget(self.DL1topLbl)
        spacerItem188 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_224.addItem(spacerItem188)
        self.EDL1convLevel = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        self.EDL1convLevel.setObjectName("EDL1convLevel")
        self.EDL1convLevel.addItem("")
        self.EDL1convLevel.addItem("")
        self.EDL1convLevel.addItem("")
        self.EDL1convLevel.addItem("")
        self.EDL1convLevel.addItem("")
        self.EDL1convLevel.setCurrentIndex(3)
        self.verticalLayout_224.addWidget(self.EDL1convLevel)
        spacerItem189 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_224.addItem(spacerItem189)
        self.DL1activationFunc = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        self.DL1activationFunc.setObjectName("DL1activationFunc")
        self.DL1activationFunc.addItem("")
        self.DL1activationFunc.addItem("")
        self.DL1activationFunc.setCurrentIndex(1)
        self.verticalLayout_224.addWidget(self.DL1activationFunc)
        self.horizontalLayout_74.addLayout(self.verticalLayout_224)
        self.verticalLayout_225 = QtWidgets.QVBoxLayout()
        self.verticalLayout_225.setObjectName("verticalLayout_225")
        self.horizontalLayout_75 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_75.setObjectName("horizontalLayout_75")
        self.DL1numBlocks = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL1numBlocks.setObjectName("DL1numBlocks")
        self.horizontalLayout_75.addWidget(self.DL1numBlocks)
        spacerItem190 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_75.addItem(spacerItem190)
        self.DL1NumBlocks = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL1NumBlocks.setObjectName("DL1NumBlocks")
        self.DL1NumBlocks.setText("2")
        self.horizontalLayout_75.addWidget(self.DL1NumBlocks)
        spacerItem191 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_75.addItem(spacerItem191)
        self.verticalLayout_225.addLayout(self.horizontalLayout_75)
        spacerItem192 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_225.addItem(spacerItem192)


        self.horizontalLayout_76 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_76.setObjectName("horizontalLayout_76")
        self.verticalLayout_226 = QtWidgets.QVBoxLayout()
        self.verticalLayout_226.setObjectName("verticalLayout_226")
        self.DL1inputChannel = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL1inputChannel.setObjectName("DL1inputChannel")
        self.verticalLayout_226.addWidget(self.DL1inputChannel)
        spacerItem193 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_226.addItem(spacerItem193)
        self.DL1inputChannelErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL1inputChannelErr.setText("")
        self.DL1inputChannelErr.setObjectName("DL1inputChannelErr")
        self.DL1inputChannelErr.setStyleSheet('color: red')
        self.DL1inputChannelErr.setWordWrap(True)
        self.verticalLayout_226.addWidget(self.DL1inputChannelErr)
        spacerItem194 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_226.addItem(spacerItem194)
        self.DL1inputChannelInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL1inputChannelInput.setObjectName("DL1inputChannelInput")
        self.DL1inputChannelInput.setText("64")
        self.verticalLayout_226.addWidget(self.DL1inputChannelInput)
        self.horizontalLayout_76.addLayout(self.verticalLayout_226)
        spacerItem195 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_76.addItem(spacerItem195)


        self.verticalLayout_227 = QtWidgets.QVBoxLayout()
        self.verticalLayout_227.setObjectName("verticalLayout_227")
        self.DL1outputChannel = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL1outputChannel.setObjectName("DL1outputChannel")
        self.verticalLayout_227.addWidget(self.DL1outputChannel)
        spacerItem196 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_227.addItem(spacerItem196)
        self.DL1outputChannelErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL1outputChannelErr.setText("")
        self.DL1outputChannelErr.setObjectName("DL1outputChannelErr")
        self.DL1outputChannelErr.setStyleSheet('color: red')
        self.DL1outputChannelErr.setWordWrap(True)
        self.verticalLayout_227.addWidget(self.DL1outputChannelErr)
        spacerItem197 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_227.addItem(spacerItem197)
        self.DL1outputChannelInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL1outputChannelInput.setObjectName("DL1outputChannelInput")
        self.DL1outputChannelInput.setText("32")
        self.verticalLayout_227.addWidget(self.DL1outputChannelInput)
        self.horizontalLayout_76.addLayout(self.verticalLayout_227)
        spacerItem198 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_76.addItem(spacerItem198)


        self.verticalLayout_228 = QtWidgets.QVBoxLayout()
        self.verticalLayout_228.setObjectName("verticalLayout_228")
        self.DL1bias = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL1bias.setObjectName("DL1bias")
        self.verticalLayout_228.addWidget(self.DL1bias)
        spacerItem199 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_228.addItem(spacerItem199)
        self.DL1biasErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL1biasErr.setText("")
        self.DL1biasErr.setObjectName("DL1biasErr")
        self.DL1biasErr.setStyleSheet('color: red')
        self.DL1biasErr.setWordWrap(True)
        self.verticalLayout_228.addWidget(self.DL1biasErr)
        spacerItem200 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_228.addItem(spacerItem200)
        self.DL1biasInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL1biasInput.setObjectName("DL1biasInput")
        self.DL1biasInput.setText("True")
        self.verticalLayout_228.addWidget(self.DL1biasInput)
        self.horizontalLayout_76.addLayout(self.verticalLayout_228)
        spacerItem201 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_76.addItem(spacerItem201)


        self.verticalLayout_229 = QtWidgets.QVBoxLayout()
        self.verticalLayout_229.setObjectName("verticalLayout_229")
        self.DL1stride = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL1stride.setObjectName("DL1stride")
        self.verticalLayout_229.addWidget(self.DL1stride)
        spacerItem202 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_229.addItem(spacerItem202)
        self.DL1strideErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL1strideErr.setText("")
        self.DL1strideErr.setObjectName("DL1strideErr")
        self.DL1strideErr.setStyleSheet('color: red')
        self.DL1strideErr.setWordWrap(True)
        self.verticalLayout_229.addWidget(self.DL1strideErr)
        spacerItem203 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_229.addItem(spacerItem203)
        self.DL1strideInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL1strideInput.setObjectName("DL1strideInput")
        self.DL1strideInput.setText("1")
        self.verticalLayout_229.addWidget(self.DL1strideInput)
        self.horizontalLayout_76.addLayout(self.verticalLayout_229)
        spacerItem204 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_76.addItem(spacerItem204)


        self.verticalLayout_230 = QtWidgets.QVBoxLayout()
        self.verticalLayout_230.setObjectName("verticalLayout_230")
        self.DL1padding = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL1padding.setObjectName("DL1padding")
        self.verticalLayout_230.addWidget(self.DL1padding)
        spacerItem205 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_230.addItem(spacerItem205)
        self.DL1paddingErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL1paddingErr.setText("")
        self.DL1paddingErr.setObjectName("DL1paddingErr")
        self.DL1paddingErr.setStyleSheet('color: red')
        self.DL1paddingErr.setWordWrap(True)
        self.verticalLayout_230.addWidget(self.DL1paddingErr)
        spacerItem206 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_230.addItem(spacerItem206)
        self.DL1paddingInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL1paddingInput.setObjectName("DL1paddingInput")
        self.DL1paddingInput.setText("0")
        self.verticalLayout_230.addWidget(self.DL1paddingInput)
        self.horizontalLayout_76.addLayout(self.verticalLayout_230)
        spacerItem207 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_76.addItem(spacerItem207)


        self.verticalLayout_231 = QtWidgets.QVBoxLayout()
        self.verticalLayout_231.setObjectName("verticalLayout_231")
        self.DL1groups = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL1groups.setObjectName("DL1groups")
        self.verticalLayout_231.addWidget(self.DL1groups)
        spacerItem208 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_231.addItem(spacerItem208)
        self.DL1groupsErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL1groupsErr.setText("")
        self.DL1groupsErr.setObjectName("DL1groupsErr")
        self.DL1groupsErr.setStyleSheet('color: red')
        self.DL1groupsErr.setWordWrap(True)
        self.verticalLayout_231.addWidget(self.DL1groupsErr)
        spacerItem209 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_231.addItem(spacerItem209)
        self.DL1groupsInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL1groupsInput.setObjectName("DL1groupsInput")
        self.DL1groupsInput.setText("1")
        self.verticalLayout_231.addWidget(self.DL1groupsInput)


        self.horizontalLayout_76.addLayout(self.verticalLayout_231)
        self.verticalLayout_225.addLayout(self.horizontalLayout_76)
        self.horizontalLayout_74.addLayout(self.verticalLayout_225)
        self.verticalLayout_222.addLayout(self.horizontalLayout_74)
        self.verticalLayout_221.addLayout(self.verticalLayout_222)
        self.line_13 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.verticalLayout_221.addWidget(self.line_13)
        spacerItem210 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_221.addItem(spacerItem210)
        self.line_14 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.verticalLayout_221.addWidget(self.line_14)
        self.horizontalLayout_77 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_77.setObjectName("horizontalLayout_77")
        self.verticalLayout_232 = QtWidgets.QVBoxLayout()
        self.verticalLayout_232.setObjectName("verticalLayout_232")
        self.DL2topLbl = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL2topLbl.setObjectName("DL2topLbl")
        self.verticalLayout_232.addWidget(self.DL2topLbl)
        spacerItem211 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_232.addItem(spacerItem211)


        self.DL2convLevel = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        self.DL2convLevel.setObjectName("DL2convLevel")
        self.DL2convLevel.addItem("")
        self.DL2convLevel.addItem("")
        self.DL2convLevel.addItem("")
        self.DL2convLevel.addItem("")
        self.DL2convLevel.addItem("")
        self.DL2convLevel.setCurrentIndex(3)
        self.verticalLayout_232.addWidget(self.DL2convLevel)
        spacerItem212 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_232.addItem(spacerItem212)
        self.DL2activationFunc = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        self.DL2activationFunc.setObjectName("DL2activationFunc")
        self.DL2activationFunc.addItem("")
        self.DL2activationFunc.addItem("")
        self.DL2activationFunc.setCurrentIndex(1)
        self.verticalLayout_232.addWidget(self.DL2activationFunc)
        self.horizontalLayout_77.addLayout(self.verticalLayout_232)
        self.verticalLayout_233 = QtWidgets.QVBoxLayout()
        self.verticalLayout_233.setObjectName("verticalLayout_233")
        self.horizontalLayout_78 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_78.setObjectName("horizontalLayout_78")
        self.DL2numBlocks = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL2numBlocks.setObjectName("DL2numBlocks")
        self.horizontalLayout_78.addWidget(self.DL2numBlocks)
        spacerItem213 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_78.addItem(spacerItem213)
        self.DL2NumBlocks = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL2NumBlocks.setObjectName("DL2NumBlocks")
        self.DL2NumBlocks.setText("2")
        self.horizontalLayout_78.addWidget(self.DL2NumBlocks)
        spacerItem214 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_78.addItem(spacerItem214)
        self.verticalLayout_233.addLayout(self.horizontalLayout_78)
        spacerItem215 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_233.addItem(spacerItem215)


        self.horizontalLayout_79 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_79.setObjectName("horizontalLayout_79")
        self.verticalLayout_234 = QtWidgets.QVBoxLayout()
        self.verticalLayout_234.setObjectName("verticalLayout_234")
        self.DL2inputChannel = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL2inputChannel.setObjectName("DL2inputChannel")
        self.verticalLayout_234.addWidget(self.DL2inputChannel)
        spacerItem216 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_234.addItem(spacerItem216)
        self.DL2inputChannelErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL2inputChannelErr.setText("")
        self.DL2inputChannelErr.setObjectName("DL2inputChannelErr")
        self.DL2inputChannelErr.setStyleSheet('color: red')
        self.DL2inputChannelErr.setWordWrap(True)
        self.verticalLayout_234.addWidget(self.DL2inputChannelErr)
        spacerItem217 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_234.addItem(spacerItem217)
        self.DL2inputChannelInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL2inputChannelInput.setObjectName("DL2inputChannelInput")
        self.DL2inputChannelInput.setText("32")
        self.verticalLayout_234.addWidget(self.DL2inputChannelInput)
        self.horizontalLayout_79.addLayout(self.verticalLayout_234)
        spacerItem218 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_79.addItem(spacerItem218)


        self.verticalLayout_235 = QtWidgets.QVBoxLayout()
        self.verticalLayout_235.setObjectName("verticalLayout_235")
        self.DL2outputChannel = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL2outputChannel.setObjectName("DL2outputChannel")
        self.verticalLayout_235.addWidget(self.DL2outputChannel)
        spacerItem219 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_235.addItem(spacerItem219)
        self.DL2outputChannelErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL2outputChannelErr.setText("")
        self.DL2outputChannelErr.setObjectName("DL2outputChannelErr")
        self.DL2outputChannelErr.setStyleSheet('color: red')
        self.DL2outputChannelErr.setWordWrap(True)
        self.verticalLayout_235.addWidget(self.DL2outputChannelErr)
        spacerItem220 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_235.addItem(spacerItem220)
        self.DL2outputChannelInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL2outputChannelInput.setObjectName("DL2outputChannelInput")
        self.DL2outputChannelInput.setText("16")
        self.verticalLayout_235.addWidget(self.DL2outputChannelInput)
        self.horizontalLayout_79.addLayout(self.verticalLayout_235)
        spacerItem221 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_79.addItem(spacerItem221)


        self.verticalLayout_236 = QtWidgets.QVBoxLayout()
        self.verticalLayout_236.setObjectName("verticalLayout_236")
        self.DL2bias = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL2bias.setObjectName("DL2bias")
        self.verticalLayout_236.addWidget(self.DL2bias)
        spacerItem222 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_236.addItem(spacerItem222)
        self.DL2biasErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL2biasErr.setText("")
        self.DL2biasErr.setObjectName("DL2biasErr")
        self.DL2biasErr.setStyleSheet('color: red')
        self.DL2biasErr.setWordWrap(True)
        self.verticalLayout_236.addWidget(self.DL2biasErr)
        spacerItem223 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_236.addItem(spacerItem223)
        self.DL2biasInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL2biasInput.setObjectName("DL2biasInput")
        self.DL2biasInput.setText("True")
        self.verticalLayout_236.addWidget(self.DL2biasInput)
        self.horizontalLayout_79.addLayout(self.verticalLayout_236)
        spacerItem224 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_79.addItem(spacerItem224)


        self.verticalLayout_237 = QtWidgets.QVBoxLayout()
        self.verticalLayout_237.setObjectName("verticalLayout_237")
        self.DL2stride = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL2stride.setObjectName("DL2stride")
        self.verticalLayout_237.addWidget(self.DL2stride)
        spacerItem225 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_237.addItem(spacerItem225)
        self.DL2strideErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL2strideErr.setText("")
        self.DL2strideErr.setObjectName("DL2strideErr")
        self.DL2strideErr.setStyleSheet('color: red')
        self.DL2strideErr.setWordWrap(True)
        self.verticalLayout_237.addWidget(self.DL2strideErr)
        spacerItem226 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_237.addItem(spacerItem226)
        self.DL2strideInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL2strideInput.setObjectName("DL2strideInput")
        self.DL2strideInput.setText("1")
        self.verticalLayout_237.addWidget(self.DL2strideInput)
        self.horizontalLayout_79.addLayout(self.verticalLayout_237)
        spacerItem227 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_79.addItem(spacerItem227)


        self.verticalLayout_238 = QtWidgets.QVBoxLayout()
        self.verticalLayout_238.setObjectName("verticalLayout_238")
        self.DL2padding = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL2padding.setObjectName("DL2padding")
        self.verticalLayout_238.addWidget(self.DL2padding)
        spacerItem228 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_238.addItem(spacerItem228)
        self.DL2paddingErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL2paddingErr.setText("")
        self.DL2paddingErr.setObjectName("DL2paddingErr")
        self.DL2paddingErr.setStyleSheet('color: red')
        self.DL2paddingErr.setWordWrap(True)
        self.verticalLayout_238.addWidget(self.DL2paddingErr)
        spacerItem229 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_238.addItem(spacerItem229)
        self.DL2paddingInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL2paddingInput.setObjectName("DL2paddingInput")
        self.DL2paddingInput.setText("0")
        self.verticalLayout_238.addWidget(self.DL2paddingInput)
        self.horizontalLayout_79.addLayout(self.verticalLayout_238)
        spacerItem230 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_79.addItem(spacerItem230)


        self.verticalLayout_239 = QtWidgets.QVBoxLayout()
        self.verticalLayout_239.setObjectName("verticalLayout_239")
        self.DL2groups = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL2groups.setObjectName("DL2groups")
        self.verticalLayout_239.addWidget(self.DL2groups)
        spacerItem231 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_239.addItem(spacerItem231)
        self.DL2groupsErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL2groupsErr.setText("")
        self.DL2groupsErr.setObjectName("DL2groupsErr")
        self.DL2groupsErr.setStyleSheet('color: red')
        self.DL2groupsErr.setWordWrap(True)
        self.verticalLayout_239.addWidget(self.DL2groupsErr)
        spacerItem232 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_239.addItem(spacerItem232)


        self.DL2groupsInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL2groupsInput.setObjectName("DL2groupsInput")
        self.DL2groupsInput.setText("1")
        self.verticalLayout_239.addWidget(self.DL2groupsInput)
        self.horizontalLayout_79.addLayout(self.verticalLayout_239)
        self.verticalLayout_233.addLayout(self.horizontalLayout_79)
        self.horizontalLayout_77.addLayout(self.verticalLayout_233)
        self.verticalLayout_221.addLayout(self.horizontalLayout_77)
        self.verticalLayout_220.addLayout(self.verticalLayout_221)
        self.line_15 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.verticalLayout_220.addWidget(self.line_15)
        spacerItem233 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_220.addItem(spacerItem233)
        self.line_16 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.verticalLayout_220.addWidget(self.line_16)
        self.horizontalLayout_80 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_80.setObjectName("horizontalLayout_80")
        self.verticalLayout_240 = QtWidgets.QVBoxLayout()
        self.verticalLayout_240.setObjectName("verticalLayout_240")
        self.DL3topLbl = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL3topLbl.setObjectName("DL3topLbl")
        self.verticalLayout_240.addWidget(self.DL3topLbl)
        spacerItem234 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_240.addItem(spacerItem234)


        self.DL3convLevel = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        self.DL3convLevel.setObjectName("DL3convLevel")
        self.DL3convLevel.addItem("")
        self.DL3convLevel.addItem("")
        self.DL3convLevel.addItem("")
        self.DL3convLevel.addItem("")
        self.DL3convLevel.addItem("")
        self.DL3convLevel.setCurrentIndex(3)
        self.verticalLayout_240.addWidget(self.DL3convLevel)
        spacerItem235 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_240.addItem(spacerItem235)
        self.DL3activationFunc = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        self.DL3activationFunc.setObjectName("DL3activationFunc")
        self.DL3activationFunc.addItem("")
        self.DL3activationFunc.addItem("")
        self.DL3activationFunc.setCurrentIndex(1)
        self.verticalLayout_240.addWidget(self.DL3activationFunc)
        self.horizontalLayout_80.addLayout(self.verticalLayout_240)
        self.verticalLayout_241 = QtWidgets.QVBoxLayout()
        self.verticalLayout_241.setObjectName("verticalLayout_241")
        self.horizontalLayout_81 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_81.setObjectName("horizontalLayout_81")
        self.DL3numBlocks = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL3numBlocks.setObjectName("DL3numBlocks")
        self.horizontalLayout_81.addWidget(self.DL3numBlocks)
        spacerItem236 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_81.addItem(spacerItem236)
        self.DL3NumBlocks = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL3NumBlocks.setObjectName("DL3NumBlocks")
        self.DL3NumBlocks.setText("2")
        self.horizontalLayout_81.addWidget(self.DL3NumBlocks)
        spacerItem237 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_81.addItem(spacerItem237)
        self.verticalLayout_241.addLayout(self.horizontalLayout_81)
        spacerItem238 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_241.addItem(spacerItem238)
        self.horizontalLayout_82 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_82.setObjectName("horizontalLayout_82")
        self.verticalLayout_242 = QtWidgets.QVBoxLayout()
        self.verticalLayout_242.setObjectName("verticalLayout_242")


        self.DL3inputChannel = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL3inputChannel.setObjectName("DL3inputChannel")
        self.verticalLayout_242.addWidget(self.DL3inputChannel)
        spacerItem239 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_242.addItem(spacerItem239)
        self.DL3inputChannelErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL3inputChannelErr.setText("")
        self.DL3inputChannelErr.setObjectName("DL3inputChannelErr")
        self.DL3inputChannelErr.setStyleSheet('color: red')
        self.DL3inputChannelErr.setWordWrap(True)
        self.verticalLayout_242.addWidget(self.DL3inputChannelErr)
        spacerItem240 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_242.addItem(spacerItem240)
        self.DL3inputChannelInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL3inputChannelInput.setObjectName("DL3inputChannelInput")
        self.DL3inputChannelInput.setText("16")
        self.verticalLayout_242.addWidget(self.DL3inputChannelInput)
        self.horizontalLayout_82.addLayout(self.verticalLayout_242)
        spacerItem241 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_82.addItem(spacerItem241)


        self.verticalLayout_243 = QtWidgets.QVBoxLayout()
        self.verticalLayout_243.setObjectName("verticalLayout_243")
        self.DL3outputChannel = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL3outputChannel.setObjectName("DL3outputChannel")
        self.verticalLayout_243.addWidget(self.DL3outputChannel)
        spacerItem242 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_243.addItem(spacerItem242)
        self.DL3outputChannelErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL3outputChannelErr.setText("")
        self.DL3outputChannelErr.setObjectName("DL3outputChannelErr")
        self.DL3outputChannelErr.setStyleSheet('color: red')
        self.DL3outputChannelErr.setWordWrap(True)
        self.verticalLayout_243.addWidget(self.DL3outputChannelErr)
        spacerItem243 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_243.addItem(spacerItem243)
        self.DL3outputChannelInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL3outputChannelInput.setObjectName("DL3outputChannelInput")
        self.DL3outputChannelInput.setText("8")
        self.verticalLayout_243.addWidget(self.DL3outputChannelInput)
        self.horizontalLayout_82.addLayout(self.verticalLayout_243)
        spacerItem244 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_82.addItem(spacerItem244)


        self.verticalLayout_244 = QtWidgets.QVBoxLayout()
        self.verticalLayout_244.setObjectName("verticalLayout_244")
        self.DL3bias = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL3bias.setObjectName("DL3bias")
        self.verticalLayout_244.addWidget(self.DL3bias)
        spacerItem245 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_244.addItem(spacerItem245)
        self.DL3biasErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL3biasErr.setText("")
        self.DL3biasErr.setObjectName("DL3biasErr")
        self.DL3biasErr.setStyleSheet('color: red')
        self.DL3biasErr.setWordWrap(True)
        self.verticalLayout_244.addWidget(self.DL3biasErr)
        spacerItem246 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_244.addItem(spacerItem246)
        self.DL3biasInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL3biasInput.setObjectName("DL3biasInput")
        self.DL3biasInput.setText("True")
        self.verticalLayout_244.addWidget(self.DL3biasInput)
        self.horizontalLayout_82.addLayout(self.verticalLayout_244)
        spacerItem247 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_82.addItem(spacerItem247)


        self.verticalLayout_245 = QtWidgets.QVBoxLayout()
        self.verticalLayout_245.setObjectName("verticalLayout_245")
        self.DL3stride = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL3stride.setObjectName("DL3stride")
        self.verticalLayout_245.addWidget(self.DL3stride)
        spacerItem248 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_245.addItem(spacerItem248)
        self.DL3strideErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL3strideErr.setText("")
        self.DL3strideErr.setObjectName("DL3strideErr")
        self.DL3strideErr.setStyleSheet('color: red')
        self.DL3strideErr.setWordWrap(True)
        self.verticalLayout_245.addWidget(self.DL3strideErr)
        spacerItem249 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_245.addItem(spacerItem249)
        self.DL3strideInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL3strideInput.setObjectName("DL3strideInput")
        self.DL3strideInput.setText("1")
        self.verticalLayout_245.addWidget(self.DL3strideInput)
        self.horizontalLayout_82.addLayout(self.verticalLayout_245)
        spacerItem250 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_82.addItem(spacerItem250)


        self.verticalLayout_246 = QtWidgets.QVBoxLayout()
        self.verticalLayout_246.setObjectName("verticalLayout_246")
        self.DL3padding = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL3padding.setObjectName("DL3padding")
        self.verticalLayout_246.addWidget(self.DL3padding)
        spacerItem251 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_246.addItem(spacerItem251)
        self.DL3paddingErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL3paddingErr.setText("")
        self.DL3paddingErr.setObjectName("DL3paddingErr")
        self.DL3paddingErr.setStyleSheet('color: red')
        self.DL3paddingErr.setWordWrap(True)
        self.verticalLayout_246.addWidget(self.DL3paddingErr)
        spacerItem252 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_246.addItem(spacerItem252)
        self.DL3paddingInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL3paddingInput.setObjectName("DL3paddingInput")
        self.DL3paddingInput.setText("0")
        self.verticalLayout_246.addWidget(self.DL3paddingInput)
        self.horizontalLayout_82.addLayout(self.verticalLayout_246)
        spacerItem253 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_82.addItem(spacerItem253)


        self.verticalLayout_247 = QtWidgets.QVBoxLayout()
        self.verticalLayout_247.setObjectName("verticalLayout_247")
        self.DL3groups = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL3groups.setObjectName("DL3groups")
        self.verticalLayout_247.addWidget(self.DL3groups)
        spacerItem254 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_247.addItem(spacerItem254)
        self.DL3groupsErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL3groupsErr.setText("")
        self.DL3groupsErr.setObjectName("DL3groupsErr")
        self.DL3groupsErr.setStyleSheet('color: red')
        self.DL3groupsErr.setWordWrap(True)
        self.verticalLayout_247.addWidget(self.DL3groupsErr)
        spacerItem255 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_247.addItem(spacerItem255)
        self.DL3groupsInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL3groupsInput.setObjectName("DL3groupsInput")
        self.DL3groupsInput.setText("1")


        self.verticalLayout_247.addWidget(self.DL3groupsInput)
        self.horizontalLayout_82.addLayout(self.verticalLayout_247)
        self.verticalLayout_241.addLayout(self.horizontalLayout_82)
        self.horizontalLayout_80.addLayout(self.verticalLayout_241)
        self.verticalLayout_220.addLayout(self.horizontalLayout_80)
        self.line_17 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.verticalLayout_220.addWidget(self.line_17)
        self.verticalLayout_219.addLayout(self.verticalLayout_220)
        spacerItem256 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_219.addItem(spacerItem256)
        self.line_18 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.verticalLayout_219.addWidget(self.line_18)
        self.horizontalLayout_83 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_83.setObjectName("horizontalLayout_83")
        self.verticalLayout_248 = QtWidgets.QVBoxLayout()
        self.verticalLayout_248.setObjectName("verticalLayout_248")
        self.DL4topLbl = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL4topLbl.setObjectName("DL4topLbl")
        self.verticalLayout_248.addWidget(self.DL4topLbl)
        spacerItem257 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_248.addItem(spacerItem257)


        self.DL4convLevel = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        self.DL4convLevel.setObjectName("DL4convLevel")
        self.DL4convLevel.addItem("")
        self.DL4convLevel.addItem("")
        self.DL4convLevel.addItem("")
        self.DL4convLevel.addItem("")
        self.DL4convLevel.addItem("")
        self.DL4convLevel.setCurrentIndex(3)
        self.verticalLayout_248.addWidget(self.DL4convLevel)
        spacerItem258 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_248.addItem(spacerItem258)
        self.DL4activationFunc = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        self.DL4activationFunc.setObjectName("DL4activationFunc")
        self.DL4activationFunc.addItem("")
        self.DL4activationFunc.addItem("")
        self.DL4activationFunc.setCurrentIndex(1)
        self.verticalLayout_248.addWidget(self.DL4activationFunc)
        self.horizontalLayout_83.addLayout(self.verticalLayout_248)
        self.verticalLayout_249 = QtWidgets.QVBoxLayout()
        self.verticalLayout_249.setObjectName("verticalLayout_249")
        self.horizontalLayout_84 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_84.setObjectName("horizontalLayout_84")
        self.DL4numBlocks = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL4numBlocks.setObjectName("DL4numBlocks")
        self.horizontalLayout_84.addWidget(self.DL4numBlocks)
        spacerItem259 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_84.addItem(spacerItem259)
        self.DL4NumBlocks = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL4NumBlocks.setObjectName("DL4NumBlocks")
        self.DL4NumBlocks.setText("2")
        self.horizontalLayout_84.addWidget(self.DL4NumBlocks)
        spacerItem260 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_84.addItem(spacerItem260)
        self.verticalLayout_249.addLayout(self.horizontalLayout_84)
        spacerItem261 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_249.addItem(spacerItem261)
        self.horizontalLayout_85 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_85.setObjectName("horizontalLayout_85")
        self.verticalLayout_250 = QtWidgets.QVBoxLayout()
        self.verticalLayout_250.setObjectName("verticalLayout_250")
        self.DL4inputChannel = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)


        self.DL4inputChannel.setObjectName("DL4inputChannel")
        self.verticalLayout_250.addWidget(self.DL4inputChannel)
        spacerItem262 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_250.addItem(spacerItem262)
        self.DL4inputChannelErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL4inputChannelErr.setText("")
        self.DL4inputChannelErr.setObjectName("DL4inputChannelErr")
        self.DL4inputChannelErr.setStyleSheet('color: red')
        self.DL4inputChannelErr.setWordWrap(True)
        self.verticalLayout_250.addWidget(self.DL4inputChannelErr)
        spacerItem263 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_250.addItem(spacerItem263)
        self.DL4inputChannelInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL4inputChannelInput.setObjectName("DL4inputChannelInput")
        self.DL4inputChannelInput.setText("8")
        self.verticalLayout_250.addWidget(self.DL4inputChannelInput)
        self.horizontalLayout_85.addLayout(self.verticalLayout_250)
        spacerItem264 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_85.addItem(spacerItem264)


        self.verticalLayout_251 = QtWidgets.QVBoxLayout()
        self.verticalLayout_251.setObjectName("verticalLayout_251")
        self.DL4outputChannel = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL4outputChannel.setObjectName("DL4outputChannel")
        self.verticalLayout_251.addWidget(self.DL4outputChannel)
        spacerItem265 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_251.addItem(spacerItem265)
        self.DL4outputChannelErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL4outputChannelErr.setText("")
        self.DL4outputChannelErr.setObjectName("DL4outputChannelErr")
        self.DL4outputChannelErr.setStyleSheet('color: red')
        self.DL4outputChannelErr.setWordWrap(True)
        self.verticalLayout_251.addWidget(self.DL4outputChannelErr)
        spacerItem266 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_251.addItem(spacerItem266)
        self.DL4outputChannelInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL4outputChannelInput.setObjectName("DL4outputChannelInput")
        self.DL4outputChannelInput.setText("4")
        self.verticalLayout_251.addWidget(self.DL4outputChannelInput)
        self.horizontalLayout_85.addLayout(self.verticalLayout_251)
        spacerItem267 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_85.addItem(spacerItem267)


        self.verticalLayout_252 = QtWidgets.QVBoxLayout()
        self.verticalLayout_252.setObjectName("verticalLayout_252")
        self.DL4bias = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL4bias.setObjectName("DL4bias")
        self.verticalLayout_252.addWidget(self.DL4bias)
        spacerItem268 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_252.addItem(spacerItem268)
        self.DL4biasErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL4biasErr.setText("")
        self.DL4biasErr.setObjectName("DL4biasErr")
        self.DL4biasErr.setStyleSheet('color: red')
        self.DL4biasErr.setWordWrap(True)
        self.verticalLayout_252.addWidget(self.DL4biasErr)
        spacerItem269 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_252.addItem(spacerItem269)
        self.DL4biasInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL4biasInput.setObjectName("DL4biasInput")
        self.DL4biasInput.setText("True")
        self.verticalLayout_252.addWidget(self.DL4biasInput)
        self.horizontalLayout_85.addLayout(self.verticalLayout_252)
        spacerItem270 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_85.addItem(spacerItem270)


        self.verticalLayout_253 = QtWidgets.QVBoxLayout()
        self.verticalLayout_253.setObjectName("verticalLayout_253")
        self.DL4stride = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL4stride.setObjectName("DL4stride")
        self.verticalLayout_253.addWidget(self.DL4stride)
        spacerItem271 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_253.addItem(spacerItem271)
        self.DL4strideErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL4strideErr.setText("")
        self.DL4strideErr.setObjectName("DL4strideErr")
        self.DL4strideErr.setStyleSheet('color: red')
        self.DL4strideErr.setWordWrap(True)
        self.verticalLayout_253.addWidget(self.DL4strideErr)
        spacerItem272 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_253.addItem(spacerItem272)
        self.DL4strideInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL4strideInput.setObjectName("DL4strideInput")
        self.DL4strideInput.setText("1")
        self.verticalLayout_253.addWidget(self.DL4strideInput)
        self.horizontalLayout_85.addLayout(self.verticalLayout_253)
        spacerItem273 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_85.addItem(spacerItem273)


        self.verticalLayout_254 = QtWidgets.QVBoxLayout()
        self.verticalLayout_254.setObjectName("verticalLayout_254")
        self.DL4padding = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL4padding.setObjectName("DL4padding")
        self.verticalLayout_254.addWidget(self.DL4padding)
        spacerItem274 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_254.addItem(spacerItem274)
        self.DL4paddingErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL4paddingErr.setText("")
        self.DL4paddingErr.setObjectName("DL4paddingErr")
        self.DL4paddingErr.setStyleSheet('color: red')
        self.DL4paddingErr.setWordWrap(True)
        self.verticalLayout_254.addWidget(self.DL4paddingErr)
        spacerItem275 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_254.addItem(spacerItem275)
        self.DL4paddingInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL4paddingInput.setObjectName("DL4paddingInput")
        self.DL4paddingInput.setText("0")
        self.verticalLayout_254.addWidget(self.DL4paddingInput)
        self.horizontalLayout_85.addLayout(self.verticalLayout_254)
        spacerItem276 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_85.addItem(spacerItem276)


        self.verticalLayout_255 = QtWidgets.QVBoxLayout()
        self.verticalLayout_255.setObjectName("verticalLayout_255")
        self.DL4groups = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL4groups.setObjectName("DL4groups")
        self.verticalLayout_255.addWidget(self.DL4groups)
        spacerItem277 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_255.addItem(spacerItem277)
        self.DL4groupsErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL4groupsErr.setText("")
        self.DL4groupsErr.setObjectName("DL4groupsErr")
        self.DL4groupsErr.setStyleSheet('color: red')
        self.DL4groupsErr.setWordWrap(True)
        self.verticalLayout_255.addWidget(self.DL4groupsErr)
        spacerItem278 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_255.addItem(spacerItem278)


        self.DL4groupsInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL4groupsInput.setObjectName("DL4groupsInput")
        self.DL4groupsInput.setText("1")
        self.verticalLayout_255.addWidget(self.DL4groupsInput)
        self.horizontalLayout_85.addLayout(self.verticalLayout_255)
        self.verticalLayout_249.addLayout(self.horizontalLayout_85)
        self.horizontalLayout_83.addLayout(self.verticalLayout_249)
        self.verticalLayout_219.addLayout(self.horizontalLayout_83)
        self.verticalLayout_218.addLayout(self.verticalLayout_219)
        self.line_19 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.verticalLayout_218.addWidget(self.line_19)
        spacerItem279 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_218.addItem(spacerItem279)


        self.line_20 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.verticalLayout_218.addWidget(self.line_20)
        self.horizontalLayout_86 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_86.setObjectName("horizontalLayout_86")
        self.verticalLayout_256 = QtWidgets.QVBoxLayout()
        self.verticalLayout_256.setObjectName("verticalLayout_256")
        self.DL5topLbl = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL5topLbl.setObjectName("DL5topLbl")
        self.verticalLayout_256.addWidget(self.DL5topLbl)
        spacerItem280 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_256.addItem(spacerItem280)
        self.DL5convLevel = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        self.DL5convLevel.setObjectName("DL5convLevel")
        self.DL5convLevel.addItem("")
        self.DL5convLevel.addItem("")
        self.DL5convLevel.addItem("")
        self.DL5convLevel.addItem("")
        self.DL5convLevel.addItem("")
        self.DL5convLevel.setCurrentIndex(3)
        self.verticalLayout_256.addWidget(self.DL5convLevel)
        spacerItem281 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_256.addItem(spacerItem281)
        self.DL5activationFunc = QtWidgets.QComboBox(self.scrollAreaWidgetContents_4)
        self.DL5activationFunc.setObjectName("DL5activationFunc")
        self.DL5activationFunc.addItem("")
        self.DL5activationFunc.addItem("")
        self.DL5activationFunc.setCurrentIndex(1)
        self.verticalLayout_256.addWidget(self.DL5activationFunc)
        self.horizontalLayout_86.addLayout(self.verticalLayout_256)
        self.verticalLayout_257 = QtWidgets.QVBoxLayout()
        self.verticalLayout_257.setObjectName("verticalLayout_257")
        self.horizontalLayout_87 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_87.setObjectName("horizontalLayout_87")
        self.DL5numBlocks = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL5numBlocks.setObjectName("DL5numBlocks")
        self.horizontalLayout_87.addWidget(self.DL5numBlocks)
        spacerItem282 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_87.addItem(spacerItem282)
        self.DL5NumBlocks = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL5NumBlocks.setObjectName("DL5NumBlocks")
        self.DL5NumBlocks.setText("2")
        self.horizontalLayout_87.addWidget(self.DL5NumBlocks)
        spacerItem283 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_87.addItem(spacerItem283)
        self.verticalLayout_257.addLayout(self.horizontalLayout_87)
        spacerItem284 = QtWidgets.QSpacerItem(20, 17, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_257.addItem(spacerItem284)
        self.horizontalLayout_88 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_88.setObjectName("horizontalLayout_88")
        self.verticalLayout_258 = QtWidgets.QVBoxLayout()
        self.verticalLayout_258.setObjectName("verticalLayout_258")
        self.DL5inputChannel = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)


        self.DL5inputChannel.setObjectName("DL5inputChannel")
        self.verticalLayout_258.addWidget(self.DL5inputChannel)
        spacerItem285 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_258.addItem(spacerItem285)
        self.DL5inputChannelErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL5inputChannelErr.setText("")
        self.DL5inputChannelErr.setObjectName("DL5inputChannelErr")
        self.DL5inputChannelErr.setStyleSheet('color: red')
        self.DL5inputChannelErr.setWordWrap(True)
        self.verticalLayout_258.addWidget(self.DL5inputChannelErr)
        spacerItem286 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_258.addItem(spacerItem286)
        self.DL5inputChannelInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL5inputChannelInput.setObjectName("DL5inputChannelInput")
        self.DL5inputChannelInput.setText("4")
        self.verticalLayout_258.addWidget(self.DL5inputChannelInput)
        self.horizontalLayout_88.addLayout(self.verticalLayout_258)
        spacerItem287 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_88.addItem(spacerItem287)


        self.verticalLayout_259 = QtWidgets.QVBoxLayout()
        self.verticalLayout_259.setObjectName("verticalLayout_259")
        self.DL5outputChannel = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL5outputChannel.setObjectName("DL5outputChannel")
        self.verticalLayout_259.addWidget(self.DL5outputChannel)
        spacerItem288 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_259.addItem(spacerItem288)
        self.DL5outputChannelErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL5outputChannelErr.setText("")
        self.DL5outputChannelErr.setObjectName("DL5outputChannelErr")
        self.DL5outputChannelErr.setStyleSheet('color: red')
        self.DL5outputChannelErr.setWordWrap(True)
        self.verticalLayout_259.addWidget(self.DL5outputChannelErr)
        spacerItem289 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_259.addItem(spacerItem289)
        self.DL5outputChannelInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL5outputChannelInput.setObjectName("DL5outputChannelInput")
        self.DL5outputChannelInput.setText("4")
        self.verticalLayout_259.addWidget(self.DL5outputChannelInput)
        self.horizontalLayout_88.addLayout(self.verticalLayout_259)
        spacerItem290 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_88.addItem(spacerItem290)


        self.verticalLayout_260 = QtWidgets.QVBoxLayout()
        self.verticalLayout_260.setObjectName("verticalLayout_260")
        self.DL5bias = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL5bias.setObjectName("DL5bias")
        self.verticalLayout_260.addWidget(self.DL5bias)
        spacerItem291 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_260.addItem(spacerItem291)
        self.DL5biasErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL5biasErr.setText("")
        self.DL5biasErr.setObjectName("DL5biasErr")
        self.DL5biasErr.setStyleSheet('color: red')
        self.DL5biasErr.setWordWrap(True)
        self.verticalLayout_260.addWidget(self.DL5biasErr)
        spacerItem292 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_260.addItem(spacerItem292)
        self.DL5biasInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL5biasInput.setObjectName("DL5biasInput")
        self.DL5biasInput.setText("True")
        self.verticalLayout_260.addWidget(self.DL5biasInput)
        self.horizontalLayout_88.addLayout(self.verticalLayout_260)
        spacerItem293 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_88.addItem(spacerItem293)


        self.verticalLayout_261 = QtWidgets.QVBoxLayout()
        self.verticalLayout_261.setObjectName("verticalLayout_261")
        self.DL5stride = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL5stride.setObjectName("DL5stride")
        self.verticalLayout_261.addWidget(self.DL5stride)
        spacerItem294 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_261.addItem(spacerItem294)
        self.DL5strideErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL5strideErr.setText("")
        self.DL5strideErr.setObjectName("DL5strideErr")
        self.DL5strideErr.setStyleSheet('color: red')
        self.DL5strideErr.setWordWrap(True)
        self.verticalLayout_261.addWidget(self.DL5strideErr)
        spacerItem295 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_261.addItem(spacerItem295)
        self.DL5strideInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL5strideInput.setObjectName("DL5strideInput")
        self.DL5strideInput.setText("1")
        self.verticalLayout_261.addWidget(self.DL5strideInput)
        self.horizontalLayout_88.addLayout(self.verticalLayout_261)
        spacerItem296 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_88.addItem(spacerItem296)


        self.verticalLayout_262 = QtWidgets.QVBoxLayout()
        self.verticalLayout_262.setObjectName("verticalLayout_262")
        self.DL5padding = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL5padding.setObjectName("DL5padding")
        self.verticalLayout_262.addWidget(self.DL5padding)
        spacerItem297 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_262.addItem(spacerItem297)
        self.DL5paddingErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL5paddingErr.setText("")
        self.DL5paddingErr.setObjectName("DL5paddingErr")
        self.DL5paddingErr.setStyleSheet('color: red')
        self.DL5paddingErr.setWordWrap(True)
        self.verticalLayout_262.addWidget(self.DL5paddingErr)
        spacerItem298 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_262.addItem(spacerItem298)
        self.DL5paddingInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL5paddingInput.setObjectName("DL5paddingInput")
        self.DL5paddingInput.setText("0")
        self.verticalLayout_262.addWidget(self.DL5paddingInput)
        self.horizontalLayout_88.addLayout(self.verticalLayout_262)
        spacerItem299 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_88.addItem(spacerItem299)


        self.verticalLayout_263 = QtWidgets.QVBoxLayout()
        self.verticalLayout_263.setObjectName("verticalLayout_263")
        self.DL5groups = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL5groups.setObjectName("DL5groups")
        self.verticalLayout_263.addWidget(self.DL5groups)
        spacerItem300 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_263.addItem(spacerItem300)
        self.DL5groupsErr = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.DL5groupsErr.setText("")
        self.DL5groupsErr.setObjectName("DL5groupsErr")
        self.DL5groupsErr.setStyleSheet('color: red')
        self.DL5groupsErr.setWordWrap(True)
        self.verticalLayout_263.addWidget(self.DL5groupsErr)
        spacerItem301 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_263.addItem(spacerItem301)
        self.DL5groupsInput = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.DL5groupsInput.setObjectName("DL5groupsInput")
        self.DL5groupsInput.setText("1")
        self.verticalLayout_263.addWidget(self.DL5groupsInput)
        self.horizontalLayout_88.addLayout(self.verticalLayout_263)
        self.verticalLayout_257.addLayout(self.horizontalLayout_88)
        self.horizontalLayout_86.addLayout(self.verticalLayout_257)
        self.verticalLayout_218.addLayout(self.horizontalLayout_86)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_264.addWidget(self.scrollArea_2)
        self.tabWidget.addTab(self.tab, "")
        self.horizontalLayout_73.addWidget(self.tabWidget)
        self.verticalLayout_216.addLayout(self.horizontalLayout_73)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2065, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Calling function for when training button is clicked
        self.trainButton.clicked.connect(partial(self.on_click, MainWindow))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_selectNetwork.setText(_translate("MainWindow", "Select Network"))
        self.networkComboBox.setItemText(0, _translate("MainWindow", "Please Select a Network"))
        self.networkComboBox.setItemText(1, _translate("MainWindow", "Segnet"))
        self.label.setText(_translate("MainWindow", "Image Size (pixels X pixels)"))
        self.label_numOfEpochs.setText(_translate("MainWindow", "Number of Epochs:"))
        self.label_numOfBatches.setText(_translate("MainWindow", "Number of Batches"))
        self.label_trainData.setText(_translate("MainWindow", "Training Data Location"))
        self.label_labeledData_2.setText(_translate("MainWindow", "Validation Data Location"))
        self.label_2.setText(_translate("MainWindow", "Number of Workers"))
        self.label_3.setText(_translate("MainWindow", "Learning Rate"))
        self.label_6.setText(_translate("MainWindow", "Log Intervals"))
        self.trainButton.setText(_translate("MainWindow", "Train"))
        #self.networkOverviewPicture.setText(_translate("MainWindow", "PICTURE FOR MAIN WINDOW USE IMAGINATION"))
        self.networkOverviewPicture.setPixmap(QtGui.QPixmap(os.getcwd() + "/overall.PNG"))

        self.networkOverviewDescription.setText(_translate("MainWindow", "Segnet is a deep convolutional encoder-decoder architecture for image segmentation."
                                                                         " This means that the network takes in images, passes them to encoders that break the "
                                                                         "image down into a smaller compressed image representing certain datapoints. This smaller "
                                                                         "encoded image is then passed through an equal and opposite amount of decoders. These decode the image "
                                                                         "to black and white. The white represents any cracks that are found in the network,"
                                                                         " and the black represents the rest of the pavement."
                                                                         ""))
        self.networkOverviewDescription.setFont(QtGui.QFont("Times", 14))
        self.networkOverviewDescription.setWordWrap(True)

        self.startFilters.setText(_translate("MainWindow", "Start Filters"))
        self.inputImageFileType.setText(_translate("MainWindow", "Input Image File Type"))
        self.outputImageFileType.setText(_translate("MainWindow", "Output Image File Type"))
        self.kernel.setText(_translate("MainWindow", "Kernel"))
        self.numberOfClasses.setText(_translate("MainWindow", "Number of Classes"))
        self.depth.setText(_translate("MainWindow", "Depth"))
        self.nInitFeatures.setText(_translate("MainWindow", "Number Initial Features"))
        self.factor.setText(_translate("MainWindow", "Factor"))
        self.dropRate.setText(_translate("MainWindow", "Drop Rate"))
        self.filterConfiguration.setText(_translate("MainWindow", "Filter Configuration"))
        self.encoderLayers.setText(_translate("MainWindow", "Encoder Layers"))
        self.decoderLayers.setText(_translate("MainWindow", "Decoder Layers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.networkOverview), _translate("MainWindow", "Network Overview"))
        #self.encoderPicture.setText(_translate("MainWindow", "PICTURE FOR ENCODER WINDOW USE IMAGINATION"))

        self.encoderPicture.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)


        self.encoderPicture.setPixmap(QtGui.QPixmap(os.getcwd() + "/encoder.png"))

        self.encoderDescription.setText(_translate("MainWindow", "Encoder Window: This window gives the option of changing certain variables"
                                                                 " in the encoders of this network. The encoders in this network take the original picture, "
                                                                 "and they perform mathematical operations on the pixels, compressing the image down into a much smaller and "
                                                                 "unrecognizable form (to humans). This network makes use of 5 encoder layers currently, and after they do their work on the "
                                                                 "input picture, they will pass it to the decoders."))
        self.encoderDescription.setFont(QtGui.QFont("Times", 14))


        self.encoderDescription.setWordWrap(True)
        self.EL1topLbl_4.setText(_translate("MainWindow", "Layer 1:"))
        self.EL1convLevel_5.setItemText(0, _translate("MainWindow", "Convolution Level"))
        self.EL1convLevel_5.setItemText(1, _translate("MainWindow", "1 x 1"))
        self.EL1convLevel_5.setItemText(2, _translate("MainWindow", "3 x 3"))
        self.EL1convLevel_5.setItemText(3, _translate("MainWindow", "7 x 7"))
        self.EL1convLevel_5.setItemText(4, _translate("MainWindow", "11 x 11"))
        self.EL1activationFunc_5.setItemText(0, _translate("MainWindow", "Activation Functions"))
        self.EL1activationFunc_5.setItemText(1, _translate("MainWindow", "Batch Normalization and ReLU"))
        self.EL1numBlocks.setText(_translate("MainWindow", "Number of Blocks ="))
        self.EL1inputChannel.setText(_translate("MainWindow", "Input Channel"))
        self.EL1outputChannel.setText(_translate("MainWindow", "Output Channel"))
        self.EL1bias.setText(_translate("MainWindow", "Bias"))
        self.EL1stride.setText(_translate("MainWindow", "Stride"))
        self.EL1padding.setText(_translate("MainWindow", "Padding"))
        self.EL1groups.setText(_translate("MainWindow", "Groups"))
        self.EL2topLbl.setText(_translate("MainWindow", "Layer 2:"))
        self.EL2convLevel.setItemText(0, _translate("MainWindow", "Convolution Level"))
        self.EL2convLevel.setItemText(1, _translate("MainWindow", "1 x 1"))
        self.EL2convLevel.setItemText(2, _translate("MainWindow", "3 x 3"))
        self.EL2convLevel.setItemText(3, _translate("MainWindow", "7 x 7"))
        self.EL2convLevel.setItemText(4, _translate("MainWindow", "11 x 11"))
        self.EL2activationFunc.setItemText(0, _translate("MainWindow", "Activation Functions"))
        self.EL2activationFunc.setItemText(1, _translate("MainWindow", "Batch Normalization and ReLU"))
        self.EL2numBlocks.setText(_translate("MainWindow", "Number of Blocks ="))
        self.EL2inputChannel.setText(_translate("MainWindow", "Input Channel"))
        self.EL2outputChannel.setText(_translate("MainWindow", "Output Channel"))
        self.EL2bias.setText(_translate("MainWindow", "Bias"))
        self.EL2stride.setText(_translate("MainWindow", "Stride"))
        self.EL2padding.setText(_translate("MainWindow", "Padding"))
        self.EL2groups.setText(_translate("MainWindow", "Groups"))
        self.EL3topLbl.setText(_translate("MainWindow", "Layer 3:"))
        self.EL3convLevel.setItemText(0, _translate("MainWindow", "Convolution Level"))
        self.EL3convLevel.setItemText(1, _translate("MainWindow", "1 x 1"))
        self.EL3convLevel.setItemText(2, _translate("MainWindow", "3 x 3"))
        self.EL3convLevel.setItemText(3, _translate("MainWindow", "7 x 7"))
        self.EL3convLevel.setItemText(4, _translate("MainWindow", "11 x 11"))
        self.EL3activationFunc.setItemText(0, _translate("MainWindow", "Activation Functions"))
        self.EL3activationFunc.setItemText(1, _translate("MainWindow", "Batch Normalization and ReLU"))
        self.EL3numBlocks.setText(_translate("MainWindow", "Number of Blocks ="))
        self.EL3inputChannel.setText(_translate("MainWindow", "Input Channel"))
        self.EL3outputChannel.setText(_translate("MainWindow", "Output Channel"))
        self.EL3bias.setText(_translate("MainWindow", "Bias"))
        self.EL3stride.setText(_translate("MainWindow", "Stride"))
        self.EL3padding.setText(_translate("MainWindow", "Padding"))
        self.EL3groups.setText(_translate("MainWindow", "Groups"))
        self.EL4topLbl.setText(_translate("MainWindow", "Layer 4:"))
        self.EL4convLevel.setItemText(0, _translate("MainWindow", "Convolution Level"))
        self.EL4convLevel.setItemText(1, _translate("MainWindow", "1 x 1"))
        self.EL4convLevel.setItemText(2, _translate("MainWindow", "3 x 3"))
        self.EL4convLevel.setItemText(3, _translate("MainWindow", "7 x 7"))
        self.EL4convLevel.setItemText(4, _translate("MainWindow", "11 x 11"))
        self.EL4activationFunc.setItemText(0, _translate("MainWindow", "Activation Functions"))
        self.EL4activationFunc.setItemText(1, _translate("MainWindow", "Batch Normalization and ReLU"))
        self.EL4numBlocks.setText(_translate("MainWindow", "Number of Blocks ="))
        self.EL4inputChannel.setText(_translate("MainWindow", "Input Channel"))
        self.EL4outputChannel.setText(_translate("MainWindow", "Output Channel"))
        self.EL4bias.setText(_translate("MainWindow", "Bias"))
        self.EL4stride.setText(_translate("MainWindow", "Stride"))
        self.EL4padding.setText(_translate("MainWindow", "Padding"))
        self.EL4groups.setText(_translate("MainWindow", "Groups"))
        self.EL5topLbl.setText(_translate("MainWindow", "Layer 5:"))
        self.EL5convLevel.setItemText(0, _translate("MainWindow", "Convolution Level"))
        self.EL5convLevel.setItemText(1, _translate("MainWindow", "1 x 1"))
        self.EL5convLevel.setItemText(2, _translate("MainWindow", "3 x 3"))
        self.EL5convLevel.setItemText(3, _translate("MainWindow", "7 x 7"))
        self.EL5convLevel.setItemText(4, _translate("MainWindow", "11 x 11"))
        self.EL5activationFunc.setItemText(0, _translate("MainWindow", "Activation Functions"))
        self.EL5activationFunc.setItemText(1, _translate("MainWindow", "Batch Normalization and ReLU"))
        self.EL5numBlocks.setText(_translate("MainWindow", "Number of Blocks ="))
        self.EL5inputChannel.setText(_translate("MainWindow", "Input Channel"))
        self.EL5outputChannel.setText(_translate("MainWindow", "Output Channel"))
        self.EL5bias.setText(_translate("MainWindow", "Bias"))
        self.EL5stride.setText(_translate("MainWindow", "Stride"))
        self.EL5padding.setText(_translate("MainWindow", "Padding"))
        self.EL5groups.setText(_translate("MainWindow", "Groups"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.encoderLayer), _translate("MainWindow", "Encoder Layers"))
        #self.DecoderPicture.setText(_translate("MainWindow", "PICTURE FOR DECODER WINDOW USE IMAGINATION"))

        self.DecoderPicture.setPixmap(QtGui.QPixmap(os.getcwd() + "/decoder.png"))

        self.decoderDescription.setText(_translate("MainWindow", "Decoder Window: This window gives the option of changing decoder variables. The decoders of this network take"
                                                                 " what the encoders give it, and they run that data through 5 similar convolutional and max pool layers. These layers put the "
                                                                 "image back together classifying if there are cracks or no cracks in the image. If there are cracks you see them display as the white"
                                                                 " line in the image. If the network misclassifies a crack, it will display as red, as shown in the picture."))
        self.decoderDescription.setFont(QtGui.QFont("Times", 14))

        self.decoderDescription.setWordWrap(True);
        self.DL1topLbl.setText(_translate("MainWindow", "Layer 1:"))
        self.EDL1convLevel.setItemText(0, _translate("MainWindow", "Convolution Level"))
        self.EDL1convLevel.setItemText(1, _translate("MainWindow", "1 x 1"))
        self.EDL1convLevel.setItemText(2, _translate("MainWindow", "3 x 3"))
        self.EDL1convLevel.setItemText(3, _translate("MainWindow", "7 x 7"))
        self.EDL1convLevel.setItemText(4, _translate("MainWindow", "11 x 11"))
        self.DL1activationFunc.setItemText(0, _translate("MainWindow", "Activation Functions"))
        self.DL1activationFunc.setItemText(1, _translate("MainWindow", "Batch Normalization and ReLU"))
        self.DL1numBlocks.setText(_translate("MainWindow", "Number of Blocks ="))
        self.DL1inputChannel.setText(_translate("MainWindow", "Input Channel"))
        self.DL1outputChannel.setText(_translate("MainWindow", "Output Channel"))
        self.DL1bias.setText(_translate("MainWindow", "Bias"))
        self.DL1stride.setText(_translate("MainWindow", "Stride"))
        self.DL1padding.setText(_translate("MainWindow", "Padding"))
        self.DL1groups.setText(_translate("MainWindow", "Groups"))
        self.DL2topLbl.setText(_translate("MainWindow", "Layer 2:"))
        self.DL2convLevel.setItemText(0, _translate("MainWindow", "Convolution Level"))
        self.DL2convLevel.setItemText(1, _translate("MainWindow", "1 x 1"))
        self.DL2convLevel.setItemText(2, _translate("MainWindow", "3 x 3"))
        self.DL2convLevel.setItemText(3, _translate("MainWindow", "7 x 7"))
        self.DL2convLevel.setItemText(4, _translate("MainWindow", "11 x 11"))
        self.DL2activationFunc.setItemText(0, _translate("MainWindow", "Activation Functions"))
        self.DL2activationFunc.setItemText(1, _translate("MainWindow", "Batch Normalization and ReLU"))
        self.DL2numBlocks.setText(_translate("MainWindow", "Number of Blocks ="))
        self.DL2inputChannel.setText(_translate("MainWindow", "Input Channel"))
        self.DL2outputChannel.setText(_translate("MainWindow", "Output Channel"))
        self.DL2bias.setText(_translate("MainWindow", "Bias"))
        self.DL2stride.setText(_translate("MainWindow", "Stride"))
        self.DL2padding.setText(_translate("MainWindow", "Padding"))
        self.DL2groups.setText(_translate("MainWindow", "Groups"))
        self.DL3topLbl.setText(_translate("MainWindow", "Layer 3:"))
        self.DL3convLevel.setItemText(0, _translate("MainWindow", "Convolution Level"))
        self.DL3convLevel.setItemText(1, _translate("MainWindow", "1 x 1"))
        self.DL3convLevel.setItemText(2, _translate("MainWindow", "3 x 3"))
        self.DL3convLevel.setItemText(3, _translate("MainWindow", "7 x 7"))
        self.DL3convLevel.setItemText(4, _translate("MainWindow", "11 x 11"))
        self.DL3activationFunc.setItemText(0, _translate("MainWindow", "Activation Functions"))
        self.DL3activationFunc.setItemText(1, _translate("MainWindow", "Batch Normalization and ReLU"))
        self.DL3numBlocks.setText(_translate("MainWindow", "Number of Blocks ="))
        self.DL3inputChannel.setText(_translate("MainWindow", "Input Channel"))
        self.DL3outputChannel.setText(_translate("MainWindow", "Output Channel"))
        self.DL3bias.setText(_translate("MainWindow", "Bias"))
        self.DL3stride.setText(_translate("MainWindow", "Stride"))
        self.DL3padding.setText(_translate("MainWindow", "Padding"))
        self.DL3groups.setText(_translate("MainWindow", "Groups"))
        self.DL4topLbl.setText(_translate("MainWindow", "Layer 4:"))
        self.DL4convLevel.setItemText(0, _translate("MainWindow", "Convolution Level"))
        self.DL4convLevel.setItemText(1, _translate("MainWindow", "1 x 1"))
        self.DL4convLevel.setItemText(2, _translate("MainWindow", "3 x 3"))
        self.DL4convLevel.setItemText(3, _translate("MainWindow", "7 x 7"))
        self.DL4convLevel.setItemText(4, _translate("MainWindow", "11 x 11"))
        self.DL4activationFunc.setItemText(0, _translate("MainWindow", "Activation Functions"))
        self.DL4activationFunc.setItemText(1, _translate("MainWindow", "Batch Normalization and ReLU"))
        self.DL4numBlocks.setText(_translate("MainWindow", "Number of Blocks ="))
        self.DL4inputChannel.setText(_translate("MainWindow", "Input Channel"))
        self.DL4outputChannel.setText(_translate("MainWindow", "Output Channel"))
        self.DL4bias.setText(_translate("MainWindow", "Bias"))
        self.DL4stride.setText(_translate("MainWindow", "Stride"))
        self.DL4padding.setText(_translate("MainWindow", "Padding"))
        self.DL4groups.setText(_translate("MainWindow", "Groups"))
        self.DL5topLbl.setText(_translate("MainWindow", "Layer 5:"))
        self.DL5convLevel.setItemText(0, _translate("MainWindow", "Convolution Level"))
        self.DL5convLevel.setItemText(1, _translate("MainWindow", "1 x 1"))
        self.DL5convLevel.setItemText(2, _translate("MainWindow", "3 x 3"))
        self.DL5convLevel.setItemText(3, _translate("MainWindow", "7 x 7"))
        self.DL5convLevel.setItemText(4, _translate("MainWindow", "11 x 11"))
        self.DL5activationFunc.setItemText(0, _translate("MainWindow", "Activation Functions"))
        self.DL5activationFunc.setItemText(1, _translate("MainWindow", "Batch Normalization and ReLU"))
        self.DL5numBlocks.setText(_translate("MainWindow", "Number of Blocks ="))
        self.DL5inputChannel.setText(_translate("MainWindow", "Input Channel"))
        self.DL5outputChannel.setText(_translate("MainWindow", "Output Channel"))
        self.DL5bias.setText(_translate("MainWindow", "Bias"))
        self.DL5stride.setText(_translate("MainWindow", "Stride"))
        self.DL5padding.setText(_translate("MainWindow", "Padding"))
        self.DL5groups.setText(_translate("MainWindow", "Groups"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Decoder Levels"))


    # on_click is triggered when the train button is selected

    def on_click(self, window):
        numberCheck = self.validateNumericInput()
        textCheck = self.validateTextInput()
        self.validateDropDowns()
        logicCheck = self.validateLogic()

        if numberCheck and textCheck and logicCheck:
            #print("test")
            outFile = open("variables.py", "w")
            outFile.write("imageLength=" + self.imageLength.text() + "\n")
            outFile.write("imageWidth=" + self.ImageWidth.text() + "\n")
            outFile.write("numEpochs=" + self.numEpochs.text() + "\n")
            outFile.write("numBatches=" + self.numBatches.text() + "\n")
            outFile.write("trainData=\"" + str(self.trainDataLocation.text()) + "\"\n")
            outFile.write("labelData=\"" + str(self.labeledDataFileLocation.text()) + "\"\n")
            outFile.write("numWorkers=" + self.numWorkers.text() + "\n")
            outFile.write("learningRate=" + self.LREntry.text() + "\n")
            outFile.write("logInterval=" + self.LogIntervals.text() + "\n")
            outFile.write("startFilters=" + self.startFiltersInput.text() + "\n")
            outFile.write("inputImageType=\"" + self.inputImageFileInput.text() + "\"\n")
            outFile.write("outputImageType=\"" + self.outputImageFileTypeInput.text() + "\"\n")
            outFile.write("kernel=" + self.kernelInput.text() + "\n")
            outFile.write("numClasses=" + self.numberOfClassesInput.text() + "\n")
            outFile.write("depth=" + self.depthInput.text() + "\n")
            outFile.write("nInitFeatures=" + self.nInitFeaturesInput.text() + "\n")
            outFile.write("factor=" + self.factorInput.text() + "\n")
            outFile.write("dropRate=" + self.dropRateInput.text() + "\n")
            outFile.write("filterConfig=" + self.filterConfigurationInput.text() + "\n")
            outFile.write("encoderLayers=" + self.encoderLayersInput.text() + "\n")
            outFile.write("decoderLayers=" + self.decoderLayersInput.text() + "\n")

            outFile.write("EL1numBlocks=" + self.EL1NumBlocks.text() + "\n")
            outFile.write("EL1convLevel=\"" + self.EL1convLevel_5.currentText() + "\"\n")
            outFile.write("EL1activationFunc=\"" + self.EL1activationFunc_5.currentText() + "\"\n")
            outFile.write("EL1inChannel=" + self.EL1inputChannelInput.text() + "\n")
            outFile.write("EL1outChannel=" + self.EL1outputChannelInput.text() + "\n")
            outFile.write("EL1bias=" + self.EL1biasInput.text() + "\n")
            outFile.write("EL1stride=" + self.EL1strideInput.text() + "\n")
            outFile.write("EL1padding=" + self.EL1paddingInput.text() + "\n")
            outFile.write("EL1groups=" + self.EL1groupsInput.text() + "\n")

            outFile.write("EL2numBlocks=" + self.EL2NumBlocks.text() + "\n")
            outFile.write("EL2convLevel=\"" + self.EL2convLevel.currentText() + "\"\n")
            outFile.write("EL2activationFunc=\"" + self.EL2activationFunc.currentText() + "\"\n")
            outFile.write("EL2inChannel=" + self.EL2inputChannelInput.text() + "\n")
            outFile.write("EL2outChannel=" + self.EL2outputChannelInput.text() + "\n")
            outFile.write("EL2bias=" + self.EL2biasInput.text() + "\n")
            outFile.write("EL2stride=" + self.EL2strideInput.text() + "\n")
            outFile.write("EL2padding=" + self.EL2paddingInput.text() + "\n")
            outFile.write("EL2groups=" + self.EL2groupsInput.text() + "\n")

            outFile.write("EL3numBlocks=" + self.EL3NumBlocks.text() + "\n")
            outFile.write("EL3convLevel=\"" + self.EL3convLevel.currentText() + "\"\n")
            outFile.write("EL3activationFunc=\"" + self.EL3activationFunc.currentText() + "\"\n")
            outFile.write("EL3inChannel=" + self.EL3inputChannelInput.text() + "\n")
            outFile.write("EL3outChannel=" + self.EL3outputChannelInput.text() + "\n")
            outFile.write("EL3bias=" + self.EL3biasInput.text() + "\n")
            outFile.write("EL3stride=" + self.EL3strideInput.text() + "\n")
            outFile.write("EL3padding=" + self.EL3paddingInput.text() + "\n")
            outFile.write("EL3groups=" + self.EL3groupsInput.text() + "\n")

            outFile.write("EL4numBlocks=" + self.EL4NumBlocks.text() + "\n")
            outFile.write("EL4convLevel=\"" + self.EL4convLevel.currentText() + "\"\n")
            outFile.write("EL4activationFunc=\"" + self.EL4activationFunc.currentText() + "\"\n")
            outFile.write("EL4inChannel=" + self.EL4inputChannelInput.text() + "\n")
            outFile.write("EL4outChannel=" + self.EL4outputChannelInput.text() + "\n")
            outFile.write("EL4bias=" + self.EL4biasInput.text() + "\n")
            outFile.write("EL4stride=" + self.EL4strideInput.text() + "\n")
            outFile.write("EL4padding=" + self.EL4paddingInput.text() + "\n")
            outFile.write("EL4groups=" + self.EL4groupsInput.text() + "\n")

            outFile.write("EL5numBlocks=" + self.EL5NumBlocks.text() + "\n")
            outFile.write("EL5convLevel=\"" + self.EL5convLevel.currentText() + "\"\n")
            outFile.write("EL5activationFunc=\"" + self.EL5activationFunc.currentText() + "\"\n")
            outFile.write("EL5inChannel=" + self.EL5inputChannelInput.text() + "\n")
            outFile.write("EL5outChannel=" + self.EL5outputChannelInput.text() + "\n")
            outFile.write("EL5bias=" + self.EL5biasInput.text() + "\n")
            outFile.write("EL5stride=" + self.EL5strideInput.text() + "\n")
            outFile.write("EL5padding=" + self.EL5paddingInput.text() + "\n")
            outFile.write("EL5groups=" + self.EL5groupsInput.text() + "\n")


            outFile.write("DL1numBlocks=" + self.EL1NumBlocks.text() + "\n")
            outFile.write("DL1convLevel=\"" + self.EL1convLevel_5.currentText() + "\"\n")
            outFile.write("DL1activationFunc=\"" + self.EL1activationFunc_5.currentText() + "\"\n")
            outFile.write("DL1inChannel=" + self.EL1inputChannelInput.text() + "\n")
            outFile.write("DL1outChannel=" + self.EL1outputChannelInput.text() + "\n")
            outFile.write("DL1bias=" + self.EL1biasInput.text() + "\n")
            outFile.write("DL1stride=" + self.EL1strideInput.text() + "\n")
            outFile.write("DL1padding=" + self.EL1paddingInput.text() + "\n")
            outFile.write("DL1groups=" + self.EL1groupsInput.text() + "\n")

            outFile.write("DL2numBlocks=" + self.EL2NumBlocks.text() + "\n")
            outFile.write("DL2convLevel=\"" + self.EL2convLevel.currentText() + "\"\n")
            outFile.write("DL2activationFunc=\"" + self.EL2activationFunc.currentText() + "\"\n")
            outFile.write("DL2inChannel=" + self.EL2inputChannelInput.text() + "\n")
            outFile.write("DL2outChannel=" + self.EL2outputChannelInput.text() + "\n")
            outFile.write("DL2bias=" + self.EL2biasInput.text() + "\n")
            outFile.write("DL2stride=" + self.EL2strideInput.text() + "\n")
            outFile.write("DL2padding=" + self.EL2paddingInput.text() + "\n")
            outFile.write("DL2groups=" + self.EL2groupsInput.text() + "\n")

            outFile.write("DL3numBlocks=" + self.EL3NumBlocks.text() + "\n")
            outFile.write("DL3convLevel=\"" + self.EL3convLevel.currentText() + "\"\n")
            outFile.write("DL3activationFunc=\"" + self.EL3activationFunc.currentText() + "\"\n")
            outFile.write("DL3inChannel=" + self.EL3inputChannelInput.text() + "\n")
            outFile.write("DL3outChannel=" + self.EL3outputChannelInput.text() + "\n")
            outFile.write("DL3bias=" + self.EL3biasInput.text() + "\n")
            outFile.write("DL3stride=" + self.EL3strideInput.text() + "\n")
            outFile.write("DL3padding=" + self.EL3paddingInput.text() + "\n")
            outFile.write("DL3groups=" + self.EL3groupsInput.text() + "\n")

            outFile.write("DL4numBlocks=" + self.EL4NumBlocks.text() + "\n")
            outFile.write("DL4convLevel=\"" + self.EL4convLevel.currentText() + "\"\n")
            outFile.write("DL4activationFunc=\"" + self.EL4activationFunc.currentText() + "\"\n")
            outFile.write("DL4inChannel=" + self.EL4inputChannelInput.text() + "\n")
            outFile.write("DL4outChannel=" + self.EL4outputChannelInput.text() + "\n")
            outFile.write("DL4bias=" + self.EL4biasInput.text() + "\n")
            outFile.write("DL4stride=" + self.EL4strideInput.text() + "\n")
            outFile.write("DL4padding=" + self.EL4paddingInput.text() + "\n")
            outFile.write("DL4groups=" + self.EL4groupsInput.text() + "\n")

            outFile.write("DL5numBlocks=" + self.EL5NumBlocks.text() + "\n")
            outFile.write("DL5convLevel=\"" + self.EL5convLevel.currentText() + "\"\n")
            outFile.write("DL5activationFunc=\"" + self.EL5activationFunc.currentText() + "\"\n")
            outFile.write("DL5inChannel=" + self.EL5inputChannelInput.text() + "\n")
            outFile.write("DL5outChannel=" + self.EL5outputChannelInput.text() + "\n")
            outFile.write("DL5bias=" + self.EL5biasInput.text() + "\n")
            outFile.write("DL5stride=" + self.EL5strideInput.text() + "\n")
            outFile.write("DL5padding=" + self.EL5paddingInput.text() + "\n")
            outFile.write("DL5groups=" + self.EL5groupsInput.text() + "\n")

            # Call next screen & run network here
            self.trainWindow = QtWidgets.QMainWindow()
            self.ui = TrainingWindow()
            self.ui.setupUi(self.trainWindow)
            window.close()
            self.trainWindow.show()
    """
    Function: ValidateNumberInput
    
    Param: Self - the window object
    
    Functionality: This function checks every numeric input textbox, it passes each textbox
                    parameter and a low and high range to the function checkNumericVal. 
                    checkNumericVal returns a boolean value, if the return is true, then the input 
                    passes and error labels are set to nothing, if it fails, than the error message is set 
                    giving the user the range in which the input should be.
    
    """

    def validateNumericInput(self):
        success = True
        imageTest = True
        # image width
        if self.checkNumericVal(self.imageLength.text(), 0, 6000):
            self.imageSizeError.setText("")
        else:
            self.imageSizeError.setText("Error: Image sizes should be numberic values, between 0 and 6000")
            imageTest = False
            success = False

        # image length
        if self.checkNumericVal(self.ImageWidth.text(), 0, 6000) and imageTest is True:
            self.imageSizeError.setText("")
        else:
            self.imageSizeError.setText("Error: Image sizes should be numberic values, between 0 and 6000")
            success = False

        # epochs
        if self.checkNumericVal(self.numEpochs.text(), 0, 1000):
            self.epochErrorLabel.setText("")
        else:
            success = False
            self.epochErrorLabel.setText("Error: epoch value should be a numeric value, between 0 and 1000")

        # batches
        if self.checkNumericVal(self.numBatches.text(), 0, 1000):
            self.batchErrorLabel.setText("")
        else:
            success = False
            self.batchErrorLabel.setText("Error: batch value should be a numeric value, between 0 and 1000")

        # workers
        if self.checkNumericVal(self.numWorkers.text(), 0, 100):
            self.numWorkersErrorLabel.setText("")
        else:
            success = False
            self.numWorkersErrorLabel.setText("Error: workers value should be a numeric value, between 0 and 100")

        # learning rate --> not using function because learning rate is a decimal, not a whole #
        if self.LREntry.text() == "" or self.LREntry.text().isdigit() or float(self.LREntry.text()) < 0 or float(self.LREntry.text()) > 1:
            success = False
            self.LRErrorLabel.setText("Error: learning rate value should be a numeric value, between 0 and 1")
        else:
            self.LRErrorLabel.setText("")

        # log intervals
        if self.checkNumericVal(self.LogIntervals.text(), 0, 1000):
            self.logIntervalsErrLabel.setText("")
        else:
            success = False
            self.logIntervalsErrLabel.setText("Error: log intervals value should be a numeric value, between 0 and 1000")

        # start filters
        if self.checkNumericVal(self.startFiltersInput.text(), 0, 20):
            self.startFiltersErr.setText("")
        else:
            success = False
            self.startFiltersErr.setText("Error: start filters value should be a numeric value, between 0 and 20")

        # number of classes
        if self.checkNumericVal(self.numberOfClassesInput.text(), 0, 20):
            self.numberOfClassesErr.setText("")
        else:
            success = False
            self.numberOfClassesErr.setText("Error: number of classes value should be a numeric value, between 0 and 20")

        # depth
        if self.checkNumericVal(self.depthInput.text(), 0, 20):
            self.depthErr.setText("")
        else:
            success = False
            self.depthErr.setText("Error: depth value should be a numeric value, between 0 and 20")

        # number of initial features
        if self.checkNumericVal(self.nInitFeaturesInput.text(), 0, 20):
            self.nInitFeaturesErr.setText("")
        else:
            success = False
            self.nInitFeaturesErr.setText("Error: number of initial features value should be a numeric value, between 0 and 20")

        # drop rate
        if self.dropRateInput.text() == "" or self.dropRateInput.text().isdigit() or float(self.dropRateInput.text()) < 0 or float(self.dropRateInput.text()) > 1:
            success = False
            self.dropRateErr.setText("Error: learning rate value should be a numeric value, between 0 and 1")
        else:
            self.dropRateErr.setText("")

        # encoder layers error checking:
        # layer 1: number of blocks
        # no label for number of blocks, defaults to 1 for invalid input
        if not self.checkNumericVal(self.EL1NumBlocks.text(), 0, 20):
            self.EL1NumBlocks.setText("1")

        # input channel and ouptut channel will be handeled by logic validation
        # stride
        if self.checkNumericVal(self.EL1strideInput.text(), 0, 10):
            self.EL1strideErr.setText("")
        else:
            success = False
            self.EL1strideErr.setText("Error: stride value should be a numeric value, between 0 and 10")

        # padding
        if self.checkNumericVal(self.EL1paddingInput.text(), -1, 10):
            self.EL1paddingErr.setText("")
        else:
            success = False
            self.EL1paddingErr.setText("Error: paddding value should be a numeric value, between 0 and 10")

        # groups
        if self.checkNumericVal(self.EL1groupsInput.text(), 0, 10):
            self.EL1groupsErr.setText("")
        else:
            success = False
            self.EL1groupsErr.setText("Error: group value should be a numeric value, between 0 and 10")


        # layer 2: number of blocks
        # no label for number of blocks, defaults to 1 for invalid input
        if not self.checkNumericVal(self.EL2NumBlocks.text(), 0, 20):
            self.EL2NumBlocks.setText("1")

        # input channel and ouptut channel will be handeled by logic validation
        # stride
        if self.checkNumericVal(self.EL2strideInput.text(), 0, 10):
            self.EL2strideErr.setText("")
        else:
            success = False
            self.EL2strideErr.setText("Error: stride value should be a numeric value, between 0 and 10")

        # padding
        if self.checkNumericVal(self.EL2paddingInput.text(), -1, 10):
            self.EL2paddingErr.setText("")
        else:
            success = False
            self.EL2paddingErr.setText("Error: paddding value should be a numeric value, between 0 and 10")

        # groups
        if self.checkNumericVal(self.EL2groupsInput.text(), 0, 10):
            self.EL2groupsErr.setText("")
        else:
            success = False
            self.EL2groupsErr.setText("Error: group value should be a numeric value, between 0 and 10")


        # layer 3: number of blocks
        # no label for number of blocks, defaults to 1 for invalid input
        if not self.checkNumericVal(self.EL3NumBlocks.text(), 0, 20):
            self.EL3NumBlocks.setText("1")

        # input channel and ouptut channel will be handeled by logic validation
        # stride
        if self.checkNumericVal(self.EL3strideInput.text(), 0, 10):
            self.EL3strideErr.setText("")
        else:
            success = False
            self.EL3strideErr.setText("Error: stride value should be a numeric value, between 0 and 10")

        # padding
        if self.checkNumericVal(self.EL3paddingInput.text(), -1, 10):
            self.EL3paddingErr.setText("")
        else:
            success = False
            self.EL3paddingErr.setText("Error: paddding value should be a numeric value, between 0 and 10")

        # groups
        if self.checkNumericVal(self.EL3groupsInput.text(), 0, 10):
            self.EL3groupsErr.setText("")
        else:
            success = False
            self.EL3groupsErr.setText("Error: group value should be a numeric value, between 0 and 10")


        # layer 4: number of blocks
        # no label for number of blocks, defaults to 1 for invalid input
        if not self.checkNumericVal(self.EL4NumBlocks.text(), 0, 20):
            self.EL4NumBlocks.setText("1")

        # input channel and ouptut channel will be handeled by logic validation
        # stride
        if self.checkNumericVal(self.EL4strideInput.text(), 0, 10):
            self.EL4strideErr.setText("")
        else:
            success = False
            self.EL4strideErr.setText("Error: stride value should be a numeric value, between 0 and 10")

        # padding
        if self.checkNumericVal(self.EL4paddingInput.text(), -1, 10):
            self.EL4paddingErr.setText("")
        else:
            success = False
            self.EL4paddingErr.setText("Error: paddding value should be a numeric value, between 0 and 10")

        # groups
        if self.checkNumericVal(self.EL4groupsInput.text(), 0, 10):
            self.EL4groupsErr.setText("")
        else:
            success = False
            self.EL4groupsErr.setText("Error: group value should be a numeric value, between 0 and 10")


        # layer 5: number of blocks
        # no label for number of blocks, defaults to 1 for invalid input
        if not self.checkNumericVal(self.EL5NumBlocks.text(), 0, 20):
            self.EL5NumBlocks.setText("1")

        # input channel and ouptut channel will be handeled by logic validation
        # stride
        if self.checkNumericVal(self.EL5strideInput.text(), 0, 10):
            self.EL5strideErr.setText("")
        else:
            success = False
            self.EL5strideErr.setText("Error: stride value should be a numeric value, between 0 and 10")

        # padding
        if self.checkNumericVal(self.EL5paddingInput.text(), -1, 10):
            self.EL5paddingErr.setText("")
        else:
            success = False
            self.EL5paddingErr.setText("Error: paddding value should be a numeric value, between 0 and 10")

        # groups
        if self.checkNumericVal(self.EL5groupsInput.text(), 0, 10):
            self.EL5groupsErr.setText("")
        else:
            success = False
            self.EL5groupsErr.setText("Error: group value should be a numeric value, between 0 and 10")


        # Decoders error checking
        # layer 1
        # layer 1: number of blocks
        # no label for number of blocks, defaults to 1 for invalid input
        if not self.checkNumericVal(self.DL1NumBlocks.text(), 0, 20):
            self.DL1NumBlocks.setText("2")

        # input channel and ouptut channel will be handeled by logic validation
        # stride
        if self.checkNumericVal(self.DL1strideInput.text(), 0, 10):
            self.DL1strideErr.setText("")
        else:
            success = False
            self.DL1strideErr.setText("Error: stride value should be a numeric value, between 0 and 10")

        # padding
        if self.checkNumericVal(self.DL1paddingInput.text(), -1, 10):
            self.DL1paddingErr.setText("")
        else:
            success = False
            self.DL1paddingErr.setText("Error: paddding value should be a numeric value, between 0 and 10")

        # groups
        if self.checkNumericVal(self.DL1groupsInput.text(), 0, 10):
            self.DL1groupsErr.setText("")
        else:
            success = False
            self.DL1groupsErr.setText("Error: group value should be a numeric value, between 0 and 10")

        # decoder layer 2
        if not self.checkNumericVal(self.DL2NumBlocks.text(), 0, 20):
            self.DL2NumBlocks.setText("2")

        # input channel and ouptut channel will be handeled by logic validation
        # stride
        if self.checkNumericVal(self.DL2strideInput.text(), 0, 10):
            self.DL2strideErr.setText("")
        else:
            success = False
            self.DL2strideErr.setText("Error: stride value should be a numeric value, between 0 and 10")

        # padding
        if self.checkNumericVal(self.DL2paddingInput.text(), -1, 10):
            self.DL2paddingErr.setText("")
        else:
            success = False
            self.DL2paddingErr.setText("Error: paddding value should be a numeric value, between 0 and 10")

        # groups
        if self.checkNumericVal(self.DL2groupsInput.text(), 0, 10):
            self.DL2groupsErr.setText("")
        else:
            success = False
            self.DL2groupsErr.setText("Error: group value should be a numeric value, between 0 and 10")


        # decoder level 3
        if not self.checkNumericVal(self.DL3NumBlocks.text(), 0, 20):
            self.DL3NumBlocks.setText("2")

        # input channel and ouptut channel will be handeled by logic validation
        # stride
        if self.checkNumericVal(self.DL3strideInput.text(), 0, 10):
            self.DL3strideErr.setText("")
        else:
            success = False
            self.DL3strideErr.setText("Error: stride value should be a numeric value, between 0 and 10")

        # padding
        if self.checkNumericVal(self.DL3paddingInput.text(), -1, 10):
            self.DL3paddingErr.setText("")
        else:
            success = False
            self.DL3paddingErr.setText("Error: paddding value should be a numeric value, between 0 and 10")

        # groups
        if self.checkNumericVal(self.DL3groupsInput.text(), 0, 10):
            self.DL3groupsErr.setText("")
        else:
            success = False
            self.DL3groupsErr.setText("Error: group value should be a numeric value, between 0 and 10")


        # decoder level 4
        if not self.checkNumericVal(self.DL4NumBlocks.text(), 0, 20):
            self.DL4NumBlocks.setText("2")

        # input channel and ouptut channel will be handeled by logic validation
        # stride
        if self.checkNumericVal(self.DL4strideInput.text(), 0, 10):
            self.DL4strideErr.setText("")
        else:
            success = False
            self.DL4strideErr.setText("Error: stride value should be a numeric value, between 0 and 10")

        # padding
        if self.checkNumericVal(self.DL4paddingInput.text(), -1, 10):
            self.DL4paddingErr.setText("")
        else:
            success = False
            self.DL4paddingErr.setText("Error: paddding value should be a numeric value, between 0 and 10")

        # groups
        if self.checkNumericVal(self.DL4groupsInput.text(), 0, 10):
            self.DL4groupsErr.setText("")
        else:
            success = False
            self.DL4groupsErr.setText("Error: group value should be a numeric value, between 0 and 10")

        # decoder level 5
        if not self.checkNumericVal(self.DL5NumBlocks.text(), 0, 20):
            self.DL5NumBlocks.setText("2")

        # input channel and ouptut channel will be handeled by logic validation
        # stride
        if self.checkNumericVal(self.DL5strideInput.text(), 0, 10):
            self.DL5strideErr.setText("")
        else:
            success = False
            self.DL5strideErr.setText("Error: stride value should be a numeric value, between 0 and 10")

        # padding
        if self.checkNumericVal(self.DL5paddingInput.text(), -1, 10):
            self.DL5paddingErr.setText("")
        else:
            success = False
            self.DL5paddingErr.setText("Error: paddding value should be a numeric value, between 0 and 10")

        # groups
        if self.checkNumericVal(self.DL5groupsInput.text(), 0, 10):
            self.DL5groupsErr.setText("")
        else:
            success = False
            self.DL5groupsErr.setText("Error: group value should be a numeric value, between 0 and 10")

        return success

    """
    Function: validateTextInput

    Param: Self - the window object

    Functionality: This function checks every text input textbox, the type of input 
                    dictates the tests done, for example for file location, it verifies
                    that location is an active directory. It validates that pictures are jpg, 
                    jpeg, or png, and it also verifies true/false inputs as well, and sets the 
                    activation layers and functions.

    """

    def validateTextInput(self):

        success = True

        # valid file directory for training data
        if not os.path.isdir(self.trainDataLocation.text()):
            self.trainingErrorLabel.setText("Error: Directory not found")
            success = False
        else:
            self.trainingErrorLabel.setText("");

        # valid file directory for testing data
        if not os.path.isdir(self.labeledDataFileLocation.text()):
            self.labeledErrorLabel.setText("Error: Directory not found")
            success = False
        else:
            self.labeledErrorLabel.setText("")

        # validate input image type (png or jpg or jpeg)
        # set to lowercase, then check
        self.inputImageFileInput.setText(self.inputImageFileInput.text().lower())
        if not self.inputImageFileInput.text() == "png" or self.inputImageFileInput.text() == "jpg" or self.inputImageFileInput.text () == "jpeg":
            self.inputImageFileTypeErr.setText("Error: invalid file type. File types must be: png, jpg, or jpeg")
            success = False
        else:
            self.inputImageFileTypeErr.setText("")

        # validate output image type (png or jpg or jpeg)
        # set to lowercase, then check
        self.outputImageFileTypeInput.setText(self.outputImageFileTypeInput.text().lower())
        if not self.outputImageFileTypeInput.text() == "png" or self.outputImageFileTypeInput.text() == "jpg" or self.outputImageFileTypeInput.text () == "jpeg":
            self.outputImageFileTypeErr.setText("Error: invalid file type. File types must be: png, jpg, or jpeg")
            success = False
        else:
            self.outputImageFileTypeErr.setText("")

        # validate bias, encoder layers first then decoder layers
        # set to lowercase, check if equal to true or false
        # encoder layers
        # layer 1
        self.EL1biasInput.setText(self.EL1biasInput.text().lower())
        if self.EL1biasInput.text() == "true":
            self.EL1biasInput.setText("True")
            self.EL1biasErr.setText("")
        elif self.EL1biasInput.text() == "false":
            self.EL1biasInput.setText("False")
            self.EL1biasErr.setText("")
        else:
            self.EL1biasErr.setText("Error: Bias should be true or false")


        # layer 2
        self.EL2biasInput.setText(self.EL2biasInput.text().lower())
        if self.EL2biasInput.text() == "true":
            self.EL2biasInput.setText("True")
            self.EL2biasErr.setText("")
        elif self.EL2biasInput.text() == "false":
            self.EL2biasInput.setText("False")
            self.EL2biasErr.setText("")
        else:
            self.EL2biasErr.setText("Error: Bias should be true or false")

        # layer 3
        self.EL3biasInput.setText(self.EL3biasInput.text().lower())
        if self.EL3biasInput.text() == "true":
            self.EL3biasInput.setText("True")
            self.EL3biasErr.setText("")
        elif self.EL3biasInput.text() == "false":
            self.EL3biasInput.setText("False")
            self.EL3biasErr.setText("")
        else:
            self.EL3biasErr.setText("Error: Bias should be true or false")

        # layer 4
        self.EL4biasInput.setText(self.EL4biasInput.text().lower())
        if self.EL4biasInput.text() == "true":
            self.EL4biasInput.setText("True")
            self.EL4biasErr.setText("")
        elif self.EL4biasInput.text() == "false":
            self.EL4biasInput.setText("False")
            self.EL4biasErr.setText("")
        else:
            self.EL4biasErr.setText("Error: Bias should be true or false")


        # layer 5
        self.EL5biasInput.setText(self.EL5biasInput.text().lower())
        if self.EL5biasInput.text() == "true":
            self.EL5biasInput.setText("True")
            self.EL5biasErr.setText("")
        elif self.EL5biasInput.text() == "false":
            self.EL5biasInput.setText("False")
            self.EL5biasErr.setText("")
        else:
            self.EL5biasErr.setText("Error: Bias should be true or false")


        # decoder layers
        # layer 1
        self.DL1biasInput.setText(self.DL1biasInput.text().lower())
        if self.DL1biasInput.text() == "true":
            self.DL1biasInput.setText("True")
            self.DL1biasErr.setText("")
        elif self.DL1biasInput.text() == "false":
            self.DL1biasInput.setText("False")
            self.DL1biasErr.setText("")
        else:
            self.DL1biasErr.setText("Error: Bias should be true or false")


        # layer 2
        self.DL2biasInput.setText(self.DL2biasInput.text().lower())
        if self.DL2biasInput.text() == "true":
            self.DL2biasInput.setText("True")
            self.DL2biasErr.setText("")
        elif self.DL2biasInput.text() == "false":
            self.DL2biasInput.setText("False")
            self.DL2biasErr.setText("")
        else:
            self.DL2biasErr.setText("Error: Bias should be true or false")

        #layer 3
        self.DL3biasInput.setText(self.DL3biasInput.text().lower())
        if self.DL3biasInput.text() == "true":
            self.DL3biasInput.setText("True")
            self.DL3biasErr.setText("")
        elif self.DL3biasInput.text() == "false":
            self.DL3biasInput.setText("False")
            self.DL3biasErr.setText("")
        else:
            self.DL3biasErr.setText("Error: Bias should be true or false")

        #layer 4
        self.DL4biasInput.setText(self.DL4biasInput.text().lower())
        if self.DL4biasInput.text() == "true":
            self.DL4biasInput.setText("True")
            self.DL4biasErr.setText("")
        elif self.DL4biasInput.text() == "false":
            self.DL4biasInput.setText("False")
            self.DL4biasErr.setText("")
        else:
            self.DL4biasErr.setText("Error: Bias should be true or false")


        #layer 5
        self.DL5biasInput.setText(self.DL5biasInput.text().lower())
        if self.DL5biasInput.text() == "true":
            self.DL5biasInput.setText("True")
            self.DL5biasErr.setText("")
        elif self.DL5biasInput.text() == "false":
            self.DL5biasInput.setText("False")
            self.DL5biasErr.setText("")
        else:
            self.DL5biasErr.setText("Error: Bias should be true or false")

        return success




    """
    Function: ValidateDopDowns

    Param: Self - the window object

    Functionality: This function checks all of the drop downs, it selects the only
                    current supported network and support convolution layers/activation functions
                    

    """


    def validateDropDowns(self):

        # network drop down
        if self.networkComboBox.currentText() == "Please Select a Network":
            self.networkErrorLabel.setText("Error: A network must be selected")
        else:
            self.networkErrorLabel.setText("")

        # 1st conv level & activation function

        if self.EL1convLevel_5.currentText() == "Convolution Level":
            self.EL1convLevel_5.setCurrentIndex(3)

        if self.EL1activationFunc_5.currentText() == "Activation Functions":
            self.EL1activationFunc_5.setCurrentIndex(1)

        if self.EL2convLevel.currentText() == "Convolution Level":
            self.EL2convLevel.setCurrentIndex(3)

        if self.EL2activationFunc.currentText() == "Activation Functions":
            self.EL2activationFunc.setCurrentIndex(1)

        if self.EL3convLevel.currentText() == "Convolution Level":
            self.EL3convLevel.setCurrentIndex(3)

        if self.EL3activationFunc.currentText() == "Activation Functions":
            self.EL3activationFunc.setCurrentIndex(1)

        if self.EL4convLevel.currentText() == "Convolution Level":
            self.EL4convLevel.setCurrentIndex(3)

        if self.EL4activationFunc.currentText() == "Activation Functions":
            self.EL4activationFunc.setCurrentIndex(1)

        if self.EL5convLevel.currentText() == "Convolution Level":
            self.EL5convLevel.setCurrentIndex(3)

        if self.EL5activationFunc.currentText() == "Activation Functions":
            self.EL5activationFunc.setCurrentIndex(1)


        if self.EDL1convLevel.currentText() == "Convolution Level":
            self.EDL1convLevel.setCurrentIndex(3)

        if self.DL1activationFunc.currentText() == "Activation Functions":
            self.DL1activationFunc.setCurrentIndex(1)

        if self.DL2convLevel.currentText() == "Convolution Level":
            self.DL2convLevel.setCurrentIndex(3)

        if self.DL2activationFunc.currentText() == "Activation Functions":
            self.DL2activationFunc.setCurrentIndex(1)

        if self.DL3convLevel.currentText() == "Convolution Level":
            self.DL3convLevel.setCurrentIndex(3)

        if self.DL3activationFunc.currentText() == "Activation Functions":
            self.DL3activationFunc.setCurrentIndex(1)

        if self.DL4convLevel.currentText() == "Convolution Level":
            self.DL4convLevel.setCurrentIndex(3)

        if self.DL4activationFunc.currentText() == "Activation Functions":
            self.DL4activationFunc.setCurrentIndex(1)

        if self.DL5convLevel.currentText() == "Convolution Level":
            self.DL5convLevel.setCurrentIndex(3)

        if self.DL5activationFunc.currentText() == "Activation Functions":
            self.DL5activationFunc.setCurrentIndex(1)

    """
    Function: checkNumericVal

    Param:      val - an integer representing the value to be checked
    
                lowerBound - the lower bound of the range val should fall in
                
                upperBound - the higher bound of the range val should fall in
                
    Return:     Boolean - returns true if val is in the range, false if not or incorrect input

    Functionality: This function checks that number entered is existent, a number, and inbetween 
                    higher and lower bound.

    """

    # Checking numerical input, checks 3 things:
    # value isn't balnk, value is a number, and that it is between 2 values (bounds)
    def checkNumericVal(self, val, lowerBound, upperBound):
        if val == "" or not val.isdigit() or int(val) <= lowerBound or int(val) >= upperBound:
            return False
        else:
            return True


    """
    Function: ValidateLogic

    Param: Self - the window object

    Functionality: This function checks the logic of the input, it verifies that the kernel,
                    factor, encoder levels, and decoder levels, all match the depth, if not there 
                    will be errors when running the network.

    """

    def validateLogic(self):

        retVal = True

        # splitting filter config from string --> list
        kernel = self.kernelInput.text().split(",")

        # verifying correct length of kernel, should be = to depth
        if len(kernel) != int(self.depthInput.text()):
            self.kernelErr.setText("Kernel entries should be equal to depth")
            retVal = False
        else:
            self.kernelErr.setText("")

        # same as kernel above
        factor = self.factorInput.text().split(",")
        if len(factor) != int(self.depthInput.text()):
            self.factorErr.setText("Factor entries should be equal to depth")
            retVal = False
        else:
            self.factorErr.setText("")

        encoderLevels = self.encoderLayersInput.text().split(",")
        if len(encoderLevels) != int(self.depthInput.text()):
            retVal = False
            self.encoderLayersErr.setText("Encoder Levels entries should be equal to depth")
        else:
            self.encoderLayersErr.setText("")

        decoderLevels = self.decoderLayersInput.text().split(",")
        if len(decoderLevels) != int(self.depthInput.text()):
            retVal = False
            self.decoderLayersErr.setText("Decoder Levels entries should be equal to depth")
        else:
            self.decoderLayersErr.setText("")

        return retVal
