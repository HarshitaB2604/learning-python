from tkinter import *

root = Tk()

# ----------------------------------CONSTANTS-----------------------
canvas_width = 300
canvas_height = 400
light_radius = 35
stoplight_width = 120
stoplight_height = 350
dist_between_lights = 50

# ---------------------------------CANVAS--------------------------------
screen = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
screen.pack()


def draw_circle(radius, center_x, center_y, color):
    screen.create_oval(center_x - radius, center_y - radius,
                       center_x + radius, center_y + radius, fill=color, outline="")


# ----------------------------------MAIN----------------------------
# base
screen.create_rectangle(canvas_width/2 - stoplight_width/2, canvas_height/2 - stoplight_height/2,
                        canvas_width/2 + stoplight_width/2, canvas_height/2 + stoplight_height/2, fill="grey", outline="")
# light
light_y = canvas_height/2 - (light_radius*2 + dist_between_lights)
colors = ["red", "yellow", "green"]
for i in range(3):
    draw_circle(light_radius, canvas_width/2, light_y, colors[i])

    light_y += light_radius*2 + dist_between_lights

mainloop()
