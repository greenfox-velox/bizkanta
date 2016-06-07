from tkinter import *

# hero_img = PhotoImage(file = 'hero-down.png')

class Tile(object):
    def __init__(self, x, y, canvas):
        self.x = x
        self.y = y
        self.offset = 72
        self.canvas = canvas
        self.wall_img = PhotoImage(file = 'wall.png')
        self.floor_img = PhotoImage(file = 'floor.png')

    def draw_image(self, img):
        self.canvas.create_image(self.x * self.offset, self.y * self.offset, image = img, anchor = NW)

class Floor(Tile):
    def __init__(self, x, y, canvas):
        super().__init__(x, y, canvas)

    def draw(self):
        self.draw_image(self.floor_img)

class Wall(Tile):
    def __init__(self, x, y, canvas):
        super().__init__(x, y, canvas)

    def draw(self):
        self.draw_image(self.wall_img)
