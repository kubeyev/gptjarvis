import MySQLdb
import telegram
import requests
from appconfig import AppConfig
from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Set up database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}:{}/{}'.format(AppConfig.MYSQL_USER,
                                                                        AppConfig.MYSQL_PASSWORD,
                                                                        AppConfig.MYSQL_HOST,
                                                                        AppConfig.MYSQL_PORT,
                                                                        AppConfig.MYSQL_DATABASE)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up bot
bot = telegram.Bot(token=AppConfig.TELEGRAM_BOT_TOKEN)

mysql_config = {
    'user': AppConfig.MYSQL_USER,
    'host': AppConfig.MYSQL_HOST,
    'port': AppConfig.MYSQL_PORT,
    'password': AppConfig.MYSQL_PASSWORD,
    'database': AppConfig.MYSQL_DATABASE
}


# Define a route to receive updates from Telegram
@app.route('/bot/webhook', methods=["POST","GET"])
def webhook():
    print("Got a message")

    if request.method == "POST":
        data = request.get_json()

        if 'message' in data:
            chat_id = data['message']['chat']['id']
            message = data['message']['text']

            # Send the message to ChatGPT
            response = chatgpt_response(message)

            # Store data in MySQL
            store_in_mysql(chat_id, message, response)

            # Send to user by chat_id
            bot.send_message(chat_id=chat_id, text=response)

    return 'OK'


# Recieve answer with ChatGPT
def chatgpt_response(message):
    headers = {
        'Content - Type': 'application / json',
        'Authorization': 'Bearer {chatgpt_token}'.format(chatgpt_token=AppConfig.CHAT_GPT_API_KEY)
    }

    data = {
        'model': 'text - davinci - 003',
        'prompt': message,
        'temperature': 0.2,
        'max_tokens': 1024
    }

    response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=data, verify=False)
    generated_text = response.json()['choices'][0]['text']

    return generated_text


# Function to store data in MySQL
def store_in_mysql(chat_id, user_message, bot_response):
    import mysql.connector

    conn = mysql.connector.connect(**mysql_config)
    cursor = conn.cursor()

    insert_query = "INSERT INTO chat_data (chat_id, user_message, bot_response) VALUES (%s, %s, %s)"
    data = (chat_id, user_message, bot_response)

    cursor.execute(insert_query, data)

    conn.commit()
    conn.close()


# Set bot webhook
@app.route("/setwebhook/")
def set_webhook():
    s = requests.get(
        "{telegram_url}/setWebhook?url={webhook_url}".format(telegram_url=AppConfig.TELEGRAM_URL,
                                                             webhook_url=AppConfig.WEBHOOK_URL))

    if s:
        print("Successfully set up webhook")
        return "Success"
    else:
        print("Couldn't set up webhook")
        return "Fail"


# Start the application
if __name__ == '__main__':
    app.run(port=AppConfig.PORT, debug=True)
