from decouple import config


class AppConfig:
    TELEGRAM_URL = "https://api.telegram.org/bot{token}".format(token=config('TELEGRAM_BOT_TOKEN'))
    WEBHOOK_URL = "https://{host}:{port}{url}".format(host=config('HOST'), port=config('PORT'), url="/bot/webhook")
    URL = "/bot/webhook"
    HOST = config('HOST')
    PORT = config('PORT')
    MYSQL_USER = config('MYSQL_USER')
    MYSQL_HOST = config('MYSQL_HOST')
    MYSQL_PORT = config('MYSQL_PORT')
    MYSQL_PASSWORD = config('MYSQL_PASSWORD')
    MYSQL_DATABASE = config('MYSQL_DATABASE')
    CHAT_GPT_API_KEY = config('CHAT_GPT_API_KEY')
    TELEGRAM_BOT_TOKEN = config('TELEGRAM_BOT_TOKEN')
