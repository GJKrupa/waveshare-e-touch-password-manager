from epd.screen import Screen
from epd.button import Button
import logging
from PIL import Image,ImageDraw,ImageFont
import os

FONT_SIZE = 18
BUTTON_HEIGHT = 25
PAGE_SIZE = 5

class SelectScreen(Screen):
    def __init__(self, epd, keepass, menu_callback, select_callback):
        super(SelectScreen, self).__init__()
        self.epd = epd
        self.menu_callback = menu_callback
        self.select_callback = select_callback
        self.keepass = keepass
        font_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)))
        self.entry_font = ImageFont.truetype(os.path.join(font_dir, 'Font.ttc'), FONT_SIZE)
        self.image = Image.new('1', (epd.height, epd.width), 255)
        self.draw = ImageDraw.Draw(self.image)    

        titles = keepass.entry_names()
        self.pages = [titles[i:i+PAGE_SIZE] for i in range(0, len(titles), PAGE_SIZE)]
        self.page_num = 0

    def select_item(self, btn, title):
        logging.info("Selected %s" % (title))
        if self.select_callback is not None:
            self.busy = True
            btn.draw_inverse(self.draw)
            self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))
            self.select_callback(title)

    def page_up(self):
        if self.page_num > 0:
            self.busy = True
            self.page_num = self.page_num - 1
            self.draw_page()
            self.busy = False

    def page_down(self):
        if self.page_num < len(self.pages)-1:
            self.busy = True
            self.page_num = self.page_num + 1
            self.draw_page()
            self.busy = False

    def menu(self):
        self.busy = True
        self.menu_callback()

    def draw_page(self):
        self.buttons = []
        if self.page_num >= 0 and self.page_num < len(self.pages):
            y_index = 0
            for title in self.pages[self.page_num]:
                self.buttons.append(
                    Button(
                        0, y_index, 200, BUTTON_HEIGHT, title, self.entry_font, lambda btn,title=title: self.select_item(btn, title)
                    )
                )
                y_index += BUTTON_HEIGHT

            if self.page_num > 0:
                self.buttons.append(
                    Button(
                        210, 0, 40, 40, "Up", self.entry_font, lambda btn: self.page_up()
                    )
                )

            self.buttons.append(
                Button(
                    210, 41, 40, 40, "Menu", self.entry_font, lambda btn: self.menu()
                )
            )

            if self.page_num < len(self.pages)-1:
                self.buttons.append(
                    Button(
                        210, 82, 40, 40, "Dn", self.entry_font, lambda btn: self.page_down()
                    )
                )

        self.draw.rectangle([(0,0),(self.epd.height, self.epd.width)], fill = 1)
        for btn in self.buttons:
            btn.draw(self.draw)

        self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))

    def start(self):
        logging.info("init and Clear")
        self.draw_page()

    def end(self):
        pass

    def on_tap(self, x, y):
        for btn in self.buttons:
            btn.try_click(x, y)
