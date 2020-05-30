from tkinter import *

root = Tk()

# -----------------CANVAS--------------
screen = Canvas(root, width=200, height=200, bg="red")
screen.pack()

# ----------------BOARD-----------------
# vertical lines
# right
screen.create_line(125, 25, 125, 175)
# left
screen.create_line(75, 25, 75, 175)

# horizontal lines
# top
screen.create_line(25, 75, 175, 75)
# bottom
screen.create_line(25, 125, 175, 125)

mainloop()
