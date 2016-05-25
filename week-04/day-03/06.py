# create a 300x300 canvas.
# draw a green 10x10 square to its center.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

width = 300
height = 300

square = canvas.create_rectangle(width/2 - 5, height/2 - 5, width/2 + 5, height/2 + 5, fill='green')

root.mainloop()
