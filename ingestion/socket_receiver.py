
import socket
import threading
from message import RedisClient, RedisChannelInfo
from ingestion import BaseReceiver

class SocketReceiver(BaseReceiver):

    """
    Log data receiver with TCP connection.

    """

    def __init__(self, port):
        super().__init__()

        self.port = port
        self.host = "0.0.0.0"
        self.running = False
        self.thread = None

        self.redis_client = RedisClient()



    def start(self):
        """Start receiving data."""
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._start_tcp_server, daemon=True)
            self.thread.start()
            print("[INFO] Server started.")

    def stop(self):
        """Stop receiving data."""
        self.running = False
        if self.thread is not None:
            self.thread.join()
            print("[INFO] Server stopped.")

    def handle_message(self, message: str):
        self.redis_client.publish(RedisChannelInfo.CHANNEL_INBOUND_TCP, message)


    def _start_tcp_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen()
            server_socket.settimeout(1.0)  # Allow periodic checks for self.running
            print(f"[INFO] Listening on {self.host}:{self.port}")

            while self.running:
                try:
                    conn, addr = server_socket.accept()
                except socket.timeout:
                    continue  # Check self.running again
                print(f"[INFO] Connection from {addr}")

                with conn:
                    while self.running:
                        try:
                            data = conn.recv(4096)
                            if not data:
                                break
                            message = data.decode('utf-8', errors='ignore')
                            self.handle_message(message)
                        except ConnectionResetError:
                            break



