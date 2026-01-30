import turtle
import colorsys
import math

# ---------- Teal / Aqua / Jade palette ----------
def teal_palette(depth, max_level, ring_i, ring_count, arm_i, symmetry):
    d = depth / max_level
    r = ring_i / max(1, ring_count - 1)
    a = arm_i / symmetry

    # Teal-focused hue band
    hue = (0.48 + 0.08 * (1 - d) + 0.04 * a) % 1.0
    sat = 0.75 + 0.15 * (1 - d)
    val = 0.6 + 0.4 * (1 - r)

    return colorsys.hsv_to_rgb(hue, sat, val)

# ---------- Glow draw ----------
def glow_forward(length, color):
    r, g, b = color

    for i in range(3, 0, -1):
        t.pensize(1 + i * 2)
        t.pencolor(r * 0.35, g * 0.35, b * 0.35)
        t.forward(length)
        t.backward(length)

    t.pensize(1)
    t.pencolor(color)
    t.forward(length)

# ---------- Dragon recursion ----------
def left_dragon(level, length, depth, max_level, ring_i, ring_count, arm_i, symmetry):
    if level > 0:
        left_dragon(level - 1, length, depth + 1, max_level, ring_i, ring_count, arm_i, symmetry)
        t.left(90)
        right_dragon(level - 1, length, depth + 1, max_level, ring_i, ring_count, arm_i, symmetry)
    else:
        color = teal_palette(depth, max_level, ring_i, ring_count, arm_i, symmetry)
        glow_forward(length, color)

def right_dragon(level, length, depth, max_level, ring_i, ring_count, arm_i, symmetry):
    if level > 0:
        left_dragon(level - 1, length, depth + 1, max_level, ring_i, ring_count, arm_i, symmetry)
        t.right(90)
        right_dragon(level - 1, length, depth + 1, max_level, ring_i, ring_count, arm_i, symmetry)
    else:
        color = teal_palette(depth, max_level, ring_i, ring_count, arm_i, symmetry)
        glow_forward(length, color)

# ---------- Mandala rings ----------
def dragon_mandala_rings(rings, base_radius, level, length):
    for ring_i in range(rings):
        radius = base_radius * (ring_i + 1)
        symmetry = 6 + ring_i * 2

        for arm_i in range(symmetry):
            angle = arm_i * 360 / symmetry

            t.penup()
            t.goto(0, 0)
            t.setheading(angle)
            t.forward(radius)
            t.pendown()

            left_dragon(level, length, 0, level, ring_i, rings, arm_i, symmetry)

# ---------- Setup ----------
LEVEL = 10
LINE_LENGTH = 5
RINGS = 3
BASE_RADIUS = 40

screen = turtle.Screen()
screen.bgcolor("black")
screen.colormode(1.0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(1)

turtle.tracer(0, 0)

# ---------- Draw ----------
dragon_mandala_rings(RINGS, BASE_RADIUS, LEVEL, LINE_LENGTH)

turtle.update()
turtle.done()
