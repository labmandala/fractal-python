import turtle

def fractal_tree(branch_length, t):
    """
    Draws a fractal tree using recursion.
    branch_length: The current length of the branch.
    t: The turtle object.
    """
    if branch_length > 5: # Base case: stop drawing when the branch is too short
        # Draw the main branch
        t.forward(branch_length)
        t.right(20) # Turn right for the first sub-branch

        # Recursive call for the first sub-branch
        fractal_tree(branch_length - 15, t)

        t.left(40) # Turn left for the second sub-branch

        # Recursive call for the second sub-branch
        fractal_tree(branch_length - 15, t)

        t.right(20) # Restore original heading
        t.backward(branch_length) # Move back to the starting point

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0) # Set speed to fastest
    t.left(90) # Start facing upwards (north)
    t.penup()
    t.goto(0, -200) # Start near the bottom of the screen
    t.pendown()
    t.color("green")
    
    fractal_tree(100, t)
    
    screen.exitonclick() # Keep the window open until clicked

if __name__ == "__main__":
    main()
