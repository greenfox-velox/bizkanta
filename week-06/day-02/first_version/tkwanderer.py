from tkinter import *

root = Tk()

canvas = Canvas(root, width='720', height='720')
canvas.pack()

rows = 10
columns = 10
offset = 72

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

def draw_floor(x, y):
    canvas.create_image(x * offset, y * offset, image = floor_img, anchor = NW)

def draw_wall(x, y):
    canvas.create_image(x * offset, y * offset, image = wall_img, anchor = NW)

def draw_hero(x, y):
    canvas.create_image(x * offset, y * offset, image = hero_img, anchor = NW)

def draw_map():
    for row in range(rows):
        for column in range(columns):
            if wholemap[column][row] == 0:
                draw_floor(row, column)
            else:
                draw_wall(row, column)

draw_map()
draw_hero(0,0)

root.mainloop()
