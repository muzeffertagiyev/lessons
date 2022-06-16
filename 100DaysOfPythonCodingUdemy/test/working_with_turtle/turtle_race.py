import random
import turtle as t


screen = t.Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Color Bet', prompt='Which turtle will win? Choose color ')
turtles = []
colors = ['red', 'purple', 'blue', 'yellow', 'pink', 'green' ]


y = -100
for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y)
    turtles.append(new_turtle)
    y += 40


if user_bet:
    race_is_on = True
while race_is_on:
    for turtle in turtles:
        random_step = random.randint(0, 10)
        turtle.fd(random_step)

        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f'You have won.Color {winning_color} is winner')
            else:
                print(f"You have lost.Color {winning_color} is winner")


screen.exitonclick()