from flask_sqlalchemy import SQLAlchemy

# Create a SQLAlchemy instance
db = SQLAlchemy()


# Define the ChatData model
class ChatData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.String(255), nullable=False)
    user_message = db.Column(db.String(255), nullable=False)
    bot_response = db.Column(db.String(255), nullable=False)

    def __init__(self, chat_id, user_message, bot_response):
        self.chat_id = chat_id
        self.user_message = user_message
        self.bot_response = bot_response
