from tkinter import *
from map import *
from character import *
from statistic import *

class Game(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.map = Map(canvas)
        self.hero = Hero(0,0, canvas)
        self.boss = Boss(4,5, canvas)
        self.skeleton1 = Skeleton(9,7, canvas)
        self.skeleton2 = Skeleton(5,1, canvas)
        self.skeleton3 = Skeleton(2,9, canvas)
        self.hero_stat = Stat(canvas, self.hero)

    def draw_all(self):
        self.map.draw()
        self.hero.draw()
        self.boss.draw()
        self.skeleton1.draw()
        self.skeleton2.draw()
        self.skeleton3.draw()
        self.hero_stat.draw_text()

    def hero_move(self, event):
        if event.keysym == 'Down':
            if self.map.is_map_boundaries(self.hero.x, self.hero.y + 1) and self.map.is_stop_at_wall(self.hero.x, self.hero.y + 1):
                self.hero.move_down()
                self.hero.draw()
        if event.keysym == 'Right':
            if self.map.is_map_boundaries(self.hero.x + 1, self.hero.y) and self.map.is_stop_at_wall(self.hero.x + 1, self.hero.y):
                self.hero.move_right()
                self.hero.draw()
        if event.keysym == 'Up':
            if self.map.is_map_boundaries(self.hero.x, self.hero.y - 1) and self.map.is_stop_at_wall(self.hero.x, self.hero.y - 1):
                self.hero.move_up()
                self.hero.draw()
        if event.keysym == 'Left':
            if self.map.is_map_boundaries(self.hero.x - 1, self.hero.y) and self.map.is_stop_at_wall(self.hero.x - 1, self.hero.y):
                self.hero.move_left()
                self.hero.draw()
