from time import sleep
from moviepy.editor import VideoFileClip
from sqlite import DataBase
from random import choice


def write(file):
    with open('connect.txt', 'w', encoding='utf8') as f:
        res = list(map(str, count()))
        res.append(str(file))
        f.write('|'.join(res))
        with open('connect2.txt', 'w', encoding='utf8') as f2:
            f2.write('|'.join(res)) # записываем в коннект 2 и пусть от туда проверяет бот
    bd.clear()


def get_lenght(file_num):
    file = f'data/video/{file_num}.mp4'
    clip = VideoFileClip(file)
    return clip.duration


def count():
    with open('connect2.txt', 'w', encoding='utf8') as f:
        f.write('start')

    data = [i[0] for i in bd.get_info()]
    print('data:', data)

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
write(2)
sleep(get_lenght(2))
#вход в кабинет
id = count()[0]
print('id', id)
if id == 1:
    write(4)
    sleep(get_lenght(4))
    print('привет')
elif id == 2:
    write(3)
    sleep(get_lenght(3))
    print('здарова бандиты')
elif id == 3:
    write(5)
    sleep(get_lenght(5))
    print('я вернулся с результатом')
#разговор с алонзо
id = count()[0]
print('id', id)
if id == 1:
    write(6)
    sleep(get_lenght(6))
    print('как у вас дела?')
    id = count()[0]
    if id == 1:
        write(8)
        sleep(get_lenght(8))
        print('промолчать')
    elif id == 2:
        write(10)
        sleep(get_lenght(10))
        print('тогда продолжу')
        id = count()[0]
        if id == 1:
            write(11)
            sleep(get_lenght(11))
            print('так можно было чтоли')
        elif id == 2:
            write(12)
            sleep(get_lenght(12))
            print('почему же')
elif id == 2:
    write(7)
    sleep(get_lenght(7))
    print('зачем вам эти документы?')
    id = count()[0]
    if id == 1:
        write(11)
        sleep(get_lenght(11))
        print('так можно было чтоли')
    elif id == 2:
        write(12)
        sleep(get_lenght(12))
        print('почему же')
# спустя пару дней
write(14)
sleep(get_lenght(14))
id = count()[0]
if id == 1:
    write(16)
    sleep(get_lenght(16))
    print('можно маме позвонить?')
elif id == 2:
    write(15)
    sleep(get_lenght(15))
    print('так точно')
elif id == 3:
    write(17)
    sleep(get_lenght(17))
    print('оружие будет?')
# заброшка
write(18)
sleep(get_lenght(18))
id = count()[0]
if id == 1:
    write(19)
    sleep(get_lenght(19))
    print('стоять')
elif id == 2:
    write(20)
    sleep(get_lenght(20))
    print('бежать')
'''struct
id = count()[0]
if id == 1:
    write(n)
    sleep(get_lenght(n))
    print('')
elif id == 2:
    write(n)
    sleep(get_lenght(n))
    print('')
elif id == 3:
    write(n)
    sleep(get_lenght(n))
    print('')
'''