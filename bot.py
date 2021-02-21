import logging
import config
from aiogram import Bot, Dispatcher, executor, types
from sqlite import DataBase
import asyncio

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

bd = DataBase('data/user.db')
bd.clear()


@dp.message_handler(commands=['start'])
async def hi(message: types.Message):
    await message.answer('Привет! Добро пожаловать. Следи за игрой и успевай отправлять ответы')


@dp.message_handler(content_types=['text'])
async def said(message: types.Message):
    if not bd.check_id(message.from_user.id):
        bd.new_user(message.from_user.id, message.text)
        await message.answer('Ваш ответ засчитан')
    else:
        await message.answer('Вы уже ответили')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

