from .parser_base import BaseParser

from pandas import DataFrame


class CefParser(BaseParser):


    def __init__(self):
        super().__init__()


    def handle_message(self, message: str) -> DataFrame:
        pass
