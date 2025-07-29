# Mini Kafka in Python

This is a simplified version of Apache Kafka, built in Python from scratch to understand how Kafka works at its core.

---

## Why This Project?

Inspired by the 2011 Kafka whitepaper from LinkedIn engineers, this project breaks down Kafka’s architecture into:
- 1. Producer
- 2. Broker (with topics)
- 3. Consumer with offset tracking

No servers. No zookeepers. Just raw logic and code.

https://notes.stephenholiday.com/Kafka.pdf

---

## Learnings:

- What is a topic?
- How messages are stored and consumed
- How offsets enable reliable message delivery
- Event-driven thinking

---

## Components


| File        | Role                               |
|-------------|------------------------------------|
| broker.py   | Stores messages per topic          |
| producer.py | Sends messages to broker           |
| consumer.py | Pulls messages with offset         |
| message.py  | Timestamped messages               |
| topic.py    | (Optional) Topic class             |
| main.py     | Demo: producer → broker → consumer |



---

## Run This

```bash
python main.py


---
