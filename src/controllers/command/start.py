import logging

from ...utils.sendtext import send_text
from .help import help

def start(update):
  logging.info({
    'user_id': update.message.from_user.id,
    'command': update.message.text,
    'chat_id': update.message.chat_id,
  })
  text = '''
  Bem Vindo ao The Random Battle.
  '''
  send_text(chat_id=update.message.chat_id, text=text)
  help(update)