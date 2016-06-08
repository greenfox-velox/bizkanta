from tkinter import *


def move(event=None):
    global x1, x2, y1, y2, oval
    if event.char == 'w':
        y1 -= 10
        y2 -= 10
        oval = (x1, y1, x2, y2)
        canvas.coords(oval_id, oval)

m = Tk()

canvas = Canvas(m)
canvas.pack(expand=1, fill='both')
x1, x2 = 50, 100
y1, y2 = 50, 100
oval = (x1, y1, x2, y2)
oval_id = canvas.create_oval(oval)
canvas.bind_all('<w>', move)

m.mainloop()
