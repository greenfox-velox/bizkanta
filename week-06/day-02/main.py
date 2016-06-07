from tkinter import *
from gameboard import *
from tile import *
from character import *

root = Tk()

canvas = Canvas(root, width='720', height='720')
canvas.pack()

game = GameBoard(canvas)
game.draw()

hero = Hero(0,1,canvas)
hero.draw()

root.mainloop()
