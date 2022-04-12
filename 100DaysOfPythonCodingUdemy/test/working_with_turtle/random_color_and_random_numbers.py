import turtle as t
import random


timmy = t.Turtle()
timmy.hideturtle()
t.colormode(255)   #so important for color rgb


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


timmy.speed('fast')
timmy.pensize(15)
angles = [0, 90, 180, 270]
random_number = random.randint(0, 255)
for _ in range(200):
    timmy.color(random_color())
    timmy.forward(20)
    timmy.setheading(random.choice(angles))


screen = t.Screen()
screen.exitonclick()
