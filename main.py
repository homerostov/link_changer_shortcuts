import aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import requests
import os



bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nОтправь мне ссылку, а я сделаю из нее другую ссылку!)")

@dp.message_handler()
async def process_start_command(message: types.Message):
    try:
        link = 'https://new_link.com/' + message.text.split('/')[4]

    except:
        link = "Это не похоже на ссылку Кинопосика"
    await message.reply(link)

if __name__ == '__main__':
    executor.start_polling(dp)