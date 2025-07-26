import threading
from abc import ABC, abstractmethod
from message import RedisClient, RedisChannelInfo

class ParserType:
    """
    Supported parser types
    """
    CUSTOM = "custom"
    LEEF = "leef"
    CEF = "cef"


class BaseParser(ABC):
    """
    Base class for log parsers.
    It supports custom, leef, and cef formats

    """

    def __init__(self):
        pass

    @abstractmethod
    def handle_message(self, message) -> None:
        """
        Handle incoming message
        :param message:
        :return: None
        """
        pass











