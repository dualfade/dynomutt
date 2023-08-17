#!/usr/bin/env python3
# do_examples.py

import sys


# FIX: usage placeholdr --
def examples():
    """help menu examples --"""

    print(
        """
hatch run default:python src/dynomutt/dynomutt.py -e

=> Dynomutt Examples:
[usage] dynomutt.py -l '127.0.0.1' -p '8082' -u 'ws://dvws.local:8080/reflected-xss'
[usage] dynomutt.py -l '127.0.0.1' -p '8082' -u 'ws://dvws.local:8080/authenticate-user-blind' -d -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36' -t 30
[usage] dynomutt.py -l '127.0.0.1' -p '8002' -u 'wss://dvws.local:8080/file-inclusion' -d -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c, User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36' -k -t 30
[usage] dynomutt.py -l '127.0.0.1' -p '8000' -u 'ws://dvws.local:8080/command-execution' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36' -t 30 -v --ms 'TJE\w.*?$' --te
[usage] dynomutt.py -l '127.0.0.1' -p '8000' -u 'ws://dvws.local:8080/file-inclusion' -d -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36' -t 5 -v --ms 'ro\w.*?$' -o /tmp/file_inclusion_fuzz.txt

=> HTTP Verb CRUD Operations:
[listener] http://127.0.0.1:8082/<path:path>
[listener] http://127.0.0.1:8082/param?data=<injection>

=> Sqlmap Example with Listener
python sqlmap.py -u 'http://127.0.0.1:8082/param?' --data='{"auth_user":"*","auth_pass":"YWRtaW4="}' --tamper base64encode --dbms mysql --risk 3 --level 5 --method POST

=> Ffuf using custom command file-inclusion wordlist
ffuf -X GET -u 'http://127.0.0.1:8082/pages/FUZZ' -w /tmp/0.txt -mc all -fc 500

=> Ffuf special char encoded injection, command injection test
pencode -input ${PWD}/specialchars.txt urlencode | ffuf -X GET -u 'http://127.0.0.1:8082/param?data=127.0.0.1FUZZcat%20/etc/hosts' -w - -mc all -fc 404 -t 3
ffuf -u 'http://127.0.0.1:8000/param?data=127.0.0.1FUZZ' -w ~/Github/custom_list/wordlists/SecLists/Fuzzing/command-injection-commix.txt -t 1 -rate 1

=> Dalfox reflected xss
dalfox -X GET url 'http://127.0.0.1:8000/param?data=Dalfox' --cookie 'PHPSESSID=sp9a9c746au3osa8maj53km312'
          """
    )

    # exit --
    sys.exit(-1)
