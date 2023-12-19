from .start import start
from .test import test
from .help import help
from .unknowncommand import unknown_command

def handle_command(update, context):
    command = update.message.text
    
    if command == '/start':
        start(update)
    elif command == '/help':
        help(update)
    elif command == '/test':
        test(update)
    else:
        unknown_command(update)