#!/usr/bin/env python3
# do_writefile.py

import modules.logging_handler as logging_handler


class Writefile(object):
    """Simple Writefile class"""

    def __init__(self, filename, payload, resp):
        """init vars, pass to writefile"""

        self.filename = filename
        self.payload = payload
        self.resp = resp

    def writefile(self):
        """write outputfile"""
        try:
            with open(self.filename, 'a') as f:
                f.write("Payload => {}\nResponse => {}\n\n".format(self.payload, self.resp))
                f.close()

        except Exception as e:
            logging_handler.warn(f"=> Warning: {e}")
            logging_handler.warn(f"=> Warning: {e.__class__.__name__}")
