from epd.screen import Screen
from epd.button import Button
import logging
from PIL import Image,ImageDraw,ImageFont
import os

class EntryScreen(Screen):
    def __init__(self, epd, callback):
        super(EntryScreen, self).__init__()
        self.epd = epd
        self.callback = callback
        font_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)))
        self.font15 = ImageFont.truetype(os.path.join(font_dir, 'Font.ttc'), 32)
        self.button_font = ImageFont.truetype(os.path.join(font_dir, 'Font.ttc'), 24)
        self.star_font = ImageFont.truetype(os.path.join(font_dir, 'Font.ttc'), 15)
        
        self.image = Image.new('1', (epd.height, epd.width), 255)
        self.draw = ImageDraw.Draw(self.image)

        self.pass_code = ""  

    def show_pass_code(self):
        self.draw.rectangle([(0,0),(self.epd.height, 21)], fill = 1)
        hidden_code = '*'*(len(self.pass_code)-1) + self.pass_code[-1:]
        self.draw.text((0,0), hidden_code, font = self.star_font, fill = 0)
        self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))

    def add_number(self, btn, num):
        self.pass_code += str(num)
        self.show_pass_code()

    def start(self):
        logging.info("init and Clear")
        
        self.buttons = [
            Button(0,   22, 40, 50, "0", self.button_font, lambda btn: self.add_number(btn, 0)),
            Button(40,  22, 40, 50, "1", self.button_font, lambda btn: self.add_number(btn, 1)),
            Button(80,  22, 40, 50, "2", self.button_font, lambda btn: self.add_number(btn, 2)),
            Button(120, 22, 40, 50, "3", self.button_font, lambda btn: self.add_number(btn, 3)),
            Button(160, 22, 40, 50, "4", self.button_font, lambda btn: self.add_number(btn, 4)),

            Button(0,   72, 40, 50, "5", self.button_font, lambda btn: self.add_number(btn, 5)),
            Button(40,  72, 40, 50, "6", self.button_font, lambda btn: self.add_number(btn, 6)),
            Button(80,  72, 40, 50, "7", self.button_font, lambda btn: self.add_number(btn, 7)),
            Button(120, 72, 40, 50, "8", self.button_font, lambda btn: self.add_number(btn, 8)),
            Button(160, 72, 40, 50, "9", self.button_font, lambda btn: self.add_number(btn, 9)),

            Button(200, 22,  40, 50, "Clr", self.button_font, lambda btn: self.clear(btn)),
            Button(200, 72, 40, 50, "OK",  self.button_font, lambda btn: self.ok(btn)),
        ]

        for btn in self.buttons:
            btn.draw(self.draw)

        self.epd.init(self.epd.FULL_UPDATE)
        self.epd.displayPartBaseImage(self.epd.getbuffer(self.image))
        self.epd.init(self.epd.PART_UPDATE)

    def clear(self, btn):
        self.busy = True
        btn.draw_inverse(self.draw)
        self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))
        self.pass_code = ""
        self.show_pass_code()
        btn.draw(self.draw)
        self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))
        self.busy = False

    def ok(self, btn):
        self.busy = True
        btn.draw_inverse(self.draw)
        self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))
        self.callback(self.pass_code)

    def end(self):
        self.draw.rectangle([(0,0),(self.epd.height, 21)], fill = 1)
        self.draw.text((0,0), "Opening...", font = self.star_font, fill = 0)
        self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))

    def on_tap(self, x, y):
        for btn in self.buttons:
            btn.try_click(x, y)
