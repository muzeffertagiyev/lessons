import turtle as t
import random


tim = t.Turtle()
t.colormode(255)   # to show that our color mode will be in RGB mode


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed('fastest')


def spinograph(size):
    for _ in range(int(360 / size)):
        tim.color(random_color())
        tim.circle(100)
        position = tim.heading()    #gets our turtle's current position 
        tim.setheading(position + size)


spinograph(3)


screen = t.Screen()
screen.exitonclick()