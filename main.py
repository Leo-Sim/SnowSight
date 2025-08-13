from time import sleep
import time
from config import Config
from ingestion import SocketReceiver
from ingestion.kafka_receiver import KafkaReceiver
from parser import ParserListener
import redis

config = Config()

inbound_port = config.get_inbound_port()
is_kafka = config.get_is_kafka()
kafka_ip = config.get_kafka_ip()
kafka_topic = config.get_kafka_topic()

print(is_kafka)
if is_kafka:
    receiver = KafkaReceiver(inbound_port, kafka_ip, kafka_topic)
    receiver.start()
else:
    receiver = SocketReceiver(inbound_port)

    receiver.start()

    parser_listener = ParserListener()
    parser_listener.get_message()




try:
    while True:
        pass  # or time.sleep(1) → keep main thread alive
except KeyboardInterrupt:
    print("\n[INFO] Shutting down...")
    receiver.stop()
