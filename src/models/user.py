# Model do usuário (player)
class Person:
    def __init__(self, user_id, chat_id, first_name, username, class):
      self.id = user_id
      self.chat_id = chat_id
      self.first_name = first_name
      self.username = username
      self.class = class
