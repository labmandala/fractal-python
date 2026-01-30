import turtle
import colorsys
import math

# ---------- Color by depth + rotation ----------
def set_depth_color(depth, max_level, rotation_index, symmetry):
    # Depth-based gradient
    t_norm = depth / max_level

    # Hue sweeps + rotation offset
    base_hue = 0.65 - 0.65 * t_norm
    hue_offset = rotation_index / symmetry * 0.25
    hue = (base_hue + hue_offset) % 1.0

    r, g, b = colorsys.hsv_to_rgb(hue, 0.6, 0.9)
    t.pencolor(r, g, b)

# ---------- Dragon recursion ----------
def left_dragon(level, length, depth, max_level, rot_i, symmetry):
    if level > 0:
        left_dragon(level - 1, length, depth + 1, max_level, rot_i, symmetry)
        t.left(90)
        right_dragon(level - 1, length, depth + 1, max_level, rot_i, symmetry)
    else:
        set_depth_color(depth, max_level, rot_i, symmetry)
        t.forward(length)

def right_dragon(level, length, depth, max_level, rot_i, symmetry):
    if level > 0:
        left_dragon(level - 1, length, depth + 1, max_level, rot_i, symmetry)
        t.right(90)
        right_dragon(level - 1, length, depth + 1, max_level, rot_i, symmetry)
    else:
        set_depth_color(depth, max_level, rot_i, symmetry)
        t.forward(length)

# ---------- Mandala lattice ----------
def dragon_mandala(level, length, symmetry):
    for i in range(symmetry):
        t.penup()
        t.goto(0, 0)
        t.setheading(i * 360 / symmetry)
        t.pendown()

        left_dragon(level, length, 0, level, i, symmetry)

# ---------- Setup ----------
LEVEL = 12
LINE_LENGTH = 4
SYMMETRY = 6   # try 6, 8, 12

screen = turtle.Screen()
screen.bgcolor("black")
screen.colormode(1.0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
turtle.tracer(0, 0)

# ---------- Draw ----------
dragon_mandala(LEVEL, LINE_LENGTH, SYMMETRY)

turtle.update()
turtle.done()
