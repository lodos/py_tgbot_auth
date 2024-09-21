import json
from datetime import datetime

from dateutil.relativedelta import relativedelta

from app.globals import database_user
from app.lang_RU import telegram_constants


def send_return_welcome():
    pass


def check_tg_username_exists(tg_username):
    try:
        # Открываем файл с пользователями
        with open('database/users.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Ищем массив users_list
        users_list = data.get('users_list', [])

        # Проходим по списку пользователей и ищем совпадение по имени
        for user in users_list:
            if user == tg_username:
                return users_list[user]

        return False
    except FileNotFoundError:
        print("Файл не найден.")
        return False
    except json.JSONDecodeError:
        print("Ошибка при чтении JSON.")
        return False


def add_user_in_db(login: str, user_info: dict):
    if check_user_exists(login):
        return telegram_constants['user_exists']

    now = datetime.now()
    thirty_years_later = now + relativedelta(years=30)  # Добавляем 30 лет
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')

    # Создаем нового пользователя с информацией
    new_user = {
        'login': login,
        'registration_date': now_str,
        'expiry_date': thirty_years_later.strftime('%Y-%m-%d %H:%M:%S'),
        'user_info': user_info  # Сохраняем дополнительную информацию о пользователе
    }

    # Читаем существующие данные из файла
    try:
        with open(database_user, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {'users_list': {}}

    # Добавляем нового пользователя в словарь
    data['users_list'][login] = new_user

    # Сохраняем обновленные данные в файл
    with open(database_user, 'w') as f:
        json.dump(data, f, indent=4)

    return telegram_constants['user_added'].replace('[username]', login)  # Вернуть сообщение об успешном добавлении



def check_user_exists(login: str) -> bool:
    """Проверяет, существует ли пользователь в файле."""
    try:
        with open(database_user, 'r') as f:
            data = json.load(f)
            return login in data['users_list']
    except (FileNotFoundError, json.JSONDecodeError):
        return False

