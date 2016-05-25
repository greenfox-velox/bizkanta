# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

width = 300
height = 300

def draw_lines(x, y):
    canvas.create_line(x, y, width/2, height/2, fill='red')
    return x, y

print(draw_lines(20, 20))
print(draw_lines(60, 120))
print(draw_lines(150, 80))

root.mainloop()
