from tkinter import *
from gameboard import *
from tile import *
from character import *

root = Tk()

canvas = Canvas(root, width='720', height='720')
canvas.pack()

game = GameBoard(canvas)
game.draw()

hero = Hero(0, 0, canvas, game)
hero.draw()
root.bind('<Down>', hero.move_down)
root.bind('<Right>', hero.move_right)
root.bind('<Up>', hero.move_up)
root.bind('<Left>', hero.move_left)

boss = Boss(4, 5, canvas, game)
boss.draw()

root.mainloop()
