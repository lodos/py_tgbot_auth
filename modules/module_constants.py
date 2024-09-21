from telegram import ReplyKeyboardMarkup, KeyboardButton

auth_tg_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Профиль")],
        [KeyboardButton(text="Помощь")],
    ],
    resize_keyboard=True
)

default_tg_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Регистрация")],
        [KeyboardButton(text="Помощь")],
    ],
    resize_keyboard=True
)
