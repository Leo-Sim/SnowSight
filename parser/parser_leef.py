from .base_parser import BaseParser



class LeefParser(BaseParser):


    def __init__(self):
        super().__init__()


    def handle_message(self, message) -> None:
        print(message)