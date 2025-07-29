# broker.py
class Broker:
    
    def __init__(self):
        self.topics = {}  # Dictionary: topic_name → list of messages

    def create_topic(self, topic_name):
        if topic_name not in self.topics:
            self.topics[topic_name] = []

    def publish(self, topic_name, message):
        self.create_topic(topic_name)
        self.topics[topic_name].append(message)

    def consume(self, topic_name, offset=0):
        if topic_name not in self.topics:
            return []
        return self.topics[topic_name][offset:]
    
   

