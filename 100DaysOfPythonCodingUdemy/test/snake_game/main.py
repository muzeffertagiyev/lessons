from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)    # it is main for our snake ,we will use update function in our while loop
# we should use time.sleep method too,to make our snake slow
screen.title("My snake game")

snake = Snake()
food = Food()
our_scoreboard = ScoreBoard()


screen.listen()
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)

game_is_on = True
while game_is_on:
    screen.update()  #screen is updating in every 0.1 seconds,means that our snake starts to move
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        our_scoreboard.increase_score()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 270 or snake.head.ycor() < -280:
        our_scoreboard.reset_score()
        snake.reset_snake()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            our_scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()
