import logging

from ...utils.sendtext import send_text

def help(update):
  logging.info({
    'user_id': update.message.from_user.id,
    'command': update.message.text,
    'chat_id': update.message.chat_id,
  })
  text = '''
  Comandos disponíveis:

  /start -> Necessário para você me usar. 👹 
  /help  -> Você verifica tudo que posso fazer.
  /test  -> Você apenas verifica se o bot está funcionando.
  '''

  send_text(chat_id=update.message.chat_id, text=text)
