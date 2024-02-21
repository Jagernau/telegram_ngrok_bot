import telebot
import os
from dotenv import load_dotenv
from os.path import join, dirname



dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)



TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
YOU_CHAT_ID = os.environ.get("YOU_CHAT_ID")

bot = telebot.TeleBot(str(TELEGRAM_BOT_TOKEN))




