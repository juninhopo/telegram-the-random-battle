import telegram
from dotenv import load_dotenv
import os

def send_photo(chat_id, photo):
  load_dotenv()

  TOKEN_TELEGRAM = os.getenv('TOKEN_TELEGRAM')
  bot = telegram.Bot(TOKEN_TELEGRAM)
  bot.send_photo(chat_id, photo)