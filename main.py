from time import sleep
import time
from config import Config
from ingestion import SocketReceiver
from parser import ParserListener

config = Config()

inbound_port = config.get_inbound_port()
print(inbound_port)

import redis





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
