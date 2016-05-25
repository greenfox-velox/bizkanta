# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

width = 300
height = 300
offset = 20

def draw_line(x, y):
    line = canvas.create_line(x, y, width/2, height/2)

for n in range(0, width + offset, offset):
    draw_line(n, 0)
    draw_line(n, height)
    draw_line(0, n)
    draw_line(width, n)

root.mainloop()
