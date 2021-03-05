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
write(48)
sleep(get_lenght(48))
id = count()[0]
if id == 1:
    write(51)
    sleep(get_lenght(51))
    print('ответить все хорошо')
    id = count()[0]
    if id == 1:
        write(52)
        sleep(get_lenght(52))
        print('еду с друзьями на тусовку')
        id = count()[0]
        if id == 1:
            write(53)
            sleep(get_lenght(53))
            print('еще бы, самую лучшую')
        elif id == 2:
            write(54)
            sleep(get_lenght(54))
            print('да не мам, какая невестка')
        elif id == 3:
            write(55)
            sleep(get_lenght(55))
            print('мааам')
    elif id == 2:
        write(61)
        sleep(get_lenght(61))
        print('да, неважно')
elif id == 2:
    write(49)
    sleep(get_lenght(49))
    print('промолчать')
    write(50)
    sleep(get_lenght(50))
    print('ну возьми ты это же мама')
    id = count()[0]
    if id == 1:
        write(51)
        sleep(get_lenght(51))
        print('привет мамуль')
        id = count()[0]
        if id == 1:
            write(52)
            sleep(get_lenght(52))
            print('еду с друзьями на тусовку')
            id = count()[0]
            if id == 1:
                write(53)
                sleep(get_lenght(53))
                print('еще бы, самую лучшую')
            elif id == 2:
                write(54)
                sleep(get_lenght(54))
                print('да не мам, какая невестка')
            elif id == 3:
                write(55)
                sleep(get_lenght(55))
                print('мааам')
        elif id == 2:
            write(61)
            sleep(get_lenght(61))
            print('да, неважно')
    elif id == 2:
        write(56)
        sleep(get_lenght(56))
        print('я супер, еду сейчас забирать оружие')
        id = count()[0]
        if id == 1:
            write(57)
            sleep(get_lenght(57))
            print('да это безопасно')
        elif id == 2:
            write(58)
            sleep(get_lenght(58))
            print('не, это не то о чем ты подумала')
        elif id == 3:
            write(59)
            sleep(get_lenght(59))
            print('я не хочу слышать нотации')
    elif id == 3:
        write(62)
        sleep(get_lenght(62))
        print('нормально')
        id = count()[0]
        if id == 1:
            write(63)
            sleep(get_lenght(63))
            print('да ничего давай пока')
        elif id == 2:
            write(64)
            sleep(get_lenght(64))
            print('все хорошо просто много работаю')
            id = count()[0]
            if id == 1:
                write(65)
                sleep(get_lenght(65))
                print('да тут работа такая, курьерска')
            elif id == 2:
                write(66)
                sleep(get_lenght(66))
                print('этого тебе знать не стоит')
            elif id == 3:
                write(67)
                sleep(get_lenght(67))
                print('в банде')
                id = count()[0]
                if id == 1:
                    write(57)
                    sleep(get_lenght(57))
                    print('да это безопасно')
                elif id == 2:
                    write(58)
                    sleep(get_lenght(58))
                    print('не, это не то о чем ты подумала')
                elif id == 3:
                    write(59)
                    sleep(get_lenght(59))
                    print('я не хочу слышать нотации')
        elif id == 3:
            write(60)
            sleep(get_lenght(60))
            print('да нет все хорошо лучше расскажи как у тебя дела')
            id = count()[0]
            if id == 1:
                write(52)
                sleep(get_lenght(52))
                print('еду с друзьями на тусовку')
                id = count()[0]
                if id == 1:
                    write(53)
                    sleep(get_lenght(53))
                    print('еще бы, самую лучшую')
                elif id == 2:
                    write(54)
                    sleep(get_lenght(54))
                    print('да не мам, какая невестка')
                elif id == 3:
                    write(55)
                    sleep(get_lenght(55))
                    print('мааам')
            elif id == 2:
                write(61)
                sleep(get_lenght(61))
                print('да, неважно')
write(68)
sleep(get_lenght(68))
id = count()[0]
if id == 1:
    write(71)
    sleep(get_lenght(71))
    print('взять трубку')
    id = count()[0]
    if id == 1:
        write(73)
        sleep(get_lenght(73))
        print('исследовать территория, где была сделка')
    elif id == 2:
        write(72)
        sleep(get_lenght(72))
        print('исследовать территорию вокруг')
    elif id == 3:
        write(74)
        sleep(get_lenght(74))
        print('позвноить одному из друзей')
elif id == 2:
    write(70)
    sleep(get_lenght(70))
    print('сбросить')
elif id == 3:
    write(69)
    sleep(get_lenght(69))
    print('проигнорить')
write(76)
sleep(get_lenght(76))
id = count()[0]
if id == 1:
    write(77)
    sleep(get_lenght(77))
    print('рассказать правду')
elif id == 2:
    write(78)
    sleep(get_lenght(78))
    print('солгать')
elif id == 3:
    write(79)
    sleep(get_lenght(79))
    print('промолчать')
write(80)
sleep(get_lenght(80))
id = count()[0]
if id == 1:
    write(81)
    sleep(get_lenght(81))
    print('начать рассказывать ')
    id = count()[0]
    if id == 1:
        write(82)
        sleep(get_lenght(82))
        print('сказать правду про девушку')
    elif id == 2:
        write(83)
        sleep(get_lenght(83))
        print('сказать что звонил диспетчер')
elif id == 2:
    write(84)
    sleep(get_lenght(84))
    print('начать говорить про ложь')
    id = count()[0]
    if id == 1:
        write(85)
        sleep(get_lenght(85))
        print('давить  на жалость')
    elif id == 2:
        write(86)
        sleep(get_lenght(86))
        print('начать обвинять босса')
# конец
write(87)
sleep(get_lenght(87))
id = count()[0]

if id == 1:
    write(91)
    sleep(get_lenght(91))
    print('толя')
elif id == 2:
    write(91)
    sleep(get_lenght(91))
    print('чулок')
elif id == 3:
    write(88)
    sleep(get_lenght(88))
    print('босс')
'''
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