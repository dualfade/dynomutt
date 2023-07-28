#!/usr/bin/env python3
# do_examples.py

import sys


# FIX: usage placeholdr --
def examples():
    """help menu examples --"""
    print('python dynomutt.py -h')
    print('\n=> Dynomutt Examples:')
    print("[usage] python dynomutt.py -l '127.0.0.1' -p '8082' -u 'ws://dvws.local:8080/reflected-xss'")
    print(
        "[usage] python dynomutt.py -l '127.0.0.1' -p '8082' -u 'ws://dvws.local:8080/authenticate-user-blind' -d -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36' -t 30"
    )
    print(
        "[usage] python dynomutt.py -l '127.0.0.1' -p '8002' -u 'wss://dvws.local:8080/file-inclusion' -d -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c, User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36' -k -t 30"
    )

    print('\n=> HTTP Verb CRUD Operations:')
    print('[listener] http://127.0.0.1:8082/param?inj=1&inj=2')
    print('[listener] http://127.0.0.1:8082//<path:path>')

    print("\n=> Sqlmap Example with Listener")
    print(
        "python sqlmap.py -u 'http://127.0.0.1:8082/param?' --data='{\"auth_user\":\"*\",\"auth_pass\":\"YWRtaW4=\"}' --tamper base64encode --dbms mysql --risk 3 --level 5 --method POST"
    )
    print("\n=> Ffuf using custom command file-inclusion wordlist")
    print("ffuf -X GET -u 'http://127.0.0.1:8082/pages/FUZZ' -w /tmp/0.txt -mc all -fc 500")
    print("\n=> Ffuf special char encoded injection, command injection test")
    print(
        "pencode -input ${PWD}/specialchars.txt urlencode | ffuf -X GET -u 'http://127.0.0.1:8082/param?data=127.0.0.1FUZZcat%20/etc/hosts' -w - -mc all -fc 404 -t 3"
    )

    # exit --
    sys.exit(-1)
