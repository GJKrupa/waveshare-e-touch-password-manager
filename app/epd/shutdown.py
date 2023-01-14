from epd.screen import Screen
from epd.button import Button
import logging
from PIL import Image,ImageDraw,ImageFont
import os

FONT_SIZE = 18

class ShutdownScreen(Screen):
    def __init__(self, epd, back_callback):
        super(ShutdownScreen, self).__init__()
        self.epd = epd
        self.back_callback = back_callback
        font_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)))
        self.entry_font = ImageFont.truetype(os.path.join(font_dir, 'Font.ttc'), FONT_SIZE)
        self.image = Image.new('1', (epd.height, epd.width), 255)
        self.draw = ImageDraw.Draw(self.image)   
        self.enabled = False 

    def back(self, btn):
        if self.back_callback is not None:
            self.busy = True
            btn.draw_inverse(self.draw)
            self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))
            self.back_callback()

    def shutdown(self, btn):
        self.busy = True
        self.draw.rectangle([(0,0),(self.epd.height, self.epd.width)], fill = 1)
        self.draw.text((2, 2), "Shutting Down", font = self.entry_font, fill = 0)
        self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))
        os.system("sudo /usr/sbin/shutdown -h now")

    def draw_page(self):
        self.draw.rectangle([(0,0),(self.epd.height, self.epd.width)], fill = 1)
        for btn in self.buttons:
            btn.draw(self.draw)

        self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))

    def start(self):
        self.buttons = [
            Button(10, 10, 105, 102, "Shutdown", self.entry_font, self.shutdown),
            Button(125, 10, 105, 102, "Back", self.entry_font, self.back)
        ]

        self.draw_page()

    def end(self):
        pass

    def on_tap(self, x, y):
        for btn in self.buttons:
            btn.try_click(x, y)
