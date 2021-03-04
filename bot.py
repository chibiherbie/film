import logging
import config
from aiogram import Bot, Dispatcher, executor, types
from sqlite import DataBase
import asyncio

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

bd = DataBase('data/user.db')
bd.clear()  # очищаем бд


# приветственное слово
@dp.message_handler(commands=['start'])
async def hi(message: types.Message):
    await message.answer('Привет! Добро пожаловать. Следи за игрой и успевай отправлять ответы')


# обработка сообщений
@dp.message_handler(content_types=['text'])
async def said(message: types.Message):
    if '1' != message.text and '2' != message.text and '3' != message:
        await message.answer('Такого варианта ответа нет')
    elif not bd.check_id(message.from_user.id):
        bd.new_user(message.from_user.id, message.text)  # заносим id в бд для защиты от спама ответов
        await message.answer('Ваш ответ засчитан')
    else:
        await message.answer('Вы уже ответили')


async def check():
    while True:
        with open('connect2.txt', 'r') as f:
            file = f.read()
        if file == 'start':
            info = bd.get_id()
            print(info)
            with open('connect2.txt', 'w') as f:
                f.write('')
        await asyncio.sleep(1)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(check())
    executor.start_polling(dp, skip_updates=True)
