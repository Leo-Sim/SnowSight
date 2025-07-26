from .base_parser import ParserType, BaseParser


class ParserFactory:

    """
    Factory for returning parser instances based on parser type.
    """

    @staticmethod
    def get_parser(parser_type: ParserType) -> BaseParser:
        pass


