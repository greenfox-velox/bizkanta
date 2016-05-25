from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()


offset = 10
x = 0

# canvas.create_rectangle(10,10,20,20)
# canvas.create_rectangle(20,20,40,40)
# canvas.create_rectangle(40,40,70,70)

def draw_square(x, offset):
    square = canvas.create_rectangle(x, x, x + offset, x + offset, fill='purple')

for n in range(0, 50, offset):
    x += offset
    offset += 10
    draw_square(x, offset)

root.mainloop()
