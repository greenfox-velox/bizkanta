from tkinter import *
from math import *
import random

canvas_size = 600

root = Tk()
canvas = Canvas(root, width=canvas_size, height=canvas_size)
canvas.pack()




def fractal(x, y, size):
    height = size * sqrt(3/4)
    third = size / 3
    canvas.create_polygon(
        x + size / 4, y,
        x + 3 * size / 4, y,
        x + size, y + height / 2,
        x + 3 * size / 4, y + height,
        x + size / 4, y + height,
        x, y + height / 2,
        fill='#%06x' % random.randint(0, 0xFFFFFF), outline='black')
    if size < 8:
        pass
    else:
        fractal(x + size / 6, y, third)
        fractal(x + 3 * size / 6, y, third)
        fractal(x, y + height / 3, third)
        fractal(x + 2 * size / 3, y + height / 3, third)
        fractal(x + size / 6, y + 2 * height / 3, third)
        fractal(x + 3* size / 6, y + 2 * height / 3, third)

fractal(5,5,595)

root.mainloop()
