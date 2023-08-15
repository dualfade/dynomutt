# dynomutt

#### Asynchronous WebSocket Injection Middleware

![image](https://github.com/dualfade/dynomutt/assets/2522757/c017f4aa-dce0-4bff-9e69-ce77f726b0b1)

[![PyPI - Version](https://img.shields.io/pypi/v/dynomutt.svg)](https://pypi.org/project/dynomutt)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dynomutt.svg)](https://pypi.org/project/dynomutt)

---

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Notes](#notes)
- [To Do](#todo)
- [Screenshots](#screenshots)
- [License](#license)

## Installation

```console
in development:
```

## Usage

```usage
hatch run python src/dynomutt/dynomutt.py -h
usage: dynomutt [-h] [-l LHOST] [-p LPORT] [-u URL] [-H HEADERS] [-d] [-v] [-k] [-t TIMEOUT] [--ms MATCH_STRING] [-e]

Asynchronous Websocket Injection Middleware

options:
  -h, --help            show this help message and exit
  -l LHOST, --lhost LHOST
                        Listen Host
  -p LPORT, --lport LPORT
                        Listen Port
  -u URL, --url URL     Target WebSocket Url
  -H HEADERS, --headers HEADERS
                        Header `Name: Value, Name: Value`, separated by comma.
  -d, --debug           Enable Bottle Debug
  -v, --verbose         Enable Verbose Mode
  -k, --ignore-ssl      Ignore SSL Warnings
  -t TIMEOUT, --timeout TIMEOUT
                        WebSocket Timeout in seconds
  --ms MATCH_STRING     Match Response String
  -e, --examples        Examples Menu
```

## Examples

```examples
hatch run default:python src/dynomutt/dynomutt.py -e

=> Dynomutt Examples:
[usage] dynomutt.py -l '127.0.0.1' -p '8082' -u 'ws://dvws.local:8080/reflected-xss'
[usage] dynomutt.py -l '127.0.0.1' -p '8082' -u 'ws://dvws.local:8080/authenticate-user-blind' -d -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36' -t 30
[usage] dynomutt.py -l '127.0.0.1' -p '8002' -u 'wss://dvws.local:8080/file-inclusion' -d -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c, User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36' -k -t 30
[usage] dynomutt.py -l '127.0.0.1' -p '8000' -u 'ws://dvws.local:8080/command-execution' -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36' -t 30 -v --ms 'TJE\w.*?$'

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

```

## Notes

- **This project in development, please use at own discretion.**
- A few highlights:

  - It's fast.
  - Dynomutt uses asyncio websockets.
  - Dynomutt uses bottle as middleware routing and an asynchronous gevent listener.
  - Two dedicated injection endpoints, one dynamic and one parameterized.
  - All HTTP verbs supported, main focus is WebSocket CRUD injection.
  - WebSocket Headers and Authorization schemes.
  - WebSocket Proxy token?= support.
  - More ?

- Up front; I am not a developer.
- There is no time to fool around with lots of semi working tools on a live engagement, which is how this
  project came to be.

## ToDo

- All initial testing has been done against OWASP dvws.
  - Additional testing (shown in screenshots):
  - [nodejs-websocket-sqli](https://github.com/rayhan0x01/nodejs-websocket-sqli)
- Needs testing against functinal entity with Authorization Tokens and Secure Socket Layer.
- Needs testing against modern wss:// ?token=
- Auto update index route.
- Finish Burp raw integration.
  - may not do this ? Most tools support this already?
- Fix XSS injection, as this sorta works.
- Fix args ordering.
- Probabaly a metric shit ton more, and as we go they say..

## Screenshots

```
Dynomutt Middleware Server --
hatch run default:python src/dynomutt/dynomutt.py -l '127.0.0.1' -p '8000' -u 'ws://localhost:8156/ws' -d -H 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36' -t 30

Sqlmap --
python sqlmap.py -u 'http://127.0.0.1:8000/param?' --data '{"employeeID":"*"}' --dbms mysql --risk 3 --level 5
```

![2023-08-12_21-23_1](https://github.com/dualfade/dynomutt/assets/2522757/1469d46e-6959-4867-a7e8-af35319c1883)
![2023-08-12_21-23](https://github.com/dualfade/dynomutt/assets/2522757/0be4b41d-768d-4eb2-a057-1ec3411dcd5c)

## License

`dynomutt` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

[![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
