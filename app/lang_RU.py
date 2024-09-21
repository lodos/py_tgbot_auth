project_title = "Simple TGBot"
project_version = "0.1"
project_synopsis = "Простой телеграм-бот для авторизации пользователей через аккаунт Телег"
# Telegram constants
telegram_constants = {
    "welcome_message": {
        "step1": f"""👨‍🔬 Рады приветствовать Вас, [username]!""",
        "step2": f"""[project_title] - это демонстрация стендовой модели по авторизации пользователя через Телеграм без ввода ПДн.""",
        "step3": f"""Воспользуйтесь разделом Помощь, чтобы узнать о проекте более подробно.💡""",
    },
    "user_added": "Пользователь [username] успешно зарегистрирован",
    "user_welcome_greeting": "🎉 Рады Вас приветствовать, [username]!",
    "user_remain_greeting": "😍‍ Рады Вас видеть, [username]!",
    "user_add_success": "Пользователь успешно добавлен! Вы можете делать все, что угодно. Мы по Вас, [username], теперь знаем всё! (шутка) 😄😄",
    "user_unknown_error": "Произошла ошибка",
    "register_completed": "Регистрация уже завершена.",

    "bot_help": {
        "step1": f"""📚 Добро пожаловать в систему помощи проекта [project_title]!""",
        "step2": f"""📖 [project_synopsis]""",
        "step3": f"""💡 Возможности: 

   Бот не собирает Ваши Персональные Данные. Нам достаточны для Вашей безопасной идентификации только те данные, которые Вы сами дали Телеграм-мессенджеру: username, firstname, lastname
   """
    },

    "user_profile": f"""
Имя пользователя: [login]
Дата регистрации: [registration_date]
Дата истечения: [expiry_date]

Информация об аккаунте:
Источник регистрации: [auth_source]
Имя: [first_name]
Фамилия: [last_name]
Язык: [language_code]
    """
}

