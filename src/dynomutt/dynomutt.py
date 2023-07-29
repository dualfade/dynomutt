#!/usr/bin/env python3
# dynomutt.py

# WARN: websockets is not current from archlinux repos,
# it is missing sync.client --
# pip install websockets bottle --user
# websockets 11.0.3

# NOTE: testing --
# https://github.com/interference-security/DVWS/ --
# https://zero-s4n.hashnode.dev/fuzzing-websocket-messages-on-burpsuite --
# https://github.com/rayhan0x01/nodejs-websocket-sqli --

# NOTE: manually --
# echo -ne '{"auth_user":"YWRtaW4=","auth_pass":"YWRtaW4="}' \
# | rlwrap websocat 'ws://dvws.local:8080/authenticate-user-blind' --async-stdio 2>/dev/null  | html2text

import sys
import argparse

from modules import middleware_handler
from modules import logging_handler
from helpers import do_burp
from helpers import do_examples

# main --
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="dynomutt")

    # bottle opts --
    parser.add_argument("-l", "--lhost", dest="lhost", help="Listen Host")
    parser.add_argument("-p", "--lport", dest="lport", help="Listen Port")
    parser.add_argument("-d", "--debug", action="store_false", dest="debug", help="Enable WebSocket Debug")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable Verbose Mode")

    # websocket opts --
    parser.add_argument("-u", "--url", dest="url", help="Target WebSocket Url")
    parser.add_argument("-k", "--ignore-ssl", action="store_true", dest="ignore_ssl", help="Ignore SSL Warnings")
    parser.add_argument("-t", "--timeout", dest="timeout", type=int, help="WebSocket Open Timeout in seconds")
    parser.add_argument(
        "-H",
        "--headers",
        dest="headers",
        help="Header `Name: Value, Name: Value`, separated by comma.",
    )

    # burp; usage --
    parser.add_argument("-r", "--raw", dest="raw", help="Burp Request File")
    parser.add_argument("-E", "--examples", action="store_true", dest="examples", help="Examples Menu")

    try:
        args = parser.parse_args()
        logging_handler.info("=> Starting dynomutt.py")

        if args.examples:
            do_examples.examples()

        if args.raw:
            do_burp = do_burp.BurpParser(args.raw, args.verbose)
            parsed = do_burp.burp_raw_parse()
            print(parsed)
            sys.exit(0)

        # middleware handler --
        handler = middleware_handler.MiddlewareServer(args.url, args.headers, args.ignore_ssl, args.timeout)
        handler.run(args.lhost, args.lport, args.debug)

    except KeyboardInterrupt:
        logging_handler.error("=> Keyboard interrupt")

    except Exception as err:
        logging_handler.error(err)

    except SystemExit:
        sys.stdout.write("\n")
        sys.stdout.flush()
