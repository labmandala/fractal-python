import turtle
import math

def tree(branch_len, t):
    """
    Draws a fractal tree using recursion.
    t: the turtle object
    branch_len: the current length of the branch
    """
    if branch_len > 5: # Base case: stop when branch is too short
        t.forward(branch_len)
        t.right(20) # Branch right
        tree(branch_len - 15, t) # Recursive call for right branch

        t.left(40) # Branch left (20 right + 40 left = 20 left from original path)
        tree(branch_len - 15, t) # Recursive call for left branch

        t.right(20) # Return to original heading
        t.backward(branch_len) # Return to the starting point of the branch

def main():
    window = turtle.Screen()
    window.bgcolor("white")
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0) # Fastest drawing speed
    t.left(90) # Start facing up
    t.penup()
    t.backward(100) # Move to the bottom of the screen
    t.pendown()
    t.pencolor("green")
    
    tree(75, t)
    turtle.exitonclick() # Keep window open until clicked

if __name__ == "__main__":
    main()
