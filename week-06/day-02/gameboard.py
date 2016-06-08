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
        self.wholemap = wholemap
        for row in range(rows):
            for column in range(columns):
                if wholemap[column][row] == 0:
                    self.Map_list.append(Floor(row, column, canvas))
                else:
                    self.Map_list.append(Wall(row, column, canvas))
    def draw(self):
        for i in self.Map_list:
            i.draw()

    def is_map_boundaries(self, x, y):
        return x >= 0 and x <= 9 and y >= 0 and y <= 9

    def is_stop_at_wall(self, x, y):
        return self.wholemap[y][x] == 0
