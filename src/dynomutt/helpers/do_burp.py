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
        """parse raw file input, by index; scrub and pull required
        values to re establish a new authenticated session to the target websocket --"""

        """ parse out base http(s) request values from burp raw file input;"""

        try:
            with open(self.filename, 'r') as f:
                enum = f.read().splitlines()

            burp_values = []
            for index, value in enumerate(enum, start=0):
                burp_values.append(value)

            burp_values = list(filter(None, burp_values))

            # WARN: wip, needs testing --
            # parse raw input, add as required to list --
            if burp_values:
                logging_handler.warn("=> BurpParser: parsing burp raw input !")

                # http verbs --
                REQUEST = []
                METHODS = ["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "TRACE", "CONNECT"]
                for index, value in enumerate(METHODS, start=0):
                    r = re.compile(value)
                    verb = scrub(list(filter(r.match, burp_values)))
                    if verb is not None:
                        REQUEST.append(verb)
                        break

                # ret verb  --
                verb = REQUEST[0]

                # host --
                r = re.compile('Host')
                host = scrub(list(filter(r.match, burp_values)))
                REQUEST.append(host)

                r = re.compile('User-Agent')
                user_agent = scrub(list(filter(r.match, burp_values)))
                REQUEST.append(user_agent)

                # cookie --
                r = re.compile('Cookie')
                cookie = scrub(list(filter(r.match, burp_values)))
                REQUEST.append(cookie)

                if self.verbose:
                    logging_handler.warn("=> BurpParser: verbose mode enabled !")
                    logging_handler.info(verb)
                    logging_handler.info(host)
                    logging_handler.info(user_agent)
                    logging_handler.info(cookie)

                # ret base --
                return REQUEST

        except FileNotFoundError as err:
            logging_handler.error(err)

        except IndexError as err:
            logging_handler.error(err)


def scrub(val):
    """scrub burp raw file input; remove all '§' template markers"""

    s = []
    template = '§'

    # loop scrub --
    for index, value in enumerate(val, start=0):
        if re.findall(template, value):
            scrubbed = value.replace(template, '')
            if scrubbed:
                s.append(str(scrubbed))

            # ret list --
            return s
        else:
            return val
