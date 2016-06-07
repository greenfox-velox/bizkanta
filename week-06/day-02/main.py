from tkinter import *
from gameboard import *
from tile import *

root = Tk()

canvas = Canvas(root, width='720', height='720')
canvas.pack()

game = GameBoard(canvas)
game.draw()

root.mainloop()
