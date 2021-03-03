from time import sleep
from moviepy.editor import VideoFileClip
from sqlite import DataBase
from random import choice


def write(file):
    with open('connect.txt', 'w', encoding='utf8') as f:
        res = list(map(str, count()))
        res.append(str(file))
        f.write('|'.join(res))


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
            return inf.index(max(inf)) + 1, inf[0], inf[1], inf[2]
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

# id = count()
id = 1
if id == 1:
    write(2)
    sleep(get_lenght(2))
    print('бежим направо')
elif id == 2:
    print('бежим налево')
id = 2
if id == 1:
    print('бежим направо')
elif id == 2:
    write(5)
    sleep(get_lenght(5))
    print('бежим налево')