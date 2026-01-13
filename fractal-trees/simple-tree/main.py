import turtle

def draw_branch(branch_length, t):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_branch(branch_length - 15, t)  # Right branch
        t.left(40)
        draw_branch(branch_length - 15, t)  # Left branch
        t.right(20)
        t.backward(branch_length)  # Return to origin

#pen draws off top of screen here due to starting position at center (default 0, 0)
#t = turtle.Turtle()
#t.left(90)
#t.speed(0)
#draw_branch(100, t)
#turtle.done()

t = turtle.Turtle()
t.speed(0)
t.left(90)

# 1. Move turtle to the bottom center
t.penup()
t.goto(0, -250) # Moves 250 pixels down from center
t.pendown()

# 2. Draw with a slightly smaller starting branch to ensure it fits
draw_branch(80, t) 

turtle.done()
