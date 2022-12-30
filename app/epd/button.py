import logging

class Button(object):
    def __init__(self, x, y, width, height, text, font, callback = None):
        self.callback = callback
        self.left = x
        self.top = y
        self.width = width
        self.height = height
        self.right = x + width
        self.bottom = y + height
        self.text = text
        self.font = font

    def draw(self, drawing):
        drawing.rectangle([(self.left, self.top),(self.right, self.bottom)], outline = 0, fill = 1)
        drawing.text((self.left+2, self.top+2), self.text, font = self.font, fill = 0)

    def draw_inverse(self, drawing):
        drawing.rectangle([(self.left, self.top),(self.right, self.bottom)], fill = 0, outline = 0)
        drawing.text((self.left+2, self.top+2), self.text, font = self.font, fill = 1)

    def is_in(self, x, y):
        return x >= self.left and x <= self.right and y >= self.top and y <= self.bottom

    def try_click(self, x, y):
        if self.is_in(x, y) and self.callback is not None:
            logging.info("Clicking %s: %d,%d -> (%d,%d - %d,%d)" % (self.text, x, y, self.left, self.top, self.right, self.bottom))
            self.callback(self)