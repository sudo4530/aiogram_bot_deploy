# app.py module
import logging
import os
from dotenv import load_dotenv
load_dotenv()

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

API_TOKEN = os.getenv("secret_key")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"Salom {message.from_user.first_name}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
