from time import sleep
from sqlite import DataBase
from random import choice
from moviepy.editor import VideoFileClip

from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QDir, Qt, QUrl, QSize, QTimer
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
                             QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar)
import os

bd = DataBase('data/user.db')


class VideoPlayer(QWidget):
    def __init__(self, parent=None):
        super(VideoPlayer, self).__init__(parent)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget()

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        layout = QVBoxLayout()
        layout.addWidget(self.videoWidget)
        layout.addLayout(controlLayout)
        self.setLayout(layout)
        # ПЛЕЕР
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.error.connect(self.handleError)
        # ТАЙМЕР
        self.timer = QTimer()
        self.timer.timeout.connect(self.check)
        self.timer.start(1000)

    def check(self):
        with open('connect.txt', 'r', encoding='utf8') as f:
            text = f.read()  # [str(i) for i in f.read().split('|')]

        if text:
            fileName = get_path(int(text))
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.mediaPlayer.play()

        with open('connect.txt', 'w', encoding='utf8') as f:
            f.write('')

    def handleError(self):
        print("Error: " + self.mediaPlayer.errorString())


# считаем ответы
def count():
    data = [i[0] for i in bd.get_info()]
    bd.clear()

    inf = [data.count(1), data.count(2), data.count(3)]

    while True:
        if inf.count(max(inf)) != 2:
            return inf.index(max(inf)) + 1
        else:
            inf_c = inf.copy()
            a = inf.index(max(inf))
            inf_c[a] = 0  # обнуляем одно макс знач у копии, чтобы потом найти индекс второго макс знач

            # делаем +1 на одно из макс знач
            inf[choice([a, inf_c.index(max(inf_c))])] += 1


# узнаем длительность
def get_lenght(file_num):
    file = f'data/video/{file_num}.mp4'
    clip = VideoFileClip(file)
    return clip.duration


# получаем путь
def get_path(file_num):
    file = os.path.dirname(os.path.abspath(f'{file_num}.mp4'))
    return f'{file}/data/video/{file_num}.mp4'


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.setWindowTitle("Player")
    player.resize(600, 400)
    player.show()
    player.check()
    sys.exit(app.exec_())
