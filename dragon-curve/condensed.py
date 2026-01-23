import turtle

def draw_dragon(level, length, sign=1):
    if level == 0:
        t.forward(length)
    else:
        draw_dragon(level - 1, length, 1)
        t.left(90 * sign)
        draw_dragon(level - 1, length, -1)

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.hideturtle()
t.pencolor("cyan")
turtle.tracer(0, 0)

# --- POSITIONING: ---
t.penup()
t.goto(-100, 50)  
t.setheading(180)  # Face West so it grows into the screen
t.pendown()

# Draw
draw_dragon(level=12, length=4)

turtle.update()
turtle.done()
