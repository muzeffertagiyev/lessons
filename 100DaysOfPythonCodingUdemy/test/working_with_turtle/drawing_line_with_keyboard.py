from os import scandir
import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forward():
    tim.fd(10)

def move_backward():
    tim.bk(10)

def turn_left():
    tim.lt(10)

def turn_right():
    tim.rt(10)

def clear():
    tim.reset()

screen.listen()
screen.onkey(fun = move_forward, key = 'w')
screen.onkey(move_backward, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear, 'c')


screen.exitonclick()