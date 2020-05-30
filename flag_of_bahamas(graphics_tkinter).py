from tkinter import *

root = Tk()

# -------------------CANVAS-----------------------------
screen = Canvas(root, width=400, height=300, bg="#078578")
screen.pack()

# -------------------FLAG--------------------------
# golden stripe
screen.create_rectangle(0, 100, 400, 200, fill="#ccaa00", outline="#078578")
# black triangle
screen.create_polygon(0, 0, 133, 150, 0, 300)

mainloop()
