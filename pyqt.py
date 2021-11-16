from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys
from os.path import expanduser
from yt_dl import *


class UI(QMainWindow, YT_Downloader):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('main.ui', self)

        self.youtube_dl = YT_Downloader()

        self.dir_mp3 = ""
        self.dir_mp4 = ""

        self.show()

    def mybutton_clicked(self):
        self.dir_mp3 = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "Open a folder",
            expanduser("~"),
            QtWidgets.QFileDialog.ShowDirsOnly
        )
        self.textEdit_3.setText(self.dir_mp3)
        self.youtube_dl.url = self.dir_mp3

    def mybutton_clicked2(self):
        self.dir_mp4 = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "Open a folder",
            expanduser("~"),
            QtWidgets.QFileDialog.ShowDirsOnly
        )
        self.textEdit_4.setText(self.dir_mp4)
        self.youtube_dl.url = self.dir_mp3

    def download_mp3(self):
        self.message.setText("Downloading MP3...")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        url = self.textEdit.toPlainText()
        path = self.dir_mp3
        self.youtube_dl.download_mp3(url, path)

    def download_mp4(self):
        self.message.setText("Downloading MP4...")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        url = self.textEdit.toPlainText()
        path = self.dir_mp4
        self.youtube_dl.download_mp4(url, path)


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
