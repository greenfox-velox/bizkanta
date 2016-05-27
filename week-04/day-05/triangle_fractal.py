from tkinter import *
from math import *

canvas_size = 600

root = Tk()
canvas = Canvas(root, width=canvas_size, height=canvas_size)
canvas.pack()

def fractal(x, y, size):
    canvas.create_polygon([x, y, x + size, y, x + size/2, y + size*sqrt(3/4)], fill="white", outline='black')
    if size < 5:
        pass
    else:
        fractal(x, y, size/2)
        fractal(x + size/2, y, size/2)
        fractal(x + size/4, y + size*sqrt(3/4)/2, size/2)


fractal(5, 5, 595)

root.mainloop()
