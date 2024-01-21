import os

import telebot
from dotenv import load_dotenv
from telebot.types import Message

load_dotenv('.env')
API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(content_types=['text'])
def echo(message: Message):
    bot.send_message(message.chat.id, message.text)


bot.polling()
