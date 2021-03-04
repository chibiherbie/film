from time import sleep
from moviepy.editor import VideoFileClip
from sqlite import DataBase
from random import choice
from main import get_lenght


def write(file):
    with open('connect.txt', 'w', encoding='utf8') as f:
        res = list(map(str, count()))
        res.append(str(file))
        f.write('|'.join(res))
        print(res)
        if res[1] != '0' or res[2] != '0' or res[3] != '0':
            with open('connect2.txt', 'w', encoding='utf8') as f2:
                f2.write('|'.join(res))  # записываем в коннект 2 и пусть от туда проверяет бот
        else:
            bd.clear()
'''
def get_lenght(file_num):
    file = f'data/video/{file_num}.mp4'
    clip = VideoFileClip(file)
    return clip.duration
'''

def count():
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
sleep(get_lenght(1))
print('начало')
write(2)
sleep(get_lenght(2))
print('поездка')
# забираем документы
id = count()[0]
if id == 1:
    write(3)
    sleep(get_lenght(3))
    print('трек 1')
elif id == 2:
    write(4)
    sleep(get_lenght(4))
    print('трек 2')
elif id == 3:
    write(5)
    sleep(get_lenght(5))
    print('трек 3')
# берем документы
write(6)
sleep(get_lenght(6))
print('документы забраны')
# входим в на базу
write(7)
sleep(get_lenght(7))
print('знакомимся')
#вход в кабинет босса
id = count()[0]
print('id', id)
if id == 1:
    write(9)
    sleep(get_lenght(9))
    print('привет')
elif id == 2:
    write(8)
    sleep(get_lenght(8))
    print('здарова бандиты')
elif id == 3:
    write(10)
    sleep(get_lenght(10))
    print('я вернулся с результатом')
#разговор с алонзо
id = count()[0]
print('id', id)
if id == 1:
    write(11)
    sleep(get_lenght(11))
    print('как у вас дела?')
    id = count()[0]
    if id == 1:
        write(12)
        sleep(get_lenght(12))
        print('промолчать')
    elif id == 2:
        write(14)
        sleep(get_lenght(14))
        print('тогда продолжу')
        id = count()[0]
        if id == 1:
            write(15)
            sleep(get_lenght(15))
            print('так можно было чтоли')
        elif id == 2:
            write(16)
            sleep(get_lenght(16))
            print('почему же')
elif id == 2:
    write(13)
    sleep(get_lenght(13))
    print('зачем вам эти документы?')
    id = count()[0]
    if id == 1:
        write(15)
        sleep(get_lenght(15))
        print('так можно было чтоли')
    elif id == 2:
        write(16)
        sleep(get_lenght(16))
        print('почему же')
# спустя пару дней
write(17)
sleep(get_lenght(17))
id = count()[0]
if id == 1:
    write(19)
    sleep(get_lenght(19))
    print('можно маме позвонить?')
elif id == 2:
    write(18)
    sleep(get_lenght(18))
    print('так точно')
elif id == 3:
    write(20)
    sleep(get_lenght(20))
    print('оружие будет?')
# заброшка
write(21)
sleep(get_lenght(21))
id = count()[0]
if id == 1:
    write(22)
    sleep(get_lenght(22))
    print('стоять')
elif id == 2:
    write(23)
    sleep(get_lenght(23))
    print('бежать')
# возвращаемся обратно
write(24)
sleep(get_lenght(24))
# новый день
write(25)
sleep(get_lenght(25))
id = count()[0]
if id == 1:
    write(26)
    sleep(get_lenght(26))
    print('привет')
    id = count()[0]
    if id == 1:
        write(27)
        sleep(get_lenght(27))
        print('почему сидишь одна')
        id = count()[0]
        if id == 1:
            write(28)
            sleep(get_lenght(28))
            print('может потому что..')
            id = count()[0]
            if id == 1:
                write(40)
                sleep(get_lenght(40))
                print('кст, узнал про тебя от толи')
                id = count()[0]
                if id == 1:
                    write(42)
                    sleep(get_lenght(42))
                    print('сказать как есть')
                elif id == 2:
                    write(41)
                    sleep(get_lenght(41))
                    print('сказать какая она красивая')
            elif id == 2:
                write(43)
                sleep(get_lenght(43))
                print('как твои дела')
                id = count()[0]
                if id == 1:
                    write(45)
                    sleep(get_lenght(45))
                    print('рассказать про недавнее задание')
                elif id == 2:
                    write(44)
                    sleep(get_lenght(44))
                    print('спросить как она попала в нашу банду')
        elif id == 2:
            write(29)
            sleep(get_lenght(29))
            print('согласен, глупый вопрос')
            id = count()[0]
            if id == 1:
                write(40)
                sleep(get_lenght(40))
                print('кст, узнал про тебя от толи')
                id = count()[0]
                if id == 1:
                    write(42)
                    sleep(get_lenght(42))
                    print('сказать как есть')
                elif id == 2:
                    write(41)
                    sleep(get_lenght(41))
                    print('сказать какая она красивая')
            elif id == 2:
                write(43)
                sleep(get_lenght(43))
                print('как твои дела')
                id = count()[0]
                if id == 1:
                    write(45)
                    sleep(get_lenght(45))
                    print('рассказать про недавнее задание')
                elif id == 2:
                    write(44)
                    sleep(get_lenght(44))
                    print('спросить как она попала в нашу банду')
    elif id == 2:
        write(30)
        sleep(get_lenght(30))
        print('я сидел и понял..')
        id = count()[0]
        if id == 1:
            write(40)
            sleep(get_lenght(40))
            print('кст, узнал про тебя от толи')
            id = count()[0]
            if id == 1:
                write(42)
                sleep(get_lenght(42))
                print('сказать как есть')
            elif id == 2:
                write(41)
                sleep(get_lenght(41))
                print('сказать какая она красивая')
        elif id == 2:
            write(43)
            sleep(get_lenght(43))
            print('как твои дела')
            id = count()[0]
            if id == 1:
                write(45)
                sleep(get_lenght(45))
                print('рассказать про недавнее задание')
            elif id == 2:
                write(44)
                sleep(get_lenght(44))
                print('спросить как она попала в нашу банду')
elif id == 2:
    write(31)
    sleep(get_lenght(31))
    print('привет. ты амина')
    id = count()[0]
    if id == 1:
        write(32)
        sleep(get_lenght(32))
        print('нет, но думаю самое время это исправить')
        id = count()[0]
        if id == 1:
            write(40)
            sleep(get_lenght(40))
            print('кст, узнал про тебя от толи')
            id = count()[0]
            if id == 1:
                write(42)
                sleep(get_lenght(42))
                print('сказать как есть')
            elif id == 2:
                write(41)
                sleep(get_lenght(41))
                print('сказать какая она красивая')
        elif id == 2:
            write(43)
            sleep(get_lenght(43))
            print('как твои дела')
            id = count()[0]
            if id == 1:
                write(45)
                sleep(get_lenght(45))
                print('рассказать про недавнее задание')
            elif id == 2:
                write(44)
                sleep(get_lenght(44))
                print('спросить как она попала в нашу банду')
    elif id == 2:
        write(46)
        sleep(get_lenght(46))
        print('да, я видел тебя на фотке')
        id = count()[0]
        if id == 1:
            write(42)
            sleep(get_lenght(42))
            print('сказать как есть')
        elif id == 2:
            write(41)
            sleep(get_lenght(41))
            print('сказать какая она красивая')
elif id == 3:
    write(33)
    sleep(get_lenght(33))
    print('твоя мама случайно не пекарь')
    id = count()[0]
    if id == 1:
        write(34)
        sleep(get_lenght(34))
        print('ладно, начнем с чистого листа')
        id = count()[0]
        if id == 1:
            write(40)
            sleep(get_lenght(40))
            print('кст, узнал про тебя от толи')
            id = count()[0]
            if id == 1:
                write(42)
                sleep(get_lenght(42))
                print('сказать как есть')
            elif id == 2:
                write(41)
                sleep(get_lenght(41))
                print('сказать какая она красивая')
        elif id == 2:
            write(43)
            sleep(get_lenght(43))
            print('как твои дела')
            id = count()[0]
            if id == 1:
                write(45)
                sleep(get_lenght(45))
                print('рассказать про недавнее задание')
            elif id == 2:
                write(44)
                sleep(get_lenght(44))
                print('спросить как она попала в нашу банду')
    elif id == 2:
        write(35)
        sleep(get_lenght(35))
        print('тогда откуда у нее такая булочка')
        id = count()[0]
        if id == 1:
            write(36)
            sleep(get_lenght(36))
            print('мог, но не успел')
            id = count()[0]
            if id == 1:
                write(37)
                sleep(get_lenght(37))
                print('с красотой не поспоришь')
                id = count()[0]
                if id == 1:
                    write(40)
                    sleep(get_lenght(40))
                    print('кст, узнал про тебя от толи')
                    id = count()[0]
                    if id == 1:
                        write(42)
                        sleep(get_lenght(42))
                        print('сказать как есть')
                    elif id == 2:
                        write(41)
                        sleep(get_lenght(41))
                        print('сказать какая она красивая')
                elif id == 2:
                    write(43)
                    sleep(get_lenght(43))
                    print('как твои дела')
                    id = count()[0]
                    if id == 1:
                        write(45)
                        sleep(get_lenght(45))
                        print('рассказать про недавнее задание')
                    elif id == 2:
                        write(44)
                        sleep(get_lenght(44))
                        print('спросить как она попала в нашу банду')
            elif id == 2:
                write(39)
                sleep(get_lenght(39))
                print('хорошо кроха')
                id = count()[0]
                if id == 1:
                    write(40)
                    sleep(get_lenght(40))
                    print('кст, узнал про тебя от толи')
                    id = count()[0]
                    if id == 1:
                        write(42)
                        sleep(get_lenght(42))
                        print('сказать как есть')
                    elif id == 2:
                        write(41)
                        sleep(get_lenght(41))
                        print('сказать какая она красивая')
                elif id == 2:
                    write(43)
                    sleep(get_lenght(43))
                    print('как твои дела')
                    id = count()[0]
                    if id == 1:
                        write(45)
                        sleep(get_lenght(45))
                        print('рассказать про недавнее задание')
                    elif id == 2:
                        write(44)
                        sleep(get_lenght(44))
                        print('спросить как она попала в нашу банду')
        elif id == 2:
            write(38)
            sleep(get_lenght(38))
            print('ну ты же и правда булочка')
            id = count()[0]
            if id == 1:
                write(40)
                sleep(get_lenght(40))
                print('кст, узнал про тебя от толи')
                id = count()[0]
                if id == 1:
                    write(42)
                    sleep(get_lenght(42))
                    print('сказать как есть')
                elif id == 2:
                    write(41)
                    sleep(get_lenght(41))
                    print('сказать какая она красивая')
            elif id == 2:
                write(43)
                sleep(get_lenght(43))
                print('как твои дела')
                id = count()[0]
                if id == 1:
                    write(45)
                    sleep(get_lenght(45))
                    print('рассказать про недавнее задание')
                elif id == 2:
                    write(44)
                    sleep(get_lenght(44))
                    print('спросить как она попала в нашу банду')
write(47)
sleep(get_lenght(47))
#диалог с мамой

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