import logging
from ...utils.sendtext import send_text

def test(update):
  logging.info({
    'user_id': update.message.from_user.id,
    'command': update.message.text,
    'chat_id': update.message.chat_id,
  })
  text = 'Eu estou funcionando! 🤖'
  send_text(chat_id=update.message.chat_id, text=text)
