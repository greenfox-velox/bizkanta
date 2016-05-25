from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

offset = 10

def draw_square(x):
    square = canvas.create_rectangle(x, x, x + offset, x + offset, fill='purple')

for x in range(10, 200, offset):
    draw_square(x)

root.mainloop()
