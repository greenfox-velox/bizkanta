# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

width = 300
height = 300

# def random_color():
#     r = lambda: random.randint(0,255)
#     print('#%02X%02X%02X' % (r(),r(),r()))
#
# print(random_color())

def draw_square(size):
    square = canvas.create_rectangle(width/2 - size/2, height/2 - size/2, width/2 + size/2, height/2 + size/2, fill="#%06x" % random.randint(0, 0xFFFFFF))

for size in range(210, 10, -10):
    draw_square(size)

root.mainloop()
