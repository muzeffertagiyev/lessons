import pandas
import turtle

image = 'blank_states_img.gif'
screen = turtle.Screen()
screen.title('U.S. states game')
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv('50_states.csv')

all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_input = screen.textinput(title=f'{len(guessed_states)}/50 States Correct', prompt="What's another state's name?").title()

    if answer_input == 'Exit':
        missing_states = [state for state in all_states if state not in guessed_states]
        data_of_missing_states = pandas.DataFrame(missing_states)
        data_of_missing_states.to_csv('missing_states.csv')
        break

    if answer_input in all_states:
        guessed_states.append(answer_input)
        states = data[data.state == answer_input]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(states.x), int(states.y))
        t.write(answer_input)

