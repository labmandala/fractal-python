import turtle

# Recursive functions to handle the "left" and "right" folds
def left_dragon(level, length):
    if level > 0:
        # A left dragon is a left followed by a right
        left_dragon(level - 1, length)
        t.left(90)
        right_dragon(level - 1, length)
    else:
        t.forward(length)

def right_dragon(level, length):
    if level > 0:
        # A right dragon is a right followed by a left
        left_dragon(level - 1, length)
        t.right(90)
        right_dragon(level - 1, length)
    else:
        t.forward(length)

# Screen setup
screen = turtle.Screen()
screen.title("Dragon Curve")
screen.bgcolor("black")

# Turtle setup
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pencolor("cyan")

# Start position
t.penup()
t.goto(-100, -120)
t.pendown()

# Disable animation for instant drawing of complex fractals
turtle.tracer(0, 0)

# Draw the Dragon Curve (increase level for more detail)
left_dragon(level=10, length=10)

turtle.done()
