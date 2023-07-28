# dynomutt

#### WebSocket Injection Middleware

![image](https://github.com/dualfade/dynomutt/assets/2522757/c017f4aa-dce0-4bff-9e69-ce77f726b0b1)

[![PyPI - Version](https://img.shields.io/pypi/v/dynomutt.svg)](https://pypi.org/project/dynomutt)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dynomutt.svg)](https://pypi.org/project/dynomutt)

---

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
in development please disregard:
pip install dynomutt
```

## Usage

```usage
usage: dynomutt.py [-h] [-l LHOST] [-p LPORT] [-d] [-v] [-u URL] [-k] [-t TIMEOUT] [-H HEADERS] [-r RAW] [-E]

dynomutt

options:
  -h, --help            show this help message and exit
  -l LHOST, --lhost LHOST
                        Listen Host
  -p LPORT, --lport LPORT
                        Listen Port
  -d, --debug           Enable WebSocket Debug
  -v, --verbose         Enable Verbose Mode
  -u URL, --url URL     Target WebSocket Url
  -k, --ignore-ssl      Ignore SSL Warnings
  -t TIMEOUT, --timeout TIMEOUT
                        WebSocket Open Timeout in seconds
  -H HEADERS, --headers HEADERS
                        Header `Name: Value, Name: Value`, separated by comma.
  -r RAW, --raw RAW     Burp Request File
  -E, --examples        Examples Menu
```

## Examples

```examples
python dynomutt.py -h

=> Dynomutt Examples:
[usage] python dynomutt.py -l '127.0.0.1' -p '8082' -u 'ws://dvws.local:8080/reflected-xss'
[usage] python dynomutt.py -l '127.0.0.1' -p '8082' -u 'ws://dvws.local:8080/authenticate-user-blind' -d -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36' -t 30
[usage] python dynomutt.py -l '127.0.0.1' -p '8002' -u 'wss://dvws.local:8080/file-inclusion' -d -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c, User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36' -k -t 30

=> HTTP Verb CRUD Operations:
[listener] http://127.0.0.1:8082/param?inj=1&inj=2
[listener] http://127.0.0.1:8082//<path:path>

=> Sqlmap Example with Listener
python sqlmap.py -u 'http://127.0.0.1:8082/param?' --data='{"auth_user":"*","auth_pass":"YWRtaW4="}' --tamper base64encode --dbms mysql --risk 3 --level 5 --method POST

=> Ffuf using custom command file-inclusion wordlist
ffuf -X GET -u 'http://127.0.0.1:8082/pages/FUZZ' -w /tmp/0.txt -mc all -fc 500

 Ffuf special char encoded injection, command injection test
pencode -input ${PWD}/specialchars.txt urlencode | ffuf -X GET -u 'http://127.0.0.1:8082/param?data=127.0.0.1FUZZcat%20/etc/hosts' -w - -mc all -fc 404 -t 3

```

## Notes

- **This is a new project in development, Please do not use yet.**
- A few highlights:
  - Dynomutt uses asyncio websockets.
  - Dynomutt uses bottle as middleware routing and an asyncronous gevent listener.
  - Two dedicated injection endpoints, one dynamic and one parameterized.
  - All HTTP verbs supported, main focus is WebSocket CRUD injection.
  - WebSocket Headers and Authorization schemes.
  - WebSocket Proxy token?= support.
  - More to come.

## To Do

- All initial testing has been done against OWASP dvws.
- Needs testing against functinal entity with Authorization Tokens and Secure Socket Layer.
- Needs testing against modern wss:// ?token=
- Add JSON payload parser.
- Auto update index route.
- Finish Burp raw integration.
- Probabaly a metric shit ton more, and as we go they say..

## License

`dynomutt` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
