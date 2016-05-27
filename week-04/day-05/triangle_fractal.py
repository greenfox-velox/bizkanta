from tkinter import *
from math import *
import random

canvas_size = 600

root = Tk()
canvas = Canvas(root, width=canvas_size, height=canvas_size)
canvas.pack()

def fractal(x, y, size):
    height = size * sqrt(3/4)
    canvas.create_polygon([x, y, x + size, y, x + size/2, y + height], fill='#%06x' % random.randint(0, 0xFFFFFF), outline='black')
    if size < 5:
        pass
    else:
        fractal(x, y, size/2)
        fractal(x + size/2, y, size/2)
        fractal(x + size/4, y + height/2, size/2)

fractal(5, 5, 595)

root.mainloop()
