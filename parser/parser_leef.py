from mypy.reachability import infer_reachability_of_if_statement

from .parser_base import BaseParser
from pandas import DataFrame

import pandas as pd


class LeefParser(BaseParser):



    def __init__(self):
        super().__init__()


    def handle_message(self, message: str) -> dict:

        result = {}
        infos = message.split(LeefInfo.HEADER_DELIMITER)

        #TODO: parse syslog header

        leef_index = infos[0].find("LEEF:")

        # Remove delimiter
        sys_header = leef_index - 2

        leef_index = infos[0][leef_index:]

        # Get leef header information
        leef_version = leef_index[leef_index.find(":") + 1:]

        if leef_version != "1.0" and leef_version != "2.0":
            print("Invalid leef format,  ", message)
            return None

        vendor = infos[1]
        product = infos[2]
        product_version = infos[3]
        event_id = infos[4]

        result[LeefInfo.HEADER_VERSION] = leef_version
        result[LeefInfo.HEADER_PRODUCT] = product
        result[LeefInfo.HEADER_VENDOR] = vendor
        result[LeefInfo.HEADER_EVENT_ID] = event_id
        result[LeefInfo.HEADER_PRODUCT_VERSION] = product_version




        delimiter = LeefInfo.BODY_DELIMITER
        body = ""

        if len(infos) == 7:
            delimiter = infos[5]
            body = infos[6]
        else:
            body = infos[5]

        body_info = body.split(delimiter)

        for kv in body_info:
            i = kv.find("=")
            key = kv[:i]
            value = kv[i + 1:]

            result[key] = value

        return result













class LeefInfo:

    HEADER_DELIMITER = "|"
    BODY_DELIMITER = "\t"


    HEADER_VERSION = "version"
    HEADER_VENDOR = "vendor"
    HEADER_PRODUCT = "product"
    HEADER_PRODUCT_VERSION = "product_version"
    HEADER_EVENT_ID = "event_id"

    HEADER_CUSTOM_DELIMITER = "delimiter"


