from time import sleep
from moviepy.editor import VideoFileClip


def get_lenght(file_num):
    file = f'video/{file_num}.mp4'
    clip = VideoFileClip(file)
    return clip.duration

print('ha-ha')
sleep(get_lenght(2))
print('ha')

'''
мусорка
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
        
    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
            
            
            #self.abrir('/Users/alekseyostrovskiy/Desktop/film/data/video/2.mp4')
        #self.abrir('/Users/alekseyostrovskiy/Desktop/film/data/video/1.mp4')
        
                # self.timer=QTimer()
        # self.timer.timeout.connect(self.showTime)
    
    #   def abrir(self, file):
#       fileName = file

#      if fileName != '':
#          self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))  # путь до файла
#          self.videoWidget.show()
#          self.mediaPlayer.play()

 #   def make_scene(self, file_num):
 #       file = os.path.dirname(os.path.abspath(f'{file_num}.mp4'))
 #       self.abrir(f'{file}/data/video/{file_num}.mp4')
'''