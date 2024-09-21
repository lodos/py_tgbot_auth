import time
from datetime import datetime

import requests
from telegram import ReplyKeyboardMarkup
from telegram.helpers import escape_markdown

from app.globals import telegram_settings
from app.lang_RU import telegram_constants, project_title, project_synopsis
from modules.module_constants import auth_tg_keyboard, default_tg_keyboard
from modules.module_telegram import check_user_exists, add_user_in_db, check_tg_username_exists

# Глобальные настройки Telegram
BASE_URL = f"https://api.telegram.org/bot{telegram_settings['settings']['token']}"


# Функция для отправки сообщения с кнопками
def format_text(text):
    # Убираем обратные слеши, но оставляем разметку Markdown
    return text.replace('\\', '')

def send_message(chat_id, text, keyboard=None, simulate_typing_duration=0):
    if simulate_typing_duration > 0:
        simulate_typing(chat_id, simulate_typing_duration)

    formatted_text = format_text(text)  # Форматируем текст перед отправкой

    url = f"{BASE_URL}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': escape_markdown(formatted_text, version=2),  # Используем escape_markdown для экранирования текста
        'parse_mode': 'MarkdownV2'
    }

    if keyboard:
        payload['reply_markup'] = keyboard.to_dict() if isinstance(keyboard, ReplyKeyboardMarkup) else keyboard

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print(f"Сообщение отправлено: {formatted_text}")
    except requests.RequestException as e:
        print(f"Ошибка при отправке сообщения: {e}")


# Функция для имитации набираемого текста
def simulate_typing(chat_id, duration):
    url = f"{BASE_URL}/sendChatAction"
    payload = {
        'chat_id': chat_id,
        'action': 'typing'
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("Имитируем печать...")
        time.sleep(duration)
    except requests.RequestException as e:
        print(f"Ошибка при имитации печати: {e}")


# Функция для получения обновлений
def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"
    payload = {'offset': offset, 'timeout': 100}
    try:
        response = requests.get(url, params=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Ошибка при получении обновлений: {e}")
        return None


# Основная функция для обработки регистрации
def handle_registration(chat_id, user_info):
    susername = f"{user_info.get('first_name', '')} {user_info.get('last_name', '')}"

    if not check_user_exists(user_info['username']):
        print(user_info)
        add_user_in_db(user_info['username'], user_info)

        welcome_message = telegram_constants['user_added'].replace('[username]', escape_markdown(susername,  version=2))
        send_message(chat_id, welcome_message, auth_tg_keyboard, simulate_typing_duration=1)
    else:
        formatted_message = telegram_constants['user_remain_greeting'].replace('[username]',
                                                                               escape_markdown(susername, version=2))
        send_message(chat_id, formatted_message, auth_tg_keyboard, simulate_typing_duration=1)


# Основная функция
def main():
    offset = None
    user_state = {}  # Хранит состояние пользователя для обработки регистрации

    while True:
        updates = get_updates(offset)
        if updates and 'result' in updates:
            for update in updates['result']:
                offset = update['update_id'] + 1
                if 'message' in update:
                    chat_id = update['message']['chat']['id']
                    first_name = update['message']['chat'].get('first_name', 'Неизвестно')
                    last_name = update['message']['chat'].get('last_name', '')
                    username = update['message']['chat'].get('username', 'Неизвестно')
                    language_code = update['message']['from'].get('language_code', 'Неизвестно')

                    # Проверка на наличие текстового поля
                    message = update['message']
                    if 'text' in message:
                        text = message['text']
                    else:
                        continue  # Пропускаем обновления без текста

                    if text == '/start':
                        user_saved_card = {
                            'auth_source': 'telegram',
                            'first_name': first_name,
                            'last_name': last_name,
                            'username': username,
                            'language_code': language_code,
                        }
                        profile_card = telegram_constants['user_profile']

                        help_text = (profile_card
                                     .replace('[login]', username)
                                     .replace('[first_name]', first_name)
                                     .replace('[last_name]',last_name)
                                     .replace('[language_code]', language_code)
                                     )

                        send_message(chat_id, escape_markdown(help_text, version=2), simulate_typing_duration=1)
                        send_message(chat_id, escape_markdown(update['message']['chat'], version=2), simulate_typing_duration=1)


                    elif text == 'Помощь':
                        bot_steps = telegram_constants['bot_help']
                        for key in sorted(bot_steps.keys()):
                            help_text = bot_steps[key].replace('[project_title]', project_title).replace('[project_synopsis]', project_synopsis)
                            send_message(chat_id, escape_markdown(help_text, version=2), simulate_typing_duration=1)
                        continue



if __name__ == "__main__":
    main()
