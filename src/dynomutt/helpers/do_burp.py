#!/usr/bin/env python3
# do_burp.py

import sys

from modules import logging_handler


class BurpParser:
    """class BurpParser"""

    def __init__(self, filename, verbose):
        """init options import and parse; return to main"""

        self.filename = filename
        self.verbose = verbose

    def burp_raw_parse(self):
        """parse burp raw file input, by index; pull required
        values to re establish a new authenticated session to the target websocket --"""

        try:
            with open(self.filename, 'r') as f:
                enum = f.read().splitlines()

            burp_values = []
            for index, value in enumerate(enum, start=0):
                burp_values.append(value)

            burp_values = list(filter(None, burp_values))
            return burp_values

            # if burp_values:
            #     logging_handler.info("=> BurpParser: parsing burp raw file input !")
            #     host = burp_values[1].split()
            #     user_agent = burp_values[2].split()
            #     sec_webSocket_version = burp_values[6].split()
            #     origin = burp_values[7].split()
            #     sec_websocket_protocol = burp_values[8].split()
            #     web_socket_key = burp_values[9].split()
            #     cookie = burp_values[11].split()
            #     upgrade = burp_values[18].split()

            #     if self.verbose:
            #         logging_handler.info("=> BurpParser: verbose mode enabled !")
            #         logging_handler.info(host)
            #         logging_handler.info(user_agent)
            #         logging_handler.info(sec_webSocket_version)
            #         logging_handler.info(origin)
            #         logging_handler.info(sec_websocket_protocol)
            #         logging_handler.info(web_socket_key)
            #         logging_handler.info(cookie)
            #         logging_handler.info(upgrade)

        except FileNotFoundError as err:
            logging_handler.error(err)

        except IndexError as err:
            logging_handler.error(err)
