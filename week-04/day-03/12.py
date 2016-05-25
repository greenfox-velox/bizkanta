# create a 300x300 canvas.
# fill it with a checkerboard pattern.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='320', height='320')
canvas.pack()

width = 320
height = 320
offset = 40
x = 0
y = 0

# canvas.create_rectangle(0,0,40,40)
# canvas.create_rectangle(40,0,80,40)
# canvas.create_rectangle(80,0,120,40)

def draw_square(x, y, color):
    square = canvas.create_rectangle(x, y, x + offset, y + offset, fill=color)

for x in range(0, width, offset):
    for y in range(0, height, offset):
        color = 'white'
        if (x % 80 == 0 and y % 80 == 0) or (not x % 80 == 0 and not y % 80 == 0):
            color = 'black'
        draw_square(x, y, color)

root.mainloop()
