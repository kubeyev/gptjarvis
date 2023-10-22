# GPTJarvis

Telegram bot for friendly use of chat gpt

# Pre-requisite
- Python 3
- Flask
- Telegram
- Request
- Ngrok (optional for localhost)

Note: You can user ngrok to speed up development and test your bot locally

# Getting started

## Setting up environment 

1. Go to @botfather on Telegram to create a bot handle.
2. Type /newbot to create a new bot.
3. Name your bot e.g. EXAMPLE
4. Username of your bot e.g EXAMPLEBOT - This is the @username handle that can be search by users on Telegram
5. Once done, copy the token generated and add to the script TELEGRAM_BOT_TOKEN env variable.
6. Change WEBHOOK_DOMAIN and WEBHOOK_URL to the hosting url and domain (this must be HTTPS).
7. Change variables related to MySQL set up in environment to your database variables.
8. Generate ChatGPT api key or put yours, remember in this project I used "text-davinci-003" model, 
and you can choose your preferred model.
9. Once done, copy the token generated and add to the script CHAT_GPT_API_KEY env variable.

## To enable bot for group chat
1. Go to @botfather on Telegram
2. Type /mybot, and select on your created bot e.g. EXAMPLEBOT
3. Go to 'Bot Settings' -> 'Group Privacy', and select on 'Turn off'

## Usage
After installing Ngrok, run ./ngrok http 5000 (with 5000 being the default port for Flask). Ngrok will return provide 
a publicly accessible URL for the running script, change WEBHOOK_URL and WEBHOOK_DOMAIN variables.

Run pip install requirements to download packages, python3 bot.py to start running and using the bot.
