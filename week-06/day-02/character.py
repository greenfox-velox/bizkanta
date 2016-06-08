from tkinter import *
# from gameboard import *
from random import randint

class Character(object):
    def __init__(self, x, y, canvas, game):
        self.x = x
        self.y = y
        self.offset = 72
        self.canvas = canvas
        self.game = game
        self.dice = self.dice()

    def draw_character(self, img):
        self.canvas.create_image(self.x * self.offset, self.y * self.offset, image = img, anchor = NW)

    def dice(self):
        dice_num = randint(1,6)
        return dice_num

class Hero(Character):
    def __init__(self, x, y, canvas, game):
        super().__init__(x, y, canvas, game)
        self.hero_img = PhotoImage(file ='hero-down.png')
        self.level = 1
        self.HP = 20 + self.dice + self.dice + self.dice
        self.DP = self.dice * self.dice
        self.SP = 5 + self.dice

    def draw(self):
        self.draw_character(self.hero_img)

    def move_down(self):
        self.hero_img = PhotoImage(file ='hero-down.png')
        if self.game.is_map_boundaries(self.x, self.y + 1) and self.game.is_stop_at_wall(self.x, self.y + 1):
            self.y += 1
        self.draw()

    def move_right(self):
        self.hero_img = PhotoImage(file ='hero-right.png')
        if self.game.is_map_boundaries(self.x + 1, self.y) and self.game.is_stop_at_wall(self.x + 1, self.y):
            self.x += 1
        self.draw()

    def move_up(self):
        self.hero_img = PhotoImage(file ='hero-up.png')
        if self.game.is_map_boundaries(self.x, self.y - 1) and self.game.is_stop_at_wall(self.x, self.y - 1):
            self.y -= 1
        self.draw()

    def move_left(self):
        self.hero_img = PhotoImage(file ='hero-left.png')
        if self.game.is_map_boundaries(self.x - 1, self.y) and self.game.is_stop_at_wall(self.x - 1, self.y):
            self.x -= 1
        self.draw()

    def hero_move(self, event):
        if event.keysym == 'Down':
            self.move_down()
        if event.keysym == 'Right':
            self.move_right()
        if event.keysym == 'Up':
            self.move_up()
        if event.keysym == 'Left':
            self.move_left()

class Boss(Character):
    def __init__(self, x, y, canvas, game):
        super().__init__(x, y, canvas, game)
        self.level = 1
        self.HP = 2 * self.level * self.dice + self.dice
        self.DP = self.level/2 * self.dice + self.dice/2
        self.SP = self.level * self.dice + self.level
        self.boss_img = PhotoImage(file ='boss.png')

    def draw(self):
        self.draw_character(self.boss_img)

class Skeleton(Character):
    def __init__(self, x, y, canvas, game):
        super().__init__(x, y, canvas, game)
        self.level = 1
        self.skeleton_img = PhotoImage(file ='skeleton.png')
        self.HP = 2 * self.level * self.dice
        self.DP = self.level/2 * self.dice
        self.SP = self.level * self.dice

    def draw(self):
        self.draw_character(self.skeleton_img)
