import os
import logging

from .controllers.message.main import handle_message
from .controllers.command.main import handle_command
from .controllers.photo.main import handle_photo
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv

# Configurando o logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add_command_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler('start', handle_command))
    dispatcher.add_handler(CommandHandler('help', handle_command))
    dispatcher.add_handler(CommandHandler('test', handle_command))

def add_message_handlers(dispatcher):
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

def add_photo_handlers(dispatcher):
    dispatcher.add_handler(MessageHandler(Filters.photo, handle_photo))

def main():

    load_dotenv()

    TOKEN_TELEGRAM = os.getenv('TOKEN_TELEGRAM')

    # Criação do objeto Updater e passagem do token de acesso
    updater = Updater(TOKEN_TELEGRAM, use_context=True)

    # Configuração dos Handlers
    dispatcher = updater.dispatcher

    add_command_handlers(dispatcher)
    add_message_handlers(dispatcher)
    add_photo_handlers(dispatcher)

    # Inicia o Bot
    logging.debug('Starting bot...')

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()