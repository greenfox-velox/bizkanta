# create a 300x300 canvas.
# fill it with four different size and color rectangles.

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

width = 300
height = 300

square_green = canvas.create_rectangle(0, 0, 100, 120, fill='green')
square_red = canvas.create_rectangle(100, 120, width, 0, fill='red')
square_blue = canvas.create_rectangle(0, 120, 200, height, fill='blue')
square_purple = canvas.create_rectangle(200, height, width, 120, fill='purple')

root.mainloop()
