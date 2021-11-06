from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys
from os.path import expanduser


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('main.ui', self)

        self.show()

    def mybutton_clicked(self):
        my_dir = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "Open a folder",
            expanduser("~"),
            QtWidgets.QFileDialog.ShowDirsOnly
        )
        self.textEdit_3.setText(my_dir)

    def mybutton_clicked2(self):
        my_dir = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "Open a folder",
            expanduser("~"),
            QtWidgets.QFileDialog.ShowDirsOnly
        )
        self.textEdit_4.setText(my_dir)

    def download_mp3(self):
        self.message.setText("Downloading MP3...")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        print(self.message.text())

    def download_mp4(self):
        self.message.setText("Downloading MP4...")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        print(self.message.text())


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
