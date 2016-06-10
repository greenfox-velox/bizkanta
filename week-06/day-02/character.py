from tkinter import *
from random import randint

class Character(object):
    def __init__(self, x, y, canvas):
        self.x = x
        self.y = y
        self.offset = 72
        self.canvas = canvas
        self.dice_num = self.dice()

    def draw_character(self, img):
        self.canvas.create_image(self.x * self.offset, self.y * self.offset, image = img, anchor = NW)

    def dice(self):
        dice_num = randint(1,6)
        return dice_num

class Hero(Character):
    def __init__(self, x, y, canvas):
        super().__init__(x, y, canvas)
        self.hero_img = PhotoImage(file ='hero-down.png')
        self.level = 1
        self.max_hp = 100
        self.current_hp = 100
        self.hp = 20 + self.dice_num + self.dice_num + self.dice_num
        self.dp = self.dice_num * self.dice_num
        self.sp = 5 + self.dice_num

    def draw(self):
        self.draw_character(self.hero_img)

    def move_down(self):
        self.hero_img = PhotoImage(file ='hero-down.png')
        self.y += 1

    def move_right(self):
        self.hero_img = PhotoImage(file ='hero-right.png')
        self.x += 1

    def move_up(self):
        self.hero_img = PhotoImage(file ='hero-up.png')
        self.y -= 1

    def move_left(self):
        self.hero_img = PhotoImage(file ='hero-left.png')
        self.x -= 1

    def current_pos(self, x, y):
        self.draw(x, y)

class Boss(Character):
    def __init__(self, x, y, canvas):
        super().__init__(x, y, canvas)
        self.level = 1
        self.boss_img = PhotoImage(file ='boss.png')
        # self.HP = 2 * self.level * self.dice + self.dice
        # self.DP = self.level/2 * self.dice + self.dice/2
        # self.SP = self.level * self.dice + self.level

    def draw(self):
        self.draw_character(self.boss_img)

class Skeleton(Character):
    def __init__(self, x, y, canvas):
        super().__init__(x, y, canvas)
        self.level = 1
        self.skeleton_img = PhotoImage(file ='skeleton.png')
        # self.HP = 2 * self.level * self.dice
        # self.DP = self.level/2 * self.dice
        # self.SP = self.level * self.dice

    def draw(self):
        self.draw_character(self.skeleton_img)

class Bomb(Character):
    def __init__(self, x, y, canvas):
        super().__init__(x, y, canvas)
        self.bomb_img = PhotoImage(file ='bomb.png')
        self.explode_img = PhotoImage(file ='expl.png')

    def draw(self, x, y):
        self.x = x
        self.y = y
        self.draw_character(self.bomb_img)

    def explode(self, x, y):
        self.draw_character(self.explode_img)
