#!/usr/bin/env python3
# do_burp.py

import re
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

            # WARN: parse raw input, add as required to list; wip, needs testing --
            if burp_values:
                logging_handler.info("=> BurpParser: parsing burp raw file input !")

                # http verb --
                REQUEST = []
                METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "TRACE", "CONNECT"]
                for index, value in enumerate(METHODS, start=0):
                    r = re.compile(value)
                    verb = list(filter(r.match, burp_values))
                    if verb is not None:
                        REQUEST.append(verb)
                        break

                # ret verb  --
                verb = REQUEST[0]

                # host --
                r = re.compile('Host')
                host = list(filter(r.match, burp_values))
                REQUEST.append(host)

                # user-agent --
                r = re.compile('User-Agent')
                user_agent = list(filter(r.match, burp_values))
                REQUEST.append(user_agent)

                # accept --
                r = re.compile('Accept')
                accept = list(filter(r.match, burp_values))
                REQUEST.append(accept)

                # accept-encoding --
                r = re.compile('Accept-Encoding')
                accept_encoding = list(filter(r.match, burp_values))
                REQUEST.append(accept_encoding)

                # cookie --
                r = re.compile('Cookie')
                cookie = list(filter(r.match, burp_values))
                REQUEST.append(cookie)

                # upgrade --
                r = re.compile('Upgrade-Insecure-Requests')
                upgrade_request = list(filter(r.match, burp_values))
                REQUEST.append(upgrade_request)

                if self.verbose:
                    logging_handler.info("=> BurpParser: verbose mode enabled !")
                    logging_handler.info(verb)
                    logging_handler.info(host)
                    logging_handler.info(user_agent)
                    # logging_handler.info(sec_webSocket_version)
                    # logging_handler.info(origin)
                    # logging_handler.info(sec_websocket_protocol)
                    # logging_handler.info(web_socket_key)
                    logging_handler.info(cookie)
                    logging_handler.info(upgrade_request)

        except FileNotFoundError as err:
            logging_handler.error(err)

        except IndexError as err:
            logging_handler.error(err)

    def burp_sanitized(self):
        """sanitize burp raw file input; remove all '§' template markers"""
