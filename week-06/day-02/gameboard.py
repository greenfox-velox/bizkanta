from tile import *

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
        for row in range(rows):
            for column in range(columns):
                if wholemap[column][row] == 0:
                    self.Map_list.append(Floor(row, column, canvas))
                else:
                    self.Map_list.append(Wall(row, column, canvas))
    def draw(self):
        for i in self.Map_list:
            i.draw()
