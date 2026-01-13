import turtle
import time

def fractal_tree(t, branch_len, angle, level):
    """
    Draws a fractal tree using recursion.
    t: the turtle object
    branch_len: the current length of the branch
    angle: the angle for branching
    level: the current recursion depth
    """
    if level > 0:
        # Draw main branch
        t.forward(branch_len)
        
        # Right branch
        t.right(angle)
        fractal_tree(t, branch_len * 0.7, angle, level - 1) # Reduce length and level
        
        # Left branch (return to previous position first)
        t.left(2 * angle)
        fractal_tree(t, branch_len * 0.7, angle, level - 1) # Reduce length and level
        
        # Return to original direction and position
        t.right(angle)
        t.backward(branch_len)
    else:
        # Optional: draw leaves at the end of smallest branches
        t.dot(5, "green")
        
def main():
    # Setup the screen
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")

    # Create the turtle
    t = turtle.Turtle()
    t.speed(0) # Max speed
    t.pencolor("chocolate") # Branch color
    t.penup()
    t.goto(0, -200) # Start position at the bottom of the screen
    t.left(90) # Point up
    t.pendown()

    # Draw the tree
    fractal_tree(t, 100, 30, 7) # Initial length, angle, and recursion depth

    # Keep the window open until clicked
    screen.exitonclick()

if __name__ == "__main__":
    main()