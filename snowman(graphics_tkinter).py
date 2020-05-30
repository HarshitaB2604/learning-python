"""
This program will draw a snowman on the screen.
"""

from tkinter import *

root = Tk()

# ------------------------CONSTANTS---------------------------------
canvas_width = 300
canvas_height = 400
bottom_diameter = canvas_height/3
middle_diameter = bottom_diameter*(2/3)
top_diameter = middle_diameter*(2/3)
snowmancolor = "#c1c6c7"

# ----------------------------CANVAS--------------------
screen = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
screen.pack()


# ---------------------------SNOWMAN---------------------------
# bottom
btcornerx = canvas_width/2 - bottom_diameter/2
btcornery = canvas_height - bottom_diameter
bbcornerx = canvas_width/2 + bottom_diameter/2
bbcornery = canvas_height
screen.create_oval(btcornerx, btcornery, bbcornerx,
                   bbcornery, fill=snowmancolor, outline="white")
# middle
mtcornerx = canvas_width/2 - middle_diameter/2
mtcornery = btcornery - middle_diameter
mbcornerx = canvas_width/2 + middle_diameter/2
mbcornery = btcornery
screen.create_oval(mtcornerx, mtcornery, mbcornerx,
                   mbcornery, fill=snowmancolor, outline="white")
# top
ttcornerx = canvas_width/2 - top_diameter/2
ttcornery = mtcornery - top_diameter
tbcornerx = canvas_width/2 + top_diameter/2
tbcornery = mtcornery
screen.create_oval(ttcornerx, ttcornery, tbcornerx,
                   tbcornery, fill=snowmancolor, outline="white")
# hat
striptleftc_y = ttcornery-15
stripbrightc_y = ttcornery
striptleftc_x = ttcornerx
stripbrightc_x = tbcornerx
screen.create_rectangle(striptleftc_x, striptleftc_y,
                        stripbrightc_x, stripbrightc_y, fill="black")
screen.create_rectangle(striptleftc_x + 10, striptleftc_y - 50,
                        stripbrightc_x - 10, striptleftc_y, fill="black")


# Add shapes to canvas
mainloop()
