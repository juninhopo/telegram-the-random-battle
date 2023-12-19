import logging

def handle_message(update, context):
    logging.info({
        'first_name': update.message.from_user.first_name,
        'chat_id': update.message.chat_id,
        'message': update.message.text,
    })