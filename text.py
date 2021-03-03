from time import sleep
from moviepy.editor import VideoFileClip
from sqlite import DataBase
from random import choice


def write(file):
    with open('connect.txt', 'w', encoding='utf8') as f:
        f.write(file)


def get_lenght(file_num):
    file = f'data/video/{file_num}.mp4'
    clip = VideoFileClip(file)
    return clip.duration


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


bd = DataBase('data/user.db')

print('идёт фильм')
write(1)
print('выбор')
sleep(get_lenght(1))

id = count()

if id == 1:
    write(2)
    sleep(get_lenght(2))
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