from turtle import *
from random import randint

speed(0)
bgcolor("black")
x = 1
while x < 40000:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    colormode(255)
    pencolor(r, g, b)
    fd(50 + x)  # Corrected: used fd() function instead of assigning to fd
    rt(90.911)  # Corrected: used rt() function instead of assigning to rt
    x += 1
exitonclick()
