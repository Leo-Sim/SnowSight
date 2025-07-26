import threading
from message import RedisChannelInfo, RedisClient
class ParserListener:

    """
    This class subscribe publisher and parse log according to its type
    """
    def __init__(self):
        self.redisClient = RedisClient()
        self.pubsub = self.redisClient.subscribe(RedisChannelInfo.CHANNEL_INBOUND_TCP)


    def get_message(self) -> None:
        """
        Start a listener thread to receive incoming message
        :return: None
        """

        def listener():

            for message in self.pubsub.listen():

                if message['type'] == 'message':
                    data = message['data']
                    if isinstance(data, bytes):
                        data = data.decode('utf-8')
                    print(message)

        thread = threading.Thread(target=listener, daemon=True)
        thread.start()