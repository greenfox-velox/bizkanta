# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# create a loop that draws 20 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

width = 300
height = 300

def draw_square(size):
    square = canvas.create_rectangle(width/2 - size/2, height/2 - size/2, width/2 + size/2, height/2 + size/2)

for size in range(10, 210, 10):
    draw_square(size)

root.mainloop()
