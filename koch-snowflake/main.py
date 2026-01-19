import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

# Setup
scr = turtle.Screen()
t = turtle.Turtle()
t.speed(0)  # Fastest drawing
t.penup()
t.goto(-150, 90)
t.pendown()

draw_snowflake(t, 4, 300) # Higher order = more detail
scr.exitonclick()
