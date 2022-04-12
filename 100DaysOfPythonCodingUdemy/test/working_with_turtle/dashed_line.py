from turtle import Turtle, Screen, screensize


tim = Turtle()

for _ in range(50):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = Screen()
screen.exitonclick()