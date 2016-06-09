from tkinter import *
# from character import *
class Stat(object):
    def __init__(self, canvas, hero):
        self.canvas = canvas
        self.hero = hero
        self.x = 850
        self.y = 100

    def draw_text(self):
        self.canvas.create_text(self.x, self.y, text = 'Hero + (Level ' + str(self.hero.level) + ') HP: ' + str(self.hero.hp) + '/' + str(self.hero.max_hp) + ' | DP: ' + str(self.hero.dp) + ' | SP: ' + str(self.hero.sp))
