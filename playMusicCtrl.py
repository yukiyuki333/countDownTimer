from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
import sys,os
from PyQt5.QtCore import QUrl
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication


class PlayMusicCtrl(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.musicPlayer = QMediaPlayer()
        self.musicPlayer.setVolume(100)
        bgm_path = os.getcwd() + '/'
        musicContent = QMediaContent(QUrl.fromLocalFile(bgm_path + 'bgm.mp3'))
        self.musicPlayer.setMedia(musicContent)

    def playMusic(self):
        self.musicPlayer.play()
        #print(self.musicPlayer.state())

    def stopMusic(self):
        self.musicPlayer.pause()
        #print(self.musicPlayer.state())
        self.musicPlayer.setPosition(0)
