import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5918389355:AAFcazb0fW53aaiY6Ws5Utd5Hy3jqTNksno'

wikipedia.set_lang("uz")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykumm!\nWikipedia botga xush kelibsiz!")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Siz bu botga xabar yuborasiz va wikipediadan ma'lumot olasiz.")

@dp.message_handler()
async def echo(message: types.Message):
    sorov = message.text
    try:
        javob=wikipedia.summary(sorov)
        await message.answer(javob)
    except:
        await message.reply("Kechirasiz, wikipediyada bu haqida ma'lumot topilmadi.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
