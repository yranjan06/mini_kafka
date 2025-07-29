# main.py
from broker import Broker
from producer import Producer
from consumer import Consumer

# Setup
broker = Broker()
producer = Producer(broker)
consumer = Consumer(broker, topic="logs")

# Simulate Producers
producer.send("logs", "User A signed in")
producer.send("logs", "User B uploaded photo")
producer.send("logs", "User C signed out")

# Simulate Consumer Polling
print("Consumer reading logs:")
msgs = consumer.poll()
for msg in msgs:
    print(f"[{msg['timestamp']:.2f}] {msg['value']}")

# Second poll → should be empty
print("\n Second poll (should be empty):")
msgs = consumer.poll()
print(msgs)
