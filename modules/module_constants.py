from telegram import ReplyKeyboardMarkup, KeyboardButton

auth_tg_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Профиль")],
        # [KeyboardButton(text="Мои проекты")], # Пример кнопки дополнительного меню
        [KeyboardButton(text="Помощь")],
    ],
    resize_keyboard=True
)

default_tg_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        # [KeyboardButton(text="Регистрация")],
        [KeyboardButton(text="Помощь")],
    ],
    resize_keyboard=True
)
