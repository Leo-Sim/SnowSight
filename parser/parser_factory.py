
from .parser_base import ParserType, BaseParser
from .parser_leef import LeefParser
from .parser_cef import CefParser
from loader import LoadInformation
class ParserFactory:

    """
    Factory for returning parser instances based on parser type.
    """

    load_information = LoadInformation()

    _leef_parser = LeefParser(load_information)
    _cef_parser = CefParser(load_information)


    @staticmethod
    def get_parser(data) -> BaseParser:
        if "LEEF:2.0" in data or "LEEF:1.0" in data:
            return ParserFactory._leef_parser
        elif "CEF:" in data:
            return ParserFactory._cef_parser

        else:
            return None




