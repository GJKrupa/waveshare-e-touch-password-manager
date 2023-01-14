from output.gb import GBKeyboard
import time
import random

KEY_UP = chr(0) * 8

class KeyboardWriter(object):
    def __init__(self):
        self.keyboard = GBKeyboard()

    def type(self, str):
        with open('/dev/hidg0', 'rb+') as fd:
            for key in self.keyboard.encode(str):
                fd.write(key.encode())
                fd.flush()
                time.sleep(0.03)
                fd.write(KEY_UP.encode())
                fd.flush()
                time.sleep(0.03 + random.uniform(0.0, 0.03))
                
        
