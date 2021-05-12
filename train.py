from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import sys
from random import randint
from superimpose import SuperImpose
from layerSuperimpose import SuperImposeLayers
from test import TestingWindow
from functools import partial
from previousgraph import PreviousGraph

# RGB Colors to  Find
blackRGB = [0, 0, 0]
whiteRGB = [255, 255, 255]
# RGBA Values to Replace
transparentRGBA = (0, 0, 0, 0)
redRGBA = (255, 0, 0, 255)
blueRGBA = (0, 0, 255, 255)
greenRGBA = (0, 255, 0, 255)
yellowRGBA = (255, 255, 0, 255)
blackRGBA = (0, 0, 0, 255)

class TrainingWindow(object):

    def __init__(self):
        self.superImpose = SuperImpose()
        self.layersuperImpose = SuperImposeLayers()
        self.image1_path = ''
        self.image2_path = ''
        self.superimpose_path = ''
        self.label_path = ''
        self.final_label = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 550)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("QMainWindow {background: #99AAB5;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        myFont = QtGui.QFont()
        myFont.setBold(True)

        self.image1Labellabel = QtWidgets.QLabel(self.centralwidget)
        self.image1Labellabel.setGeometry(QtCore.QRect(110, 173, 251, 191))
        self.image1Labellabel.setObjectName("image1Labellabel")
        self.image1Labellabel.setFont(myFont)

        self.image1Label = QtWidgets.QLabel(self.centralwidget)
        self.image1Label.setGeometry(QtCore.QRect(110, 280, 251, 191))
        self.image1Label.setFrameShape(QtWidgets.QFrame.Box)
        self.image1Label.setText("Image First Layer")
        self.image1Label.setPixmap(QtGui.QPixmap())
        self.image1Label.setScaledContents(True)
        self.image1Label.setObjectName("image1Label")

        self.image2Labellabel = QtWidgets.QLabel(self.centralwidget)
        self.image2Labellabel.setGeometry(QtCore.QRect(400, 173, 251, 191))
        self.image2Labellabel.setObjectName("image2Labellabel")
        self.image2Labellabel.setFont(myFont)


        self.image2Label = QtWidgets.QLabel(self.centralwidget)
        self.image2Label.setGeometry(QtCore.QRect(400, 280, 251, 191))
        self.image2Label.setFrameShape(QtWidgets.QFrame.Box)
        self.image2Label.setText("Image Second Layer")
        self.image2Label.setPixmap(QtGui.QPixmap())
        self.image2Label.setScaledContents(True)
        self.image2Label.setObjectName("image2Label")

        self.inputImgLabellabel = QtWidgets.QLabel(self.centralwidget)
        self.inputImgLabellabel.setGeometry(QtCore.QRect(110, 7, 100, 16))
        self.inputImgLabellabel.setObjectName("inputImgLabellabel")
        self.inputImgLabellabel.setFont(myFont)

        self.inputImgLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputImgLabel.setGeometry(QtCore.QRect(110, 25, 251, 191))
        self.inputImgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.inputImgLabel.setText("Input Image")
        self.inputImgLabel.setPixmap(QtGui.QPixmap())
        self.inputImgLabel.setScaledContents(True)
        self.inputImgLabel.setObjectName("inputImgLabel")

        self.outputImgLabellabel = QtWidgets.QLabel(self.centralwidget)
        self.outputImgLabellabel.setGeometry(QtCore.QRect(400, 7, 200, 16))
        self.outputImgLabellabel.setObjectName("outputImgLabellabel")
        self.outputImgLabellabel.setFont(myFont)

        self.outputImgLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputImgLabel.setGeometry(QtCore.QRect(400, 25, 251, 191))
        self.outputImgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputImgLabel.setWindowTitle("Input Superimposed with Label")
        self.outputImgLabel.setText("Input Superimposed with Label")
        self.outputImgLabel.setPixmap(QtGui.QPixmap())
        self.outputImgLabel.setScaledContents(True)
        self.outputImgLabel.setObjectName("inputImgLabel")

        self.intoutImgLabellabel = QtWidgets.QLabel(self.centralwidget)
        self.intoutImgLabellabel.setGeometry(QtCore.QRect(680, 7, 200, 16))
        self.intoutImgLabellabel.setObjectName("intoutImgLabellabel")
        self.intoutImgLabellabel.setFont(myFont)

        self.intoutImgLabel = QtWidgets.QLabel(self.centralwidget)
        self.intoutImgLabel.setGeometry(QtCore.QRect(680, 25, 251, 191))
        self.intoutImgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.intoutImgLabel.setText("Label Created Superimposed")
        self.intoutImgLabel.setPixmap(QtGui.QPixmap())
        self.intoutImgLabel.setScaledContents(True)
        self.intoutImgLabel.setObjectName("inoutImgLabel")

        self.superimposeLabellabel = QtWidgets.QLabel(self.centralwidget)
        self.superimposeLabellabel.setGeometry(QtCore.QRect(680, 173, 251, 191))
        self.superimposeLabellabel.setObjectName("superimposeLabellabel")
        self.superimposeLabellabel.setFont(myFont)

        self.superimposeLabel = QtWidgets.QLabel(self.centralwidget)
        self.superimposeLabel.setGeometry(QtCore.QRect(680, 280, 251, 191))
        self.superimposeLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.superimposeLabel.setText("Image Layers Superimposed")
        self.superimposeLabel.setPixmap(QtGui.QPixmap())
        self.superimposeLabel.setScaledContents(True)
        self.superimposeLabel.setObjectName("superimposeLabel")

        self.image1Text = QtWidgets.QLineEdit(self.centralwidget)
        self.image1Text.setGeometry(QtCore.QRect(120, 480, 113, 32))
        self.image1Text.setAlignment(QtCore.Qt.AlignCenter)
        self.image1Text.setObjectName("image1Text")

        self.loadLayer1Text = QtWidgets.QLineEdit(self.centralwidget)
        self.loadLayer1Text.setGeometry(QtCore.QRect(240, 480, 113, 32))
        self.loadLayer1Text.setAlignment(QtCore.Qt.AlignCenter)
        self.loadLayer1Text.setObjectName("Layer")

        self.loadLayer2Text = QtWidgets.QLineEdit(self.centralwidget)
        self.loadLayer2Text.setGeometry(QtCore.QRect(470, 480, 113, 32))
        self.loadLayer2Text.setAlignment(QtCore.Qt.AlignCenter)
        self.loadLayer2Text.setObjectName("Layer2")

        ####################
        self.inoutImgText = QtWidgets.QLineEdit(self.centralwidget)
        self.inoutImgText.setGeometry(QtCore.QRect(175, 220, 113, 32))
        self.inoutImgText.setAlignment(QtCore.Qt.AlignCenter)
        self.inoutImgText.setObjectName("Image Num")

        ####################
        self.loadImagesButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadImagesButton.setGeometry(QtCore.QRect(755, 480, 110, 34))
        self.loadImagesButton.setObjectName("loadImagesButton")
        ############################
        self.loadImagesButton.clicked.connect(self.ImageLoad)
        #########################

        ####################
        self.InOutButton = QtWidgets.QPushButton(self.centralwidget)
        self.InOutButton.setGeometry(QtCore.QRect(465, 220, 120, 34))
        self.InOutButton.setObjectName("loadImagesButton")
        ############################
        self.InOutButton.clicked.connect(self.InOutLoad)

        # Set up testing button
        self.goToTestingButton = QtWidgets.QPushButton(self.centralwidget)
        self.goToTestingButton.setGeometry(QtCore.QRect(1095, 470, 113, 32))
        self.goToTestingButton.setObjectName("gototesting")
        self.goToTestingButton.clicked.connect(partial(self.go_to_testing_window, MainWindow))

        # Graph container
        self.graphWidget = PlotWidget(self.centralwidget)
        self.graphWidget.setGeometry(QtCore.QRect(960, 120, 421, 311))
        self.graphWidget.setObjectName("graphWidget")

        # Setting axis labels
        self.graphWidget.setLabel('left', 'Loss')
        self.graphWidget.setLabel('bottom', 'Epoch')

        # Creating legend for plot
        #self.graphWidget.addLegend()
        #self.graphWidget.legend.addItem(self.data_line, 'curv1')

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1125, 100, 91, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        # Menu bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # Status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Setting data points
        self.x = list(range(100))  # 100 time points
        self.y = [randint(0, 100) for _ in range(100)]  # 100 data points

        # Styling for graph
        self.graphWidget.setBackground('w')
        pen = pg.mkPen(color=(0, 0, 0))
        self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen)

        # Set time for updating intervals
        self.timer = QtCore.QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

        # Set previous loss vs epoch button
        self.previous_data_button = QtWidgets.QPushButton(self.centralwidget)
        self.previous_data_button.setGeometry(QtCore.QRect(1095, 435, 113, 32))
        self.previous_data_button.setObjectName("file1Button")
        self.previous_data_button.clicked.connect(self.open_previous_graph)

        # Set up menu and status bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1015, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Training"))
        self.image1Text.setPlaceholderText(_translate("MainWindow", "Image"))
        self.inoutImgText.setPlaceholderText(_translate("MainWindow", "Image"))
        self.loadLayer1Text.setPlaceholderText(_translate("MainWindow", "Layer"))
        self.loadLayer2Text.setPlaceholderText(_translate("MainWindow", "Layer"))
        self.loadImagesButton.setText(_translate("MainWindow", "Load Images"))
        self.InOutButton.setText(_translate("MainWindow", "Input | Output"))
        self.label.setText(_translate("MainWindow", "Loss vs Epoch"))
        self.previous_data_button.setText(_translate("MainWindow", "Previous Data"))
        self.goToTestingButton.setText(_translate("MainWindow", "Testing"))
        self.image1Labellabel.setText(_translate("MainWindow", "Image Layer 1"))
        self.image2Labellabel.setText(_translate("MainWindow", "Image Layer 2 "))
        self.superimposeLabellabel.setText(_translate("MainWindow", "Superimpose Layers"))
        self.inputImgLabellabel.setText(_translate("MainWindow", "Input Image"))
        self.outputImgLabellabel.setText(_translate("MainWindow", "Label Superimposed"))
        self.intoutImgLabellabel.setText(_translate("MainWindow", "Network Label Superimposed"))

    def ImageLoad(self):
        self.image1_path = "Deep Network Visualization/train/label_majorcrack/" + self.image1Text.text() + ".bmp"
        self.image2_path = "Deep Network Visualization/train/label_majorcrack/" + self.image1Text.text() + "_1.bmp"
        self.final_label = "Superimpose Layer Images/" + self.image1Text.text() + ".PNG"
        self.image1Label.setPixmap(QtGui.QPixmap(self.image1_path))
        self.image2Label.setPixmap(QtGui.QPixmap(self.image2_path))
        self.layersuperImpose.super_impose_img(self.image2_path, self.image1_path, self.image1Text.text(), redRGBA)
        self.superimposeLabel.setPixmap(QtGui.QPixmap(self.final_label))

    def InOutLoad(self):
        self.image1_path = "Deep Network Visualization/train/original/" + self.inoutImgText.text() + ".JPG"
        self.image2_path = "Deep Network Visualization/train/label_majorcrack/" + self.inoutImgText.text() + ".bmp"
        self.superimpose_path = "Superimpose Inout Images/" + self.inoutImgText.text() + ".PNG"
        self.label_path = "Deep Network Visualization/train/label_majorcrack/" + self.inoutImgText.text() + "_1.bmp"
        self.final_label = "Superimpose Inout Images/" + self.inoutImgText.text() + "_1.PNG"
        self.inputImgLabel.setPixmap(QtGui.QPixmap(self.image1_path))
        self.superImpose.super_impose_img(self.image2_path, self.image1_path, self.inoutImgText.text(), greenRGBA)
        self.outputImgLabel.setPixmap(QtGui.QPixmap(self.superimpose_path))
        self.superImpose.super_impose_img(self.label_path, self.superimpose_path, self.inoutImgText.text() + "_1", redRGBA)
        self.intoutImgLabel.setPixmap(QtGui.QPixmap(self.final_label))

    def update_plot_data(self):
        """
        Updates loss vs epoch graph on a set interval.
        :return: None
        """
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
        self.y = self.y[1:]  # Remove the first
        self.y.append(randint(0, 100))  # Add a new random value.
        self.data_line.setData(self.x, self.y)  # Update the data.

    def go_to_testing_window(self, window):
        """
        Opens the Testing window when passed to button event
        :return: None
        """
        self.testing_window = QtWidgets.QMainWindow()
        self.ui = TestingWindow()
        self.ui.setupUi(self.testing_window)
        window.close()
        self.testing_window.show()

    def open_previous_graph(self):
        """
        Opens previously saved data for loss vs epoch
        :return: None
        """
        self.previous_graph = QtWidgets.QMainWindow()
        self.ui = PreviousGraph()
        self.ui.setupUi(self.previous_graph)
        self.previous_graph.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TrainingWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
