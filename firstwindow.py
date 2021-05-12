from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QFileDialog

from MainWindow import Ui_MainWindow
import sys


class FileWindow(object):
    def __init__(self):
        self.file1 = None
        self.file2 = None
        self.file3 = None

    def go_to_parameter_window(self):
        """
        Opens the Parameter window when passed to button event
        :return: None
        """
        self.parameter_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.parameter_window, self.file2, self.file3)
        MainWindow.close()
        self.parameter_window.show()

    def open_file_explorer(self):
        """
        Opens file directory and returns the FILE path selected.
        :return: string
        """
        file_name = QFileDialog.getOpenFileName()
        if file_name:
            return file_name
        return

    def open_folder_explorer(self):
        """
        Opens the file directory and returns the FOLDER path selected.
        :return:
        """
        folderName = QFileDialog.getExistingDirectory()
        if folderName:
            return folderName
        return

    def open_file_1(self):
        """
        Sets the file1 object (Network) and sets the location to file1.
        Manipulates the visuals and button on the window
        :return:
        """
        self.file1 = self.open_file_explorer()
        if self.file1 and self.file2 and self.file3:
            self.pushButton.setEnabled(True)
        if self.file1:
            self.GroupBox.setStyleSheet("QGroupBox {background: green;}")

    def open_file_2(self):
        """
        Sets the file1 object (Training Data) and sets the location to file1.
        Manipulates the visuals and button on the window
        :return:
        """
        self.file2 = self.open_folder_explorer()
        if self.file1 and self.file2 and self.file3:
            self.pushButton.setEnabled(True)
        if self.file2:
            self.GroupBox_2.setStyleSheet("QGroupBox {background: green;}")

    def open_file_3(self):
        """
        Sets the file1 object (Labeled Data) and sets the location to file1.
        Manipulates the visuals and button on the window
        :return:
        """
        self.file3 = self.open_folder_explorer()
        if self.file1 and self.file2 and self.file3:
            self.pushButton.setEnabled(True)
        if self.file3:
            self.GroupBox_3.setStyleSheet("QGroupBox {background: green;}")

    def setupUi(self, MainWindow):
        """
        Setups all of the UI and controls for the file buttons as well as the original
        colors for the square indicators.
        :param MainWindow:
        :return:
        """
        # Main window container
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 602)
        MainWindow.setFixedSize(808, 602)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Open network file
        self.GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.GroupBox.setGeometry(QtCore.QRect(130, 190, 170, 80))
        self.GroupBox.setObjectName("GroupBox")
        self.GroupBox.setStyleSheet("QGroupBox {background: red;}")

        # Open training data file
        self.GroupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.GroupBox_2.setGeometry(QtCore.QRect(330, 190, 170, 80))
        self.GroupBox_2.setObjectName("GroupBox_2")
        self.GroupBox_2.setStyleSheet("QGroupBox {background: red;}")

        # open key data file
        self.GroupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.GroupBox_3.setGeometry(QtCore.QRect(530, 190, 170, 80))
        self.GroupBox_3.setObjectName("GroupBox_3")
        self.GroupBox_3.setStyleSheet("QGroupBox {background: red;}")

        # Open network button
        self.file1Button = QtWidgets.QPushButton(self.centralwidget)
        self.file1Button.setGeometry(QtCore.QRect(130, 270, 170, 32))
        self.file1Button.setObjectName("file1Button")

        # Open training data button
        self.file2Button = QtWidgets.QPushButton(self.centralwidget)
        self.file2Button.setGeometry(QtCore.QRect(330, 270, 170, 32))
        self.file2Button.setObjectName("file2Button")

        # Open key data button
        self.file3Button = QtWidgets.QPushButton(self.centralwidget)
        self.file3Button.setGeometry(QtCore.QRect(530, 270, 170, 32))
        self.file3Button.setObjectName("file3Button")

        # Next button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 400, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setEnabled(False)

        MainWindow.setCentralWidget(self.centralwidget)

        # Menu at top of screen
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 808, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # Status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Opens parameter window on next button
        self.pushButton.clicked.connect(self.go_to_parameter_window)

        # Open file buttons
        self.file1Button.clicked.connect(self.open_file_1)
        self.file2Button.clicked.connect(self.open_file_2)
        self.file3Button.clicked.connect(self.open_file_3)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        # Set titles boxes
        #self.GroupBox.setTitle(_translate("MainWindow", "Choose Network"))
        #self.GroupBox_2.setTitle(_translate("MainWindow", "Choose Input Images"))
        #self.GroupBox_3.setTitle(_translate("MainWindow", "Choose Key Images"))

        # Set titles buttons
        self.pushButton.setText(_translate("MainWindow", "Next"))
        self.file1Button.setText(_translate("MainWindow", "Choose Network"))
        self.file2Button.setText(_translate("MainWindow", "Training Data"))
        self.file3Button.setText(_translate("MainWindow", "Labeled Data"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FileWindow()
    ui.setupUi(MainWindow)
    MainWindow.setStyleSheet("QMainWindow {background: #2C2F33;}")
    MainWindow.show()
    sys.exit(app.exec_())