from epd.entry import EntryScreen
from epd.select import SelectScreen
from epd.item import ItemScreen
from epd.lib.epd2in13_V3 import EPD
from epd.lib.gt1151 import GT1151, GT_Development
from passwords.store import Store
import RPi.GPIO as GPIO
from threading import Condition, Thread
from queue import Queue, Empty
import logging
import time
import signal

DATABASE="/home/passman/database/passman.kdbx"

class Main(object):
    def __init__(self):
        self.gt = GT1151()
        self.GT_Dev = GT_Development()
        self.GT_Old = GT_Development()
        self.epd = EPD()
        self.store = None
        self.event_queue = Queue()
        self.running = True
        self.touched = Condition()
        self.touch_thread = None
        self.pressed = False
        self.dragging = False
        self.busy = False


    def on_gpio_change(self, channel) :
        logging.debug("Edge detected")
        if(self.gt.digital_read(self.gt.INT) == 0) :
            with self.touched:
                self.GT_Dev.Touch = 1
                logging.debug("Signalling")
                self.touched.notify()
        else :
            logging.debug("Zero")
            self.GT_Dev.Touch = 0

    def touch_loop(self):
        try:
            while self.running:
                with self.touched:
                    while self.GT_Dev.Touch != 1 and self.running:
                        self.touched.wait(timeout=1)
                    logging.debug("Scan")
                    self.gt.GT_Scan(self.GT_Dev, self.GT_Old)

                    if self.GT_Dev.TouchCount == 0:
                        if self.pressed:
                            logging.debug("Lifted: cnt: %d, flag: %d, x: %d, y: %d, s: %d" % (self.GT_Dev.TouchCount, self.GT_Dev.TouchpointFlag, self.GT_Dev.X[0], self.GT_Dev.Y[0], self.GT_Dev.S[0]))
                            if not self.dragging:
                                event = {
                                        "x": self.GT_Dev.X[0],
                                        "y": self.GT_Dev.Y[0],
                                        "s": self.GT_Dev.S[0]
                                }
                                logging.debug("Queuing event")
                                if self.current_screen.busy:
                                    logging.debug("Dropping touch event while busy")
                                else:
                                    self.event_queue.put(event)
                            
                        else:
                            logging.debug("Unexpected: cnt: %d, flag: %d, x: %d, y: %d, s: %d" % (self.GT_Dev.TouchCount, self.GT_Dev.TouchpointFlag, self.GT_Dev.X[0], self.GT_Dev.Y[0], self.GT_Dev.S[0]))
                        self.dragging = False
                        self.pressed = False
                    else:
                        if not self.pressed:
                            logging.debug("Pressed: cnt: %d, flag: %d, x: %d, y: %d, s: %d" % (self.GT_Dev.TouchCount, self.GT_Dev.TouchpointFlag, self.GT_Dev.X[0], self.GT_Dev.Y[0], self.GT_Dev.S[0]))
                        else:
                            if(self.GT_Old.X[0] != self.GT_Dev.X[0] or self.GT_Old.Y[0] != self.GT_Dev.Y[0] or self.GT_Old.S[0] != self.GT_Dev.S[0]):
                                self.dragging = True
                                logging.debug("Dragged: cnt: %d, flag: %d, x: %d, y: %d, s: %d" % (self.GT_Dev.TouchCount, self.GT_Dev.TouchpointFlag, self.GT_Dev.X[0], self.GT_Dev.Y[0], self.GT_Dev.S[0]))
                        self.pressed = True
        except Exception as e:
            logging.error(e)
            self.running = False

    def on_passcode(self, passcode):
        logging.debug("Loading")
        self.current_screen.end()
        self.store = Store(DATABASE)
        if self.store.open(passcode):
            self.current_screen = SelectScreen(self.epd, self.store, self.on_lock, self.on_select_item)
        else:
            self.current_screen = EntryScreen(self.epd, self.on_passcode)
        self.current_screen.start()

    def on_lock(self):
        self.current_screen.end()
        self.current_screen = EntryScreen(self.epd, self.on_passcode)
        self.current_screen.start()

    def on_select_item(self, name):
        self.current_screen.end()
        self.current_screen = ItemScreen(self.epd, self.store, name, self.on_item_back)
        self.current_screen.start()

    def on_item_back(self):
        self.current_screen.end()
        self.current_screen = SelectScreen(self.epd, self.store, self.on_lock, self.on_select_item)
        self.current_screen.start()

    def on_ctrl_c(self, sig, frame):
        logging.warning("CTRL-C")
        self.running = False

    def run(self):
        try:
            self.epd.init(self.epd.FULL_UPDATE)
            self.gt.GT_Init()
            self.gt.GT_Reset()
            self.current_screen = EntryScreen(self.epd, self.on_passcode)
            self.current_screen.start()

            self.touch_thread = Thread(target=self.touch_loop)
            self.touch_thread.start()
            GPIO.add_event_detect(self.gt.INT, GPIO.BOTH, callback=self.on_gpio_change)

            signal.signal(signal.SIGINT, self.on_ctrl_c)
            while(self.running):
                try:
                    evt = self.event_queue.get(timeout=1)
                    logging.debug("Got event")
                    self.current_screen.on_tap(250-evt['y'], evt['x'])
                except Empty:
                    pass

        except Exception as e:
            logging.error(e)

        self.running = False
        self.epd.sleep()
        time.sleep(2)
        self.touch_thread.join()
        self.epd.Dev_exit()

logging.basicConfig(level=logging.INFO)
Main().run()