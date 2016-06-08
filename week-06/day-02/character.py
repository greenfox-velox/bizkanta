from tkinter import *
from gameboard import *

class Character(object):
    def __init__(self, x, y, canvas, game):
        self.x = x
        self.y = y
        self.offset = 72
        self.canvas = canvas
        self.game = game

    def draw_character(self, img):
        self.canvas.create_image(self.x * self.offset, self.y * self.offset, image = img, anchor = NW)

class Hero(Character):
    def __init__(self, x, y, canvas, game):
        super().__init__(x, y, canvas, game)
        self.hero_img = PhotoImage(file ='hero-down.png')

    def draw(self):
        if self.game.is_floor(self.x, self.y):
            self.draw_character(self.hero_img)

    def move_down(self, event):
        self.hero_img = PhotoImage(file ='hero-down.png')
        if self.y < 9 and self.game.is_floor(self.x, self.y + 1):
            self.y += 1
        self.draw()

    def move_right(self, event):
        self.hero_img = PhotoImage(file ='hero-right.png')
        if self.x < 9 and self.game.is_floor(self.x + 1, self.y):
            self.x += 1
        self.draw()

    def move_up(self, event):
        self.hero_img = PhotoImage(file ='hero-up.png')
        if self.y > 0 and self.game.is_floor(self.x, self.y - 1):
            self.y -= 1
        self.draw()

    def move_left(self, event):
        self.hero_img = PhotoImage(file ='hero-left.png')
        if self.x > 0 and self.game.is_floor(self.x - 1, self.y):
            self.x -= 1
        self.draw()

class Boss(Character):
    def __init__(self, x, y, canvas, game):
        super().__init__(x, y, canvas, game)
        self.boss_img = PhotoImage(file ='boss.png')

    def draw(self):
        self.draw_character(self.boss_img)
