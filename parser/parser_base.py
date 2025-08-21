import threading
import pandas as pd
import re

from datetime import datetime
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

    def __init__(self, load_information):

        self.load_information = load_information
        self.buffer = []
        self.batch_size = self.load_information.batch_size
        self.count = 0


    def _parse_syslog_header_info(self, header: str) -> dict:
        """
        Parse syslog header like:
        <98>Aug 20 13:46:07 db-03 custom-agent[6794]
        """
        pattern = (
            r"^<(?P<pri>\d+)>"                     # <98>
            r"(?P<timestamp>\w+\s+\d+\s+\d+:\d+:\d+)\s+"  # Aug 20 13:46:07
            r"(?P<host>\S+)\s+"                    # db-03
            r"(?P<app>[^\[]+)"                     # custom-agent
            r"(?:\[(?P<pid>\d+)\])?"               # [6794] optional
        )

        match = re.match(pattern, header)
        if not match:
            return {"raw_header": header}

        data = match.groupdict()

        # timestamp → datetime 변환 (연도는 현재 연도로 보정)
        try:
            ts = datetime.strptime(data["timestamp"], "%b %d %H:%M:%S")
            ts = ts.replace(year=datetime.now().year)
            data["timestamp"] = ts
        except Exception:
            pass

        return {
            "pri": int(data["pri"]),
            "timestamp": data["timestamp"],
            "host": data["host"],
            "app": data["app"].strip(),
            "pid": data.get("pid"),
        }

    def load_data(self, message: str) -> None:
        """
        This methods load parsed logs to data warehouse
        :return:
        """

        sys_header = self.parse_syslog_header(message)

        syslog_header_info: dict = self._parse_syslog_header_info(sys_header)



        info: dict = self.handle_message(message)
        info = {**info, **syslog_header_info}

        self.buffer.append(info)

        self.count += 1
        # TODO: empty buffer
        buffer_len = len(self.buffer)

        if self.count >= self.batch_size:
            self.count = 0

            # flush self.buffer
            df = pd.DataFrame(self.buffer)
            self.buffer.clear()







            pass
    @abstractmethod
    def parse_syslog_header(self, header) -> str:
        """
        This method is called to parse and return syslog header if it exists.
        :param header:
        :return: str
        """

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











