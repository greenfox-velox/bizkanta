from tkinter import *
from map import *
from game import *
from stat import *
from tile import *
from character import *

root = Tk()

canvas = Canvas(root, width='1000', height='720')
canvas.pack()

game = Game(canvas)
game.draw_all()

root.bind('<KeyPress>', game.hero_move)

root.mainloop()
