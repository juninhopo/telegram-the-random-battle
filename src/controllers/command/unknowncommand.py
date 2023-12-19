import logging
from ...utils.sendtext import send_text

def unknown_command(update):
  logging.info({
    'command': update.message.text,
    'chat_id': update.message.chat_id,
  })
  text = '''
  Esse comando não existe.
  Você pode tentar o comando /help para ajuda.
  '''
  send_text(chat_id=update.message.chat_id, text=text)
