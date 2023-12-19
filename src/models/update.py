class User:
    def __init__(self, user_id, first_name, last_name, username, is_bot, language_code):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.is_bot = is_bot
        self.language_code = language_code

class Chat:
    def __init__(self, chat_id, first_name, last_name, type, username):
        self.id = chat_id
        self.first_name = first_name
        self.last_name = last_name
        self.type = type
        self.username = username

class Message:
    def __init__(self, message_id, date, text, chat, from_user):
        self.message_id = message_id
        self.date = date
        self.text = text
        self.chat = chat
        self.from_user = from_user

class Update:
    def __init__(self, update_id, message):
        self.update_id = update_id
        self.message = message   