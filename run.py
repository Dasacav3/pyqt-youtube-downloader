from multiprocessing import Process, cpu_count
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys
from os.path import expanduser
from yt_dl import *


class UI(QMainWindow, YT_Downloader):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('gui.ui', self)

        self.setWindowIcon(QtGui.QIcon('logo.png'))
        
        self.youtube_dl = YT_Downloader()

        self.directory = ""

        self.show()

    def chooseDirectory(self):
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(
            self,
            "Open a folder",
            expanduser("~"),
            QtWidgets.QFileDialog.ShowDirsOnly
        )
        self.directoryText.setText(self.directory)

    def downloadFile(self):
        self.message.setText("Downloading File")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        url = self.urlText.toPlainText()
        path = self.directory + "/"
        format = self.formatSelect.currentText()
        print(format)

        try:
            if format == "mp3":
                self.youtube_dl.download_mp3(url, path)
            elif format == "mp4":
                self.youtube_dl.download_mp4(url, path)
            elif format == "aac":
                self.youtube_dl.download_aac(url, path)
            elif format == "webm":
                self.youtube_dl.download_webm(url, path)
            elif format == "ogg":
                self.youtube_dl.download_ogg(url, path)
            elif format == "m4a":
                self.youtube_dl.download_m4a(url, path)
        except:
            print("Error downloading file")
        finally:
            self.message.setText("Download Complete")


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
