from tkinter import *
from math import *
import random

canvas_size = 700

root = Tk()
canvas = Canvas(root, width=canvas_size, height=canvas_size)
canvas.pack()

def fractal(x, y, size):
    height = size * sqrt(3/4)
    third = size/3
    canvas.create_polygon(
        x + size/4, y,
        x + size*3/4, y,
        x + size, y + height/2,
        x + size*3/4, y + height,
        x + size/4, y + height,
        x, y + height/2,
        fill='lemonchiffon', outline='black')
    if size < 8:
        pass
    else:
        fractal(x + third/2, y, third)
        fractal(x + 3*third/2, y, third)
        fractal(x, y + height/3, third)
        fractal(x + 2*third, y + height/3, third)
        fractal(x + third/2, y + height*2/3, third)
        fractal(x + third*3/2, y + height*2/3, third)

fractal(20,20,595)

root.mainloop()
