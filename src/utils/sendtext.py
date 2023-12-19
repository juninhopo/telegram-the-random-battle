import telegram
from dotenv import load_dotenv
import os

def send_text(chat_id, text):
  load_dotenv()

  TOKEN_TELEGRAM = os.getenv('TOKEN_TELEGRAM')
  bot = telegram.Bot(TOKEN_TELEGRAM)
  bot.send_message(chat_id, text)