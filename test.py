from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl, QTimer
from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
import sys


class VideoPlayer:

    def __init__(self):
        self.video = QVideoWidget()
        self.video.resize(300, 300)
        self.video.move(0, 0)
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.video)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("D:/FILM/film/data/video/2.mp4")))

        self.timer = QTimer()
        self.timer.timeout.connect(self.check)
        self.timer.start(1000)

    def callback(self):
        self.player.setPosition(0)  # to start at the beginning of the video every time
        self.video.show()
        self.player.play()

    def check(self):
        print('DADA')
t = [1, 2, 3, 4]
res = list(map(str, t))
res.append(str(5))
print('|'.join(res))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    v = VideoPlayer()
    b = QPushButton('start')
    b.clicked.connect(v.callback)
    b.show()
    sys.exit(app.exec_())