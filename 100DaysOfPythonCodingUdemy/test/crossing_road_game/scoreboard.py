from turtle import Turtle


FONT = ('courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align='left', font=FONT)
        
    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)


    