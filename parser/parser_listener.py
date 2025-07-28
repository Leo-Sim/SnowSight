import threading
from message import RedisChannelInfo, RedisClient
from parser import ParserFactory, LeefParser, CefParser, ParserType, BaseParser


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

                        parser: BaseParser = None

                        if "LEEF:2.0" in data or "LEEF:1.0" in data:
                            parser = ParserFactory.get_parser(ParserType.LEEF)

                        elif "CEF:" in data:
                            parser = ParserFactory.get_parser(ParserType.CEF)

                        parser.load_data(data)








        thread = threading.Thread(target=listener, daemon=True)
        thread.start()