#!/usr/bin/env python3
# websocket_handler.py

import re
import ssl
import asyncio
from websockets.client import connect

from . import logging_handler


class WebsocketSendPayload(object):
    """class WebsocketSendPayload"""

    def __init__(self, url, headers, ignore_ssl, timeout, payload):
        """init vars, pass to websocket connect"""

        self.url = url
        self.headers = headers
        self.ignore_ssl = ignore_ssl
        self.timeout = timeout
        self.payload = payload

    async def sendPayload(self):
        """sendPayload url, payload and parsed dict headers"""
        """ client asyncio enabled; https://tinyurl.com/z43vnuwx"""

        # headers --
        headers_dict = {}
        if self.headers:
            try:
                header = self.headers.split(',')

                # FIX: breaking; index err --
                # WARN: huh ? magically working ?? --
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

        # WARN: will need testing --
        # ssl ? self.ignore_ssl --
        if re.findall(r'^wss://', self.url):
            if self.ignore_ssl:
                logging_handler.info("=> Using wss:// protocol !")
                logging_handler.warn("=> Ignoring SSL certificate verification !")
                ssl_context = ssl.SSLContext()
                ssl_context.verify_mode = ssl.CERT_NONE

        if re.findall(r'^ws://', self.url):
            logging_handler.info("=> Using ws:// protocol !")

        if self.timeout:
            logging_handler.info(f"=> Using timeout: {self.timeout} seconds !")

        # NOTE: client.connect --
        async with connect(self.url, extra_headers=custom_headers, open_timeout=self.timeout, ssl=None) as websocket:
            try:
                await websocket.send(self.payload)
                await asyncio.sleep(0)
                print(f">>> {self.payload}")

                resp = await websocket.recv()
                print(f"<<< {resp}")

            except ConnectionError as err:
                print(f"ConnectionError: {err}")
                pass
