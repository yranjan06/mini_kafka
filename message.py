# message.py
import time

def create_message(value):
    return {
        "timestamp": time.time(),
        "value": value
    }
