from tkinter import *

root = Tk()

# -------------------CANVAS-----------------------------
screen = Canvas(root, width=400, height=300, bg="white")
screen.pack()

# -------------------FLAG-----------------------
screen.create_rectangle(0, 150, 400, 300, fill="red", outline="white")

mainloop()
