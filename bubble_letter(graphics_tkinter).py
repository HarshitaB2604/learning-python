from tkinter import *

root = Tk()

# -------------------CANVAS-----------------------------
screen = Canvas(root, width=400, height=500, bg="#1bbade")
screen.pack()

# ------------------LETTER(L)-----------------------
screen.create_line(75, 50, 150, 50, 150, 350, 275,
                   350, 275, 420, 75, 420, 75, 50)


mainloop()
