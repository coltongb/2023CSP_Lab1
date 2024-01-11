# Import Turtle
import turtle as trtl

# Declare Turtles.
# ONLY USE THE lines TURTLE!!!!
box = trtl.Turtle()
lines = trtl.Turtle()
wn = trtl.Screen()

# Setup Screen
def setupScreen():
    global wn
    wn.setup(1000, 700)

# Create the box on the screen
def setupBox():
    box.speed(0)
    box.penup()
    box.goto(-490, -300)
    box.pendown()
    box.forward(980)
    box.left(90)
    box.forward(630)
    box.left(90)
    box.forward(980)
    box.left(90)
    box.forward(630)
    box.hideturtle()

srtx = -490
srty = -300
endy = -300
endx = 490
lines.speed(0)
# Code for 80 point version goes here
def v80():
    global srtx, srty, endx,endy
    lines.penup()
    lines.goto(srtx, srty)
    lines.pendown()
    for shape in range(50):
        lines.penup()
        lines.goto(srtx, srty)
        lines.pendown()
        lines.goto(endx, endy)
        srtx += 20
        endy += 13



# Code for the 90 point version goes here
def v90():
    # Calling the 80 point function - don't copy-paste from earlier method!!
    global srtx
    global srty
    global endx
    global endy
    v80()
    lines.penup()
    lines.goto(-srtx, srty)
    lines.pendown()
    endy -= 630
    for shape in range(50):
        lines.penup()
        lines.goto(srtx, srty)
        lines.pendown()
        lines.goto(-endx, endy)
        srtx -= 20
        endy += 13

v90()

# Code for the 100 point version here
def v100():
    # Calling the 90 point function - don't copy-paste from earlier method!!
    v90()




# Code for the 110 point version here
def v110():
    # Calling the 100 point function - don't copy-paste from earlier method!!
    v100()


setupScreen()
setupBox()






wn.mainloop()