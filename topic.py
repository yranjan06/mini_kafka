# topic.py
class Topic:
    def __init__(self, name):
        self.name = name
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def get_messages(self, offset):
        return self.messages[offset:]
