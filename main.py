from time import sleep
from sqlite import DataBase
from random import choice

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

bd = DataBase('data/user.db')


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


print('идёт фильм')
print('выбор')
sleep(10)

id = count()
if id == 1:
    print('бежим на право')
elif id == 2:
    print('бежим на лево')
else:
    print('АААААААА')
