from tkinter import *

canvas_size = 600

root = Tk()
canvas = Canvas(root, width=canvas_size, height=canvas_size)
canvas.pack()

def fractal(x, y, size):
    canvas.create_rectangle(x, y, x + size, y + size, fill="yellow")
    if size < 5:
        pass
    else:
        fractal(x + size/3, y, size/3)
        fractal(x, y + size/3, size/3)
        fractal(x + 2*size/3, y + size/3, size/3)
        fractal(x + size/3, y + 2*size/3, size/3)

fractal(5, 5, 590)

root.mainloop()
