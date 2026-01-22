import turtle

# Recursive functions to handle the "left" and "right" folds
def left_dragon(level, length):
    if level > 0:
        left_dragon(level - 1, length)
        t.left(90)
        right_dragon(level - 1, length)
    else:
        t.forward(length)

def right_dragon(level, length):
    if level > 0:
        left_dragon(level - 1, length)
        t.right(90)
        right_dragon(level - 1, length)
    else:
        t.forward(length)

# --- Configuration ---
LEVEL = 12         # Level of detail (8-13 is best for screen)
LINE_LENGTH = 6    # Individual segment size

# --- Setup ---
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pencolor("#00FFCC")

# --- Centering Logic ---
# Shifting the start point helps keep the growth on screen
t.penup()
t.goto(150, -50)  # Move slightly left and down from center (0,0)
t.pendown()

# Disable animation for instant drawing of complex fractals
turtle.tracer(0, 0)

# --- Draw ---
left_dragon(LEVEL, LINE_LENGTH)

# Refresh screen to show the result
turtle.update()
turtle.done()
