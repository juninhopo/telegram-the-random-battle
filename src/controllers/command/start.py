import logging

from ...utils.sendtext import send_text
from .help import help

def start(update):
  logging.info({
    'command': update.message.text,
    'user_id': update.message.user_id,
    'chat_id': update.message.chat_id,
  })
  text = '''
  Bem Vindo ao The Random Battle.
  '''
  send_text(chat_id=update.message.chat_id, text=text)
  help(update)