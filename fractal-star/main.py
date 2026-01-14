import turtle

def draw_fractal_star(t, size):
    # Base case: stop when the star is too small to see
    if size <= 10:
        return
    else:
        # Draw a 5-pointed star
        for _ in range(5):
            t.forward(size)
            # Recursive call: draw a smaller star at the current point
            draw_fractal_star(t, size / 3)
            # 144 degrees is the standard turn for a 5-pointed star
            t.left(216) 

# Setup the screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")

star_turtle = turtle.Turtle()
star_turtle.color("cyan")
star_turtle.speed(0)  # Maximum speed for complex fractals

# Move to a starting position to avoid the edges
star_turtle.penup()
star_turtle.goto(-150, 50)
star_turtle.pendown()

# Initial call with a starting size
draw_fractal_star(star_turtle, 360)

turtle.done()
import turtle

def draw_fractal_star(t, size):
    # Base case: stop when the star is too small to see
    if size <= 10:
        return
    else:
        # Draw a 5-pointed star
        for _ in range(5):
            t.forward(size)
            # Recursive call: draw a smaller star at the current point
            draw_fractal_star(t, size / 3)
            # 144 degrees is the standard turn for a 5-pointed star
            t.left(216) 

# Setup the screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")

star_turtle = turtle.Turtle()
star_turtle.color("cyan")
star_turtle.speed(0)  # Maximum speed for complex fractals

# Move to a starting position to avoid the edges
star_turtle.penup()
star_turtle.goto(-150, 50)
star_turtle.pendown()

# Initial call with a starting size
draw_fractal_star(star_turtle, 360)

turtle.done()
