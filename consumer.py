# consumer.py
class Consumer:
    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic
        self.offset = 0

    def poll(self):
        messages = self.broker.consume(self.topic, self.offset)
        self.offset += len(messages)
        return messages
