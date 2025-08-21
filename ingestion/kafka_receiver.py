from kafka import KafkaConsumer
import json
import threading

from parser import ParserFactory
from ingestion import BaseReceiver

class KafkaReceiver(BaseReceiver):

    def __init__(self, port, ip, kafka_topic):
        super().__init__()

        self.ip = ip
        self.port = port
        self.kafka_topic = kafka_topic

        self.consumer = KafkaConsumer(
            self.kafka_topic,
            bootstrap_servers=self.ip + ':' + str(self.port),
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda value: json.loads(value),
        )

        self.stop_event = threading.Event()

    def start(self):

        thread = threading.Thread(target=self._listen, daemon=True)
        thread.start()
        return thread


    def _listen(self):

        for message in self.consumer:
            if self.stop_event.is_set():
                break

            parser = ParserFactory.get_parser(message.value)

            if parser is None:
                print(f"[Error] Parser is None. Message: {message.value}")
                continue

            parser.load_data(message.value)

    def stop(self):
        self.stop_event.set()
        self.consumer.close()


    def handle_message(self, message: str):
        pass


# if __name__ == "__main__":
#     k = KafkaReceiver()




