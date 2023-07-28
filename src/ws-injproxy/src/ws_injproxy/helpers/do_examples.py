#!/usr/bin/env python3
# do_examples.py

import sys


# FIX: usage placeholdr --
def examples():
    """help menu examples --"""
    print('wss_attack_tool:\n')
    print('[usage] python wss_attack_tool.py -l 127.0.0.1 -p 8082 -w wss://example.com/api/wss')
    print('[usage] python wss_attack_tool.py -l 127.0.0.1 -p 8082 --insecure -w wss://example.com/api/wss')
    print('[usage] python wss_attack_tool.py -l 127.0.0.1 -p 8082 -r /tmp/burp.raw')

    # exit --
    sys.exit(-1)
