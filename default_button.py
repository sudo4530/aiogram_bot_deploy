from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button = ReplyKeyboardMarkup(resize_keyboard=True)
button.add(KeyboardButton("Menyu"))

menu_button = ReplyKeyboardMarkup(resize_keyboard=True)
menu_button.add(KeyboardButton("Product 1"), KeyboardButton("Product 2"))
