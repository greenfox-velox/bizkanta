from tkinter import *

class Character(object):
    def __init__(self, x, y, canvas):
        self.x = x
        self.y = y
        self.offset = 72
        self.canvas = canvas
        self.hero_img = PhotoImage(file ='hero-down.png')

    def draw_character(self, img):
        self.canvas.create_image(self.x * self.offset, self.y * self.offset, image = img, anchor = NW)

class Hero(Character):
    def __init__(self, x, y, canvas):
        super().__init__(x, y, canvas)

    def draw(self):
        self.draw_character(self.hero_img)
