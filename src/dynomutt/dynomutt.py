#!/usr/bin/env python3
# dynomutt.py

# WARN: websockets is not current from archlinux repos,
# it is missing sync.client --
# pip install websockets bottle --user
# websockets 11.0.3

# NOTE: testing --
# https://github.com/interference-security/DVWS/ --
# https://github.com/rayhan0x01/nodejs-websocket-sqli --

# NOTE: manually --
# echo -ne '{"auth_user":"YWRtaW4=","auth_pass":"YWRtaW4="}' \
# | rlwrap websocat 'ws://dvws.local:8080/authenticate-user-blind' --async-stdio 2>/dev/null  | html2text

import sys
from optparse import OptionParser

from modules import middleware_handler
from modules import logging_handler
from helpers import do_burp
from helpers import do_examples

# main --
if __name__ == "__main__":
    parser = OptionParser()

    # bottle opts --
    parser.add_option("-l", "--lhost", dest="lhost", help="Listen Host")
    parser.add_option("-p", "--lport", dest="lport", help="Listen Port")
    parser.add_option("-d", "--debug", action="store_false", dest="debug", help="Enable Debug")

    # websocket opts --
    parser.add_option("-u", "--url", dest="url", help="Target Url")
    parser.add_option("-k", "--ignore-ssl", action="store_true", dest="ignore_ssl", help="Ignore SSL")
    parser.add_option("-t", "--timeout", dest="timeout", type="int", help="WebSocket Open Timeout in seconds")
    parser.add_option(
        "-H",
        "--headers",
        dest="headers",
        help="Header `Name: Value, Name: Value`, separated by comma.",
    )

    # burp; usage --
    parser.add_option("-r", "--raw", dest="raw", help="Burp Request File")
    parser.add_option("-E", "--examples", action="store_true", dest="examples", help="Examples Menu")

    try:
        (options, args) = parser.parse_args()
        logging_handler.info("=> Starting ws_injproxy.py")

        if options.examples:
            do_examples.examples()

        if options.raw:
            do_burp = do_burp.BurpParser(options.raw)
            raw = do_burp.parse()
            print(raw)
            sys.exit()

        # middleware handler --
        handler = middleware_handler.MiddlewareServer(options.url, options.headers, options.ignore_ssl, options.timeout)
        handler.run(options.lhost, options.lport, options.debug)

    except KeyboardInterrupt:
        logging_handler.error("=> Keyboard interrupt")

    except Exception as err:
        logging_handler.error(err)

    except SystemExit:
        sys.stdout.write("\n")
        sys.stdout.flush()
