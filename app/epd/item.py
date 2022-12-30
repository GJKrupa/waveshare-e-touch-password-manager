from epd.screen import Screen
from epd.button import Button
import logging
from PIL import Image,ImageDraw,ImageFont
import os
from output.hid import KeyboardWriter

FONT_SIZE = 14
BUTTON_HEIGHT = 25
PAGE_SIZE = 5

class ItemScreen(Screen):
    def __init__(self, epd, keepass, title, back_callback):
        super(ItemScreen, self).__init__()
        self.epd = epd
        self.back_callback = back_callback
        self.keepass = keepass
        font_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)))
        self.entry_font = ImageFont.truetype(os.path.join(font_dir, 'Font.ttc'), FONT_SIZE)
        self.image = Image.new('1', (epd.height, epd.width), 255)
        self.draw = ImageDraw.Draw(self.image)    
        self.keyboard = KeyboardWriter()
        self.title = title

    def type_password(self, btn):
        self.busy = True
        btn.draw_inverse(self.draw)
        self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))
        self.keyboard.type(self.keepass.password(self.title))
        btn.draw(self.draw)
        self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))
        self.busy = False

    def type_username(self, btn):
        self.busy = True
        btn.draw_inverse(self.draw)
        self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))
        self.keyboard.type(self.keepass.username(self.title))
        btn.draw(self.draw)
        self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))
        self.busy = False

    def back(self, btn):
        self.busy = True
        btn.draw_inverse(self.draw)
        self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))
        if self.back_callback is not None:
            self.back_callback()

    def type(self, btn, str):
        self.busy = True
        btn.draw_inverse(self.draw)
        self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))
        self.keyboard.type(str)
        btn.draw(self.draw)
        self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))
        self.busy = False

    def start(self):
        logging.info("init and Clear")
        self.draw.rectangle([(0,0),(self.epd.height, self.epd.width)], fill = 1)

        self.buttons = []

        if self.keepass.username(self.title) is not None:
            self.buttons.append(Button(0, 0, 120, 50, "Username", self.entry_font, self.type_username))
        else:
            self.buttons.append(Button(0, 0, 120, 50, "X No Username X", self.entry_font, lambda btn: 0))

        if self.keepass.password(self.title) is not None:            
            self.buttons.append(Button(120, 0, 120, 50, "Password", self.entry_font, self.type_password))
        else:
            self.buttons.append(Button(120, 0, 120, 50, "X No Pwd X", self.entry_font, lambda btn: 0))

        self.buttons.append(Button(0, 50, 60, 50, "Tab", self.entry_font, lambda btn: self.type(btn, "\t")))
        self.buttons.append(Button(60, 50, 60, 50, "Ent", self.entry_font, lambda btn: self.type(btn, "\n")))
        self.buttons.append(Button(120, 50, 120, 50, "Back", self.entry_font, self.back))

        for btn in self.buttons:
            btn.draw(self.draw)

        self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))

    def end(self):
        pass

    def on_tap(self, x, y):
        for btn in self.buttons:
            btn.try_click(x, y)
