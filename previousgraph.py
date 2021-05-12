from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import sys
from random import randint
from superimpose import SuperImpose
from test import TestingWindow
from functools import partial

class PreviousGraph(object):

    def __init__(self):
        self.superImpose = SuperImpose()
        self.image1_path = ''
        self.image2_path = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(520, 400)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("QMainWindow {background: #99AAB5;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ####################
        self.goToTestingButton = QtWidgets.QPushButton(self.centralwidget)
        self.goToTestingButton.setGeometry(QtCore.QRect(1095, 460, 113, 32))
        self.goToTestingButton.setObjectName("gototesting")
        ############################
        self.goToTestingButton.clicked.connect(partial(self.go_to_testing_window, MainWindow))

        # Graph container
        self.graphWidget = PlotWidget(self.centralwidget)
        self.graphWidget.setGeometry(QtCore.QRect(10, 10, 500, 350))
        self.graphWidget.setObjectName("graphWidget")

        # Setting axis labels
        self.graphWidget.setLabel('left', 'Loss')
        self.graphWidget.setLabel('bottom', 'Epoch')

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
        #self.timer = QtCore.QTimer()
        #self.timer.setInterval(500)
        #self.timer.timeout.connect(self.update_plot_data)
        #self.timer.start()

        #
        self.file1Button = QtWidgets.QPushButton(self.centralwidget)
        self.file1Button.setGeometry(QtCore.QRect(1095, 435, 113, 32))
        self.file1Button.setObjectName("file1Button")

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
        MainWindow.setWindowTitle(_translate("MainWindow", "Previous Graph"))
        self.label.setText(_translate("MainWindow", "Loss vs Epoch"))
        self.file1Button.setText(_translate("MainWindow", "Compare"))
        self.goToTestingButton.setText(_translate("MainWindow", "Testing"))

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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = PreviousGraph()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
