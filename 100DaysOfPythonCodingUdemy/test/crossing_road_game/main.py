import time
from turtle import Screen
from player import Player
from car_manager import Car_manager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.title('Road Crossing')
screen.tracer(0)

player = Player()
car_manager = Car_manager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.go_up, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()


    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.level_up()




screen.exitonclick()