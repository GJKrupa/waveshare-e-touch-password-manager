from pykeepass import PyKeePass
from pykeepass.exceptions import CredentialsError

import logging

class Store(object):
    def __init__(self, filename):
        self.filename = filename
        self.keepass = None

    def open(self, passphrase):
        try:
            logging.info("Opening")
            self.keepass = PyKeePass(self.filename, passphrase)
            logging.info("OK")
            return True
        except CredentialsError:
            logging.info("BAD")
            return False
        except:
            logging.info("Unknown error")

    def entry_names(self):
        return [entry.title for entry in self.keepass.entries]

    def password(self, name):
        entry = self.keepass.find_entries(title=name, first=True)
        return entry.password 

    def username(self, name):
        entry = self.keepass.find_entries(title=name, first=True)
        return entry.username 