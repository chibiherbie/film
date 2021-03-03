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
# def check_comand():
#     while True:
#         with open('connect.txt', 'r', encoding='utf8') as f:
#             text = [str(i) for i in f.read().split('|')]
#
#         if text[0] == 'main':
#             open('text.txt', 'w').close()
#             break
#         sleep(1)
#
#         return int(text[1])
counter = 0

bd = DataBase('data/user.db')


class VideoPlayer(QWidget):
    def __init__(self, parent=None):
        super(VideoPlayer, self).__init__(parent)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        self.videoWidget = QVideoWidget()

        # self.timer=QTimer()
        # self.timer.timeout.connect(self.showTime)
        #самое главное!

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)

        layout = QVBoxLayout()
        layout.addWidget(self.videoWidget)
        layout.addLayout(controlLayout)

        self.setLayout(layout)

        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.error.connect(self.handleError)

        # ТАЙМЕР
        self.timer = QTimer()
        self.timer.timeout.connect(self.check)
        self.timer.start(1000)

        #self.abrir('/Users/alekseyostrovskiy/Desktop/film/data/video/2.mp4')
        #self.abrir('/Users/alekseyostrovskiy/Desktop/film/data/video/1.mp4')

    def check(self):
        with open('connect.txt', 'r', encoding='utf8') as f:
            text = f.read()  # [str(i) for i in f.read().split('|')]

        if text:
            fileName = get_path(2)
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.mediaPlayer.play()

        with open('connect.txt', 'w', encoding='utf8') as f:
            f.write('')

    def abrir(self, file):
        fileName = file

        if fileName != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))# путь до файла
            self.videoWidget.show()
            self.mediaPlayer.play()
    '''
    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
    '''

    def handleError(self):
        print("Error: " + self.mediaPlayer.errorString())

    def make_scene(self, file_num):
        file = os.path.dirname(os.path.abspath(f'{file_num}.mp4'))
        self.abrir(f'{file}/data/video/{file_num}.mp4')

    def base(self):
        print('идёт фильм')
        print('выбор')
        # id = count()
        id = 2
        if id == 1:
            self.make_scene(1)
            duration = get_lenght(1)
            make_pause(duration)
            print('бежим направо')
        elif id == 2:
            fileName = get_path(2)
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.mediaPlayer.play()
            # self.make_scene(2)
            # self.abrir('/Users/alekseyostrovskiy/Desktop/film/data/video/2.mp4')
            duration = get_lenght(2)
            make_pause(3)
            print('бежим налево')
        id = 1
        if id == 1:
            fileName = get_path(5)
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.mediaPlayer.play()
            # self.make_scene(5)
            duration = get_lenght(5)
            make_pause(3)
            self.make_scene(2)
            print('бежим направо')
        elif id == 2:
            self.make_scene(2)
            duration = get_lenght(2)
            make_pause(3)
            print('бежим налево')


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
# мутим паузу


def make_pause(duration):
    sleep(duration)


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
    # player.base()
    sys.exit(app.exec_())
