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
        'token': '[TG_BOT_TOKEN]',
        "bot_name": '[TG_BOT_NAME]',
    },
}

params = {
    "host": "0.0.0.0",
    "port": 8003
}

# Basic auth credits
auth_params = {
    'username': '[BASIC_AUTH_LOGIN]',
    'password': '[BASIC_AUTH_PASS]',
}

