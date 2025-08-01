import threading
from abc import ABC, abstractmethod
from pandas import DataFrame
from message import RedisClient, RedisChannelInfo
from loader import LoadInformation

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

    def parse_syslog_header(self, header):
        pass

    def load_data(self, message: str) -> None:
        """
        This methods load parsed logs to data warehouse
        :return:
        """

        info: dict = self.handle_message(message)

        #TODO: load parsed log to  data warehouse
        pass

    @abstractmethod
    def handle_message(self, message: str) -> dict:
        """
        This method is called when a message is received.
        This method is responsible for parsing data
        Returns dictionary of each parsed log information

        :param message:
        :return: Dictionary
        """
        pass











