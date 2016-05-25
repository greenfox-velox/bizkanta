# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

red_line = canvas.create_line(20, 20, 100, 20, fill='red')
green_line = canvas.create_line(100, 20, 100, 50, fill='green')
blue_line = canvas.create_line(100, 50, 20, 50, fill='blue')
purple_line = canvas.create_line(20, 50, 20, 20, fill='purple')


root.mainloop()
