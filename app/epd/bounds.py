import pprint

class Bounds(object):
    def __init__(self, left, top, right, bottom):
        self.left = int(left)
        self.top = int(top)
        self.right = int(right)
        self.bottom = int(bottom)

    def width(self):
        return self.right - self.left

    def height(self):
        return self.bottom - self.top

    def is_in(self, x, y):
        return x >= self.left and x <= self.right and y >= self.top and y <= self.bottom

    def __repr__(self):
        return pprint.pformat({
            "left": self.left,
            "top": self.top,
            "right": self.right,
            "bottom": self.bottom
        })