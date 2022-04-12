
from turtle import Turtle, Screen
import random


timmy = Turtle()

timmy.hideturtle()
timmy.shape('turtle')
timmy.color('medium sea green')

colors = ['black', 'maroon', 'purple', 'fuchsia', 'green', 'olive', 'yellow', 'blue']


def draw_shape(number_sides):

    angle = 360 / number_sides
    for i in range(number_sides):

        timmy.forward(100)
        timmy.right(angle)


for number_of_side in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(number_of_side)


screen = Screen()
screen.exitonclick()
