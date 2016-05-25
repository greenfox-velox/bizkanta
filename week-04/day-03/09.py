# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

width = 300
height = 300

def draw_square(size):
    return canvas.create_rectangle(width/2 - size/2, height/2 - size/2, width/2 + size/2, height/2 + size/2)

print(draw_square(150))
print(draw_square(120))
print(draw_square(50))

root.mainloop()
