#!/usr/bin/env python3
# middleware_handler.py

# NOTE: theory --
# Connect -> (http/https) -> parse (upgrade) -> (ws/wss) -> proxy
# Connect <-> (ws/wss) -> static

import re
import asyncio
import bottle
from gevent import monkey

from . import logging_handler
from . import websocket_handler

monkey.patch_all()
from bottle import Bottle, route, request, response, run


class MiddlewareServer:
    """MiddlewareServer class"""

    def __init__(self, url, headers, ignore_ssl, timeout):
        self.app = Bottle()
        self.app.install(self.middleware_RequestHandler)
        self.url = url
        self.headers = headers
        self.ignore_ssl = ignore_ssl
        self.timeout = timeout

    def middleware_RequestHandler(self, callback):
        """Middleware Requests function"""

        def wrapper(*args, **kwargs):
            response.headers['X-Custom-Header'] = 'Middleware Server'
            return callback(*args, **kwargs)

        return wrapper

    # index route --
    @route('/index')
    def index(self):
        """show a default index page"""

        #:NOTE: show examples on index page ??
        return "Middleware Server running !"

    @route('/<path:path>')
    def dynamic_handler(self, path):
        """handle dynamic requests"""

        try:
            ws = websocket_handler.WebsocketSendPayload(
                self.url, self.headers, self.ignore_ssl, self.timeout, str(path)
            )
            return asyncio.run(ws.sendPayload())

        except ConnectionError as err:
            logging_handler.error(err)

    @route('/param', method='ANY')
    def param_handler(self):
        """handle parameterized requests"""
        """check incoming request method; verify content-type; send to websocket method"""
        """support standard crud operations """

        # GET --
        if request.method == 'GET':
            try:
                payload = request.query.data  # pyright: ignore
                ws = websocket_handler.WebsocketSendPayload(
                    self.url, self.headers, self.ignore_ssl, self.timeout, str(payload)
                )
                return asyncio.run(ws.sendPayload())

            except ConnectionError as err:
                logging_handler.error(err)

        # POST --
        elif request.method == 'POST':
            if request.forms:
                """forms placeholder"""
            if request.json:
                post_data = str(request.json)

                try:
                    while post_data:
                        payload = re.sub("'", '"', post_data)
                        ws = websocket_handler.WebsocketSendPayload(
                            self.url, self.headers, self.ignore_ssl, self.timeout, str(payload)
                        )
                        return asyncio.run(ws.sendPayload())

                except ConnectionError as err:
                    logging_handler.error(err)

        elif request.method == "PATCH":
            """do_patch functions"""
            logging_handler.info("=> PATCH placeholder")

        elif request.method == "UPDATE":
            """do_options functions"""
            logging_handler.info("=> update placeholder")

        elif request.method == "PUT":
            """do_put functions"""
            logging_handler.info("=> PUT placeholder")

        elif request.method == "DELETE":
            """do_delete functions"""
            logging_handler.info("=> DELETE placeholder")

        elif request.method == "HEAD":
            """do_head functions"""
            logging_handler.info("=> DELETE placeholder")
        else:
            """something is quite not right; issue warning"""
            logging_handler.warn("=> operation not allowed")

    # define routes; run --
    def run(self, lhost, lport, debug) -> None:
        """apply routes, run server"""

        try:
            self.app.route('/')(self.index)  # pyright: ignore
            self.app.route('/param', method='ANY')(self.param_handler)  # pyright: ignore
            self.app.route('/<path:path>', method='ANY')(self.dynamic_handler)  # pyright: ignore
            logging_handler.info("=> Starting MiddlewareServer")

            # debug --
            if debug == True:
                logging_handler.warn("=> Debug enabled")

            # endpoints --
            logging_handler.info(f"=> http://{lhost}:{lport}/<path:path>")
            logging_handler.info(f"=> http://{lhost}:{lport}/param?data=<injection>")

            # gevent; run --
            run(self.app, host=lhost, port=lport, debug=debug, server='gevent')

        except KeyboardInterrupt:
            logging_handler.error("=> Keyboard interrupt")
            pass
        except Exception as err:
            logging_handler.error(err)
