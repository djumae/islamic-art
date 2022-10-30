'''
Author: djumae
Last modified date: October 24, 2022
Purpose: to draw geometric patterns commonly in Islamic art

Test cases:
1. sides_inside = 15, sides_outside = 5
2. sides_inside = 5, sides_outside = 7
3. sides_inside = 3, sides_outside = 5

'''


import turtle
import random
#initialize variables
sides_inside = 15
sides_outside = 5
length_sides_inside = 10
length_sides_outside = 30
iterations = 10
win_length = 500
win_height = 500
x_position = -200
y_position = 200

#set up the pen
t = turtle.Turtle()
turtle.screensize(win_length,win_height)
t.speed('fastest')
#like turbo mode in scratch
turtle.tracer(0,0)
turtle.colormode(255)
r = random.randrange(0,256,10)
g = random.randrange(0,256,10)
b = random.randrange(0,256,10)
t.pencolor(r,g,b)
#pen movement
for a in range(0, 5):
    t.penup()
    x_position = -200
    t.setposition(x_position, y_position)
    for b in range(0, 6):
        t.pendown()
        for c in range(0, iterations):
            for d in range(0, sides_inside):
                t.forward(length_sides_inside)
                t.right(360/sides_inside)
            t.right(360/iterations)
        for e in range(0, iterations):
            for f in range(0, sides_outside):
                t.forward(length_sides_outside)
                t.right(360/sides_outside)
            t.right(360/iterations)
        t.penup()
        x_position += 79
        t.setx(x_position)
        r = random.randrange(0, 256, 10)
        g = random.randrange(0, 256, 10)
        b = random.randrange(0, 256, 10)
        t.pencolor(r, g, b)
    y_position -= 66

turtle.done()
