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
        '''
        # ТЕКСТ
        self.label = QLabel(self)
        self.label.setText("Шоу начинается")
        self.resize(199, 200)
        # ГОЛОСОВАНИЕ
        self.var_1 = QLabel(self)
        self.var_1.setText("")
        self.var_1.setStyleSheet("QLabel {color : white; }")
        self.var_1.move(100, 100)
        self.var_2 = QLabel(self)
        self.var_2.setText("")
        self.var_2.setStyleSheet("QLabel {color : white; }")
        self.var_2.move(200, 100)
        self.var_3 = QLabel(self)
        self.var_3.setText("")
        self.var_3.setStyleSheet("QLabel {color : white; }")
        self.var_3.move(300, 100)
        '''
    def check(self):
        with open('connect.txt', 'r', encoding='utf8') as f:
            text = [str(i) for i in f.read().split('|')]

        if text[-1]:
            fileName = get_path(int(text[-1]))
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.mediaPlayer.play()
        '''
        if text[0] == 1:
            self.label.setText('Победил первый вариант.')
            if text[1]:
                self.var_1.setText(text[1])
            if text[2]:
                self.var_2.setText(text[2])
            if text[3]:
                self.var_3.setText(text[3])

        if text[0] == 2:
            self.label.setText('Победил второй вариант.')
            if text[1]:
                self.var_1.setText(text[1])
            if text[2]:
                self.var_2.setText(text[2])
            if text[3]:
                self.var_3.setText(text[3])

        if text[0] == 3:
            self.label.setText('Победил третий вариант.')
            if text[1]:
                self.var_1.setText(text[1])
            if text[2]:
                self.var_2.setText(text[2])
            if text[3]:
                self.var_3.setText(text[3])
        '''
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
    # file = f'data/video/{file_num}.mp4'
    file = f'/Volumes/Untitled/video/{file_num}.mp4'
    clip = VideoFileClip(file)
    return clip.duration


# получаем путь
def get_path(file_num):
    # file = os.path.dirname(os.path.abspath(f'{file_num}.mp4'))
    # return f'{file}/data/video/{file_num}.mp4'
    return f'/Volumes/Untitled/video/{file_num}.mp4'


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.setWindowTitle("Player")
    player.resize(600, 400)
    player.show()
    player.check()
    sys.exit(app.exec_())
