from turtle import Turtle
import turtle
import colorgram
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
turtle.colormode(255)

class Car_manager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_color(self):
        rgb_colors = []
        colors = colorgram.extract('images.jpeg',40)
        for color in colors:
            red = color.rgb.r
            green = color.rgb.g
            blue = color.rgb.b
            rgb = (red, green, blue)
            rgb_colors.append(rgb)
        return rgb_colors

    def create_car(self):
        chances = random.randint(1, 6)
        if chances == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.color(random.choice(self.create_color()))
            new_car.goto(320, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
