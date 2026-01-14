import turtle

def draw_fractal_star(t, size):
    if size <= 10:
        return
    for _ in range(5):
        t.forward(size)
        draw_fractal_star(t, size / 3)
        t.left(216) 

# 1. Setup screen size explicitly
screen = turtle.Screen()
screen.setup(width=1000, height=1000) # Large enough to contain the fractal
screen.bgcolor("black")
screen.tracer(0) # Disable animation for instant drawing

star_turtle = turtle.Turtle()
star_turtle.color("cyan")
star_turtle.hideturtle()

# 2. Position for centering
# For a size 360 star, shifting roughly half its width left 
# and moving up prevents it from hitting the right/bottom edges.
star_turtle.penup()
star_turtle.goto(-180, 100) 
star_turtle.pendown()

# 3. Draw and update
draw_fractal_star(star_turtle, 360)
screen.update() # Required because tracer is 0

turtle.done()
