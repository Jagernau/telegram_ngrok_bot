import pyngrok.ngrok as ng
import telebot
import os
from dotenv import load_dotenv
from os.path import join, dirname

from telebot import types
from passwordgenerator import pwgenerator
from uuid import uuid4



dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)



NGROK_TOKEN = os.environ.get("NGROK_TOKEN")
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
YOU_CHAT_ID = os.environ.get("YOU_CHAT_ID")
YOU_NAME = os.environ.get("YOU_NAME")

ng.set_auth_token(NGROK_TOKEN)
bot = telebot.TeleBot(str(TELEGRAM_BOT_TOKEN))




