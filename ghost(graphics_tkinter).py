from tkinter import *

root = Tk()

# ------------------------CONSTANTS---------------------------------
canvas_width = 400
canvas_height = 400

head_radius = canvas_width/4
body_width = head_radius * 2
body_height = canvas_height/3
num_feet = 3
foot_radius = body_width / (num_feet * 2)
body_color = "red"

eye_radius = head_radius * (4/9)
eye_offset = eye_radius * 1.5
eye_color = "white"
pupil_radius = eye_radius/2.5
pupil_left_offset = head_radius/4
pupil_right_offset = pupil_radius * 5
pupil_color = "blue"

# ----------------------------CANVAS--------------------
screen = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
screen.pack()

# ----------------------------GHOST---------------------
# body
bodytx = canvas_width/2 - body_width/2
bodyty = canvas_height/2 - body_height/2
bodybx = canvas_width/2 + body_width/2
bodyby = canvas_height/2 + body_height/2
screen.create_rectangle(bodytx, bodyty, bodybx, bodyby,
                        fill=body_color, outline=body_color)

# head
screen.create_oval(bodytx, bodyty - head_radius, bodybx,
                   bodyty + head_radius, fill=body_color, outline=body_color)

# feet
foot_ty = bodyby - foot_radius
foot_by = foot_ty + foot_radius*2
foot_tx = bodytx
foot_bx = foot_tx + foot_radius*2
for feet in range(num_feet):
    screen.create_oval(foot_tx, foot_ty, foot_bx, foot_by,
                       fill=body_color, outline=body_color)

    foot_tx += foot_radius*2
    foot_bx += foot_radius*2

# eyes
eye_tx = canvas_width/2 - eye_offset
eye_ty = bodyty - 20
eye_bx = eye_tx + eye_radius
eye_by = eye_ty + eye_radius

lpupil_tx = eye_tx + pupil_left_offset
for i in range(2):
    # outer eye
    screen.create_oval(eye_tx, eye_ty, eye_bx,
                       eye_by, fill=eye_color, outline=body_color)

    eye_tx += eye_offset
    eye_bx += eye_offset

# left pupil
pupil_ty = eye_ty + pupil_left_offset/2 + 5
screen.create_oval(lpupil_tx, pupil_ty, lpupil_tx + pupil_radius,
                   pupil_ty + pupil_radius, fill=pupil_color, outline=eye_color)

# right pupil
rpupil_tx = eye_bx - pupil_right_offset
screen.create_oval(rpupil_tx, pupil_ty, rpupil_tx + pupil_radius,
                   pupil_ty + pupil_radius, fill=pupil_color, outline=eye_color)


mainloop()
