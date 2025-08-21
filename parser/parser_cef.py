from .parser_base import BaseParser

from pandas import DataFrame


class CefParser(BaseParser):


    def __init__(self):
        super().__init__()

    def parse_syslog_header(self, header) -> str:
        pass

    def handle_message(self, message: str) -> DataFrame:
        pass
