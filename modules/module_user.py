import re


def validate_email(email: str) -> bool:
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email) is not None


# Функция для проверки корректности телефона
def validate_phone(phone: str) -> bool:
    phone_regex = r"^\+?\d{10,15}$"
    return re.match(phone_regex, phone) is not None


# Функция для проверки корректности логина
def validate_login(login: str) -> bool:
    # Регулярное выражение:
    # ^[a-zA-Zа-яА-ЯёЁ]+([ ]?[a-zA-Zа-яА-ЯёЁ]+){0,2}$:
    # - начало строки (^)
    # - первая часть логина: буквы латинского или русского алфавита ([a-zA-Zа-яА-ЯёЁ]+)
    # - далее допускается 0, 1 или 2 пробела, после каждого из которых должны быть буквы ([ ]?[a-zA-Zа-яА-ЯёЁ]+){0,2}
    # - конец строки ($)
    pattern = r'^[a-zA-Zа-яА-ЯёЁ]+([ ]?[a-zA-Zа-яА-ЯёЁ]+){0,2}$'

    return bool(re.match(pattern, login))

