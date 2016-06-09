from tile import *
from character import *

wholemap = [
[0,1,1,0,1,0,0,0,0,0],
[0,0,0,0,1,0,0,1,1,0],
[0,0,0,0,0,1,0,1,0,0],
[0,0,1,0,0,1,0,1,0,0],
[0,0,1,1,0,0,0,1,0,0],
[0,0,0,1,0,0,0,0,0,0],
[0,0,0,1,1,1,1,0,1,1],
[1,0,0,1,0,0,0,0,1,0],
[1,1,1,1,0,0,0,1,1,0],
[0,0,0,0,0,1,0,0,0,0]
]

rows = 10
columns = 10

class GameBoard(object):
    def __init__(self, canvas):
        self.Map_list = []
        self.canvas = canvas
        self.wholemap = wholemap
        for row in range(rows):
            for column in range(columns):
                if wholemap[column][row] == 0:
                    self.Map_list.append(Floor(row, column, canvas))
                else:
                    self.Map_list.append(Wall(row, column, canvas))
    def draw(self):
        for tile in self.Map_list:
            tile.draw()

    def is_map_boundaries(self, x, y):
        return x >= 0 and x <= 9 and y >= 0 and y <= 9

    def is_stop_at_wall(self, x, y):
        return self.wholemap[y][x] == 0

class Statistics():
    def __init__(self, canvas, hero):
        self.canvas = canvas
        self.hero = hero
        self.x = 850
        self.y = 100

    def draw_text(self):
        self.canvas.create_text(self.x, self.y, text = 'Hero + (Level ' + str(self.hero.level) + ') HP: ' + str(self.hero.hp) + '/' + str(self.hero.max_hp) + ' | DP: ' + str(self.hero.dp) + ' | SP: ' + str(self.hero.sp))
