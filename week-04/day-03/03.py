# create a 300x300 canvas.
# draw its diagonals in green.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

width = 300
height = 300

diagonal1 = canvas.create_line(0, 0, width, height, fill='green')
diagonal2 = canvas.create_line(0, height, width, 0, fill='green')


root.mainloop()
