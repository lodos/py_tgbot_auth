is_prod = 0  # Если 0 - то dev контур, если 1 - prod

app_settings = {
    'fastapi': {
        'host': '0.0.0.0',
        'port': 8601,
    },
    'gradio': {
        "share": False
    }
}

database_user = 'database/users.json'

telegram_settings = {
    'flask': {
        'host': '0.0.0.0',
        'port': 8443,
    },
    'settings': {
        'token': '7931868142:AAH4OY2qLG59QLMp1D5icdGbqaWfSbRtcwM',
        "bot_name": 'EPGSDemoBot',
    },
}

params = {
    "host": "0.0.0.0",
    "port": 8003
}

#  новая версия лицензирования
auth_params = {
    'username': 'tgbot',
    'password': 'Pq6827CmJD5Hl6OjcBQpjp9ceUJtAUM',
}

