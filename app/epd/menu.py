from epd.screen import Screen
from epd.button import Button
import logging
from PIL import Image,ImageDraw,ImageFont
import os

FONT_SIZE = 18

class MenuScreen(Screen):
    def __init__(self, epd, lock_callback, back_callback, shared_drive_callback, shutdown_callback):
        super(MenuScreen, self).__init__()
        self.epd = epd
        self.lock_callback = lock_callback
        self.back_callback = back_callback
        self.shutdown_callback = shutdown_callback
        self.shared_drive_callback = shared_drive_callback
        font_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)))
        self.entry_font = ImageFont.truetype(os.path.join(font_dir, 'Font.ttc'), FONT_SIZE)
        self.image = Image.new('1', (epd.height, epd.width), 255)
        self.draw = ImageDraw.Draw(self.image)    

    def lock(self, btn):
        if self.lock_callback is not None:
            self.busy = True
            btn.draw_inverse(self.draw)
            self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))
            self.lock_callback()

    def back(self, btn):
        if self.back_callback is not None:
            self.busy = True
            btn.draw_inverse(self.draw)
            self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))
            self.back_callback()

    def shared_drive(self, btn):
        if self.shared_drive_callback is not None:
            self.busy = True
            btn.draw_inverse(self.draw)
            self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))
            self.shared_drive_callback()

    def shutdown(self, btn):
        if self.shutdown_callback is not None:
            self.busy = True
            btn.draw_inverse(self.draw)
            self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))
            self.shutdown_callback()

    def draw_page(self):
        self.draw.rectangle([(0,0),(self.epd.height, self.epd.width)], fill = 1)
        for btn in self.buttons:
            btn.draw(self.draw)

        self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))

    def start(self):
        logging.info("init and Clear")

        self.buttons = [
            Button(0, 0, 250, 25, "Back", self.entry_font, self.back),
            Button(0, 25, 250, 25, "Lock", self.entry_font, self.lock),
            Button(0, 50, 250, 25, "Shutdown", self.entry_font, self.shutdown),
            Button(0, 75, 250, 25, "Shared Drive", self.entry_font, self.shared_drive)
        ]

        self.draw_page()

    def end(self):
        pass

    def on_tap(self, x, y):
        for btn in self.buttons:
            btn.try_click(x, y)
