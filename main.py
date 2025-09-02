
from time import sleep
from config import Config
from ingestion import SocketReceiver
from ingestion.kafka_receiver import KafkaReceiver
from parser import ParserListener
from loader import LoadInformation, Loader

import redis
import time

config = Config()

inbound_port = config.get_inbound_port()
is_kafka = config.get_is_kafka()
kafka_ip = config.get_kafka_ip()
kafka_topic = config.get_kafka_topic()


if is_kafka:
    receiver = KafkaReceiver(inbound_port, kafka_ip, kafka_topic)
    receiver.start()

    print(f"[Info] Receiver type : Kafka")
else:
    receiver = SocketReceiver(inbound_port)

    receiver.start()

    parser_listener = ParserListener()
    parser_listener.get_message()
    print(f"[Info] Receiver type : Socket (TCP)")




try:
    while True:
        pass  # or time.sleep(1) → keep main thread alive
except KeyboardInterrupt:
    print("\n[INFO] Shutting down...")
    receiver.stop()
