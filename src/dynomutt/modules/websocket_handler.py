#!/usr/bin/env python3
# websocket_handler.py

import re
import ssl
import signal
import psutil
import asyncio
from websockets.client import connect

from . import logging_handler
import helpers.do_writefile as do_writefile


class WebsocketSendPayload(object):
    """class WebsocketSendPayload"""

    def __init__(self, url, headers, ignore_ssl, timeout, match_string, terminate, outfile, payload):
        """init vars, pass to websocket connect"""

        self.url = url
        self.headers = headers
        self.ignore_ssl = ignore_ssl
        self.timeout = timeout
        self.match_string = match_string
        self.terminate = terminate
        self.outfile = outfile
        self.payload = payload

    async def sendPayload(self):
        """sendPayload url, payload and parsed dict headers"""
        """ client asyncio enabled; https://tinyurl.com/z43vnuwx"""

        """ check incoming request for ws/wss scheme and validate, if match_string is present
        then match response and print to stdout; exit cleanly """

        # headers --
        headers_dict = {}
        if self.headers:
            try:
                header = self.headers.split(',')

                print(header)
                for i in header:
                    key = i.strip()
                    headers_dict[key.split(':')[0]] = key.split(':')[1]

            except IndexError as err:
                logging_handler.error(err)
        else:
            pass

        # ret; headers_dict --
        custom_headers = headers_dict

        # ws open timeout --
        if self.timeout:
            logging_handler.info(f"=> Using timeout: {self.timeout} seconds !")

        # WARN: will needs more testing --
        # testing; https://www.piesocket.com/websocket-tester --
        # encrypted websocket --

        if re.findall(r'^wss://', self.url):
            if self.ignore_ssl:
                logging_handler.info("=> Using wss:// websocket scheme !")
                logging_handler.info("=> Ignoring SSL certificate verification !")

            # set ssl_context --
            ssl_context = ssl.SSLContext()
            ssl_context.verify_mode = ssl.CERT_NONE

            async with connect(
                self.url,
                extra_headers=custom_headers,
                close_timeout=self.timeout,
                ssl=ssl_context,
            ) as websocket:
                try:
                    await websocket.send(self.payload)
                    await asyncio.sleep(0)
                    print(f">>> {self.payload}")

                    resp = await websocket.recv()

                    # FIX: need to check / move this if statement --
                    # FIX: same with below; needs refactor --
                    if self.outfile:
                        """write output to file"""

                        w = do_writefile.Writefile(self.outfile, self.payload, resp)
                        w.writefile()

                    else:
                        pass

                    if self.match_string:
                        m = re.search(self.match_string, resp)
                        if m is not None:
                            print(f"<<< {resp}")
                            match_response(m, self.match_string, self.payload)

                            # HACK: https://github.com/bottlepy/bottle/issues/1229 --
                            if self.terminate:
                                logging_handler.warn("=> Termination Flag Detected !")
                                logging_handler.warn("=> Exiting !")
                                current_process = psutil.Process()
                                current_process.send_signal(signal.SIGTERM)
                            else:
                                pass

                    else:
                        print(f"<<< {resp}")

                except ConnectionError as err:
                    print(f"ConnectionError: {err}")
                    pass

        # unencrypted websocket --
        if re.findall(r'^ws://', self.url):
            logging_handler.info("=> Using ws:// websocket scheme !")
            async with connect(
                self.url,
                extra_headers=custom_headers,
                close_timeout=self.timeout,
                ssl=None,
            ) as websocket:
                try:
                    await websocket.send(self.payload)
                    await asyncio.sleep(0)
                    print(f">>> {self.payload}")

                    resp = await websocket.recv()

                    if self.outfile:
                        """write output to file"""

                        w = do_writefile.Writefile(self.outfile, self.payload, resp)
                        w.writefile()

                    else:
                        pass

                    if self.match_string:
                        m = re.search(self.match_string, resp)
                        if m is not None:
                            print(f"<<< {resp}")
                            match_response(m, self.match_string, self.payload)

                            # HACK: https://github.com/bottlepy/bottle/issues/1229 --
                            if self.terminate:
                                logging_handler.warn("=> Termination Flag Detected !")
                                logging_handler.warn("=> Exiting !")
                                current_process = psutil.Process()
                                current_process.send_signal(signal.SIGTERM)
                            else:
                                pass

                    else:
                        print(f"<<< {resp}")

                except ConnectionError as err:
                    print(f"ConnectionError: {err}")
                    pass


def match_response(*args, **kwargs):
    """match_response standard output"""

    m = args[0]
    match_string = args[1]
    payload = args[2]

    logging_handler.info(f"=> Match String: {match_string} !")
    logging_handler.info(f"=> Match Detected: {m} !")
    logging_handler.info(f"=> Payload: {payload} !")
