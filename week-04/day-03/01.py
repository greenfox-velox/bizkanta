# create a 300x300 black canvas.
# draw a red horizontal line to its middle.
# draw a green vertical line to its middle.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg='black')
canvas.pack()

width = 300
height = 300

red_line = canvas.create_line(0, height/2, width, height/2, fill='red')
green_line = canvas.create_line(width/2, 0, width/2, height, fill='green')


root.mainloop()
