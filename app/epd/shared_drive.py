from epd.screen import Screen
from epd.button import Button
import logging
from PIL import Image,ImageDraw,ImageFont
import os
import dbus
import pprint

class SharedDriveScreen(Screen):
    def __init__(self, epd, back_callback, message = None):
        super(SharedDriveScreen, self).__init__()
        self.epd = epd
        self.back_callback = back_callback
        self.message = message
        font_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)))
        self.entry_font = ImageFont.truetype(os.path.join(font_dir, 'Font.ttc'), 18)
        self.message_font = ImageFont.truetype(os.path.join(font_dir, 'Font.ttc'), 13)
        self.image = Image.new('1', (epd.height, epd.width), 255)
        self.draw = ImageDraw.Draw(self.image)   
        self.enabled = False 

    def back(self, btn):
        if self.back_callback is not None:
            self.busy = True
            btn.draw_inverse(self.draw)
            self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))
            self.back_callback()

    def start_samba(self):
        sysbus = dbus.SystemBus()
        systemd1 = sysbus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
        manager = dbus.Interface(systemd1, 'org.freedesktop.systemd1.Manager')
        job = manager.StartUnit('smbd.service', 'replace')
        pprint.pprint(job)

    def stop_samba(self):
        sysbus = dbus.SystemBus()
        systemd1 = sysbus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
        manager = dbus.Interface(systemd1, 'org.freedesktop.systemd1.Manager')
        job = manager.StopUnit('smbd.service', 'replace')
        pprint.pprint(job)

    def toggle(self, btn):
        if self.enabled:
            self.busy = True
            self.enabled = False
            btn.draw(self.draw)
            self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))
            self.stop_samba()
            self.busy = False
        else:
            self.busy = True
            self.enabled = True
            btn.draw_inverse(self.draw)
            self.epd.displayPartial_Wait(self.epd.getbuffer(self.image))
            self.start_samba()
            self.busy = False

    def draw_page(self):
        self.draw.rectangle([(0,0),(self.epd.height, self.epd.width)], fill = 1)

        if self.message is not None:
            self.draw.text((0,0), self.message, font = self.message_font, fill = 0)

        for btn in self.buttons:
            btn.draw(self.draw)

        self.epd.init(self.epd.FULL_UPDATE)
        self.epd.displayPartBaseImage(self.epd.getbuffer(self.image))
        self.epd.init(self.epd.PART_UPDATE)

    def start(self):
        logging.info("init and Clear")

        self.buttons = [
            Button(10, 15, 105, 102, "Enable", self.entry_font, self.toggle),
            Button(125, 15, 105, 102, "Back", self.entry_font, self.back)
        ]

        self.draw_page()

    def end(self):
        self.stop_samba()
        pass

    def on_tap(self, x, y):
        for btn in self.buttons:
            btn.try_click(x, y)
