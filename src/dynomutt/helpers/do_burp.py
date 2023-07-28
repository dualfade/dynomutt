#!/usr/bin/env python3
# do_burp.py

import sys

from modules import logging_handler


class BurpParser:
    """class BurpParser"""

    def __init__(self, filename):
        """init options import and parse; return to main"""

        self.filename = filename

    def parse(self):
        """parse burp raw file input, by index; pull required
        values to re establish a new authenticated session to the target system --"""

        try:
            with open(self.filename, 'r') as f:
                enum = f.read().splitlines()

            burp_values = []
            for index, value in enumerate(enum, start=0):
                burp_values.append(value)

            # ret --
            return burp_values

        except IOError as err:
            logging_handler.error(err)

    def get_vals(self):
        """get burp header value --"""

        # get required headers --
        # if burp_vals:
        #     host = burp_vals[1].split()
        #     user_agent = burp_vals[2].split()
        #     sec_webSocket_version = burp_vals[6].split()
        #     origin = burp_vals[7].split()
        #     sec_websocket_protocol = burp_vals[8].split()
        #     web_socket_key = burp_vals[9].split()
        #     cookie = burp_vals[11].split()
        #     upgrade = burp_vals[18].split()

        #     # verbose by default --
        #     if (options.verbose == True):
        #         logging.info(host)
        #         logging.info(user_agent)
        #         logging.info(sec_webSocket_version)
        #         logging.info(origin)
        #         logging.info(sec_websocket_protocol)
        #         logging.info(web_socket_key)
        #         logging.info(cookie)
        #         logging.info(upgrade)
        #     else:
        #         pass

        # else:
        #     logging.info('[info] user defined args')
