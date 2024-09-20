import hashlib
import json
import random
from datetime import datetime

import pytz
from fastapi import HTTPException

from app.globals import params


async def MakeException(status, detail_string, settings=None):
    params['http_response'] = \
        {
            "status": status,
            "detail": detail_string
        }
    await SetHTTPErrorEvent(params)
    raise HTTPException(status_code=status, detail=detail_string)


async def SetHTTPErrorEvent(params):
    return True


def get_current_time():
    # Задайте желаемый часовой пояс, например 'Europe/Moscow'
    timezone = pytz.timezone('Europe/Moscow')

    # Получите текущее время с часовым поясом
    current_time = datetime.now(timezone)

    # Отформатируйте дату и время в нужный формат
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

    return formatted_time


def get_formatted_time(dt):
    # Задайте желаемый часовой пояс, например 'Europe/Moscow'
    timezone = pytz.timezone('Europe/Moscow')

    # Получите текущее время с часовым поясом
    current_time = dt(timezone)

    # Отформатируйте дату и время в нужный формат
    formatted_time = current_time.strftime('%Y-%d-%m %H:%M:%S %Z%z')

    return formatted_time


def get_article_sh256(article: str):
    article_encoded = hashlib.sha256(json.dumps(article).encode()).hexdigest()
    return article_encoded


def escape_apostrophes(value: str) -> str:
    # print(value)
    return str(value).replace("'", "`")


def process_article_body(article_body):
    if not isinstance(article_body, str):
        print("Error: The body is not a string.")
        return

    # Если строка пустая, сообщаем об этом
    if not article_body:
        print("The article body is empty.")
        return

    try:
        # Попробуйте загрузить строку JSON
        parsed_body = json.loads(article_body)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return

    # Проверяем тип после загрузки JSON
    if isinstance(parsed_body, dict):
        print("The article body is a dictionary.")
        # Обрабатываем как словарь
        # Пример: доступ к ключам и значениям
        for key, value in parsed_body.items():
            print(f"Key: {key}, Value: {value}")
    elif isinstance(parsed_body, list):
        print("The article body is a list.")
        # Обрабатываем как список
        # Пример: доступ к элементам списка
        for item in parsed_body:
            print(f"Item: {item}")
    else:
        print("The article body is neither a dictionary nor a list.")
