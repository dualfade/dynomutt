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
pip install dynomutt
```

## Usage

```usage
dynomutt[main] % python src/dynomutt/dynomutt.py -h
Usage: dynomutt.py [options]

Options:
  -h, --help            show this help message and exit
  -l LHOST, --lhost=LHOST
                        Listen Host
  -p LPORT, --lport=LPORT
                        Listen Port
  -d, --debug           Enable Debug
  -u URL, --url=URL     Target WebSocket Url
  -k, --ignore-ssl      Ignore SSL
  -t TIMEOUT, --timeout=TIMEOUT
                        WebSocket Open Timeout in seconds
  -H HEADERS, --headers=HEADERS
                        Header `Name: Value, Name: Value`, separated by comma.
  -r RAW, --raw=RAW     Burp Request File
  -E, --examples        Examples Menu

dynomutt[main] %
```

## Notes

- This is a new project in development, Please do not use yet.
- Dynomutt uses asyncio websockets.
- Dynomutt uses bottle as middleware routing and a asyncronous gevent listener.
- Two dedicated injection endpoints, one dynamic and one parameterized.
- All HTTP verbs supported, main focus is WebSocket CRUD injection.
- WebSocket Headers and Authorization schemes.
- WebSocket Proxy token?= support.
- More to come.

## License

`dynomutt` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
