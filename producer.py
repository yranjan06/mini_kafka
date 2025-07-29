# producer.py
import time
from message import create_message

class Producer:
    def __init__(self, broker):
        self.broker = broker

    def send(self, topic, value):
        message = create_message(value)
        self.broker.publish(topic, message)
