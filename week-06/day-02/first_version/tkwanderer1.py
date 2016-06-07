from tkinter import *

root = Tk()

canvas = Canvas(root, width='720', height='720')
canvas.pack()

rows = 10
columns = 10
offset = 72
x = 0
y = 0

wholemap = (
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
)


wall_img = PhotoImage(file = 'wall.png')
floor_img = PhotoImage(file = 'floor.png')
hero_img = PhotoImage(file = 'hero-down.png')

class Draw_tile():
    def __init__(self, x, y,):
        self.x = x
        self.y = y
        self.column = column
        self.row = row

    def draw_floor(self):
        canvas.create_image(self.x + self.row * offset, self.y + self.column * offset, image = floor_img, anchor = NW)

    def draw_wall(self):
        canvas.create_image(self.x + self.row * offset, self.y + self.column * offset, image = wall_img, anchor = NW)

    def draw_hero(self):
        canvas.create_image(self.x + offset, self.y + offset, image = hero_img, anchor = NW)

def draw_map(x, y):
    for row in range(rows):
        for column in range(columns):
            if wholemap[column][row] == 0:
                draw_floor()
            else:
                draw_wall()

tile = Draw_tile(0,0)
tile()

root.mainloop()
