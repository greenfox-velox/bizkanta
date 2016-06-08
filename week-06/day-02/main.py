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
# root.bind('<Down>', hero.move_down)
# root.bind('<Right>', hero.move_right)
# root.bind('<Up>', hero.move_up)
# root.bind('<Left>', hero.move_left)
# hero_move = Move(0,0,canvas,game)
root.bind('<KeyPress>', hero.hero_move)

boss = Boss(4, 5, canvas, game)
boss.draw()

skeleton1 = Skeleton(9, 7, canvas, game)
skeleton2 = Skeleton(5, 1, canvas, game)
skeleton3 = Skeleton(2, 9, canvas, game)
skeleton1.draw()
skeleton2.draw()
skeleton3.draw()

root.mainloop()
