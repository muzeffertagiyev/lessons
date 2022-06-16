import random
import colorgram

import turtle as t

# getting colors from our image
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.g
    rgb = (red, green, blue)
    rgb_colors.append(rgb)

t.colormode(255)

tim = t.Turtle()
tim.hideturtle()
tim.penup()
tim.speed('fastest')

# to the starting point
tim.setheading(225)
tim.forward(300)
tim.setheading(180)
tim.forward(100)
tim.setheading(0)

# starting to make dots
number_of_dots = 100
for dot in range(1, number_of_dots+1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)
    if dot % 10 ==0:
        tim.left(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()
