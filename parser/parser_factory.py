
from .parser_base import ParserType, BaseParser
from .parser_leef import LeefParser
from .parser_cef import CefParser

class ParserFactory:

    """
    Factory for returning parser instances based on parser type.
    """

    _leef_parser = LeefParser()
    _cef_parser = CefParser()


    @staticmethod
    def get_parser(parser_type: ParserType) -> BaseParser:
        if parser_type == ParserType.LEEF:
            return ParserFactory._leef_parser
        elif parser_type == ParserType.CEF:
            return ParserFactory._cef_parser

        else:
            return None




