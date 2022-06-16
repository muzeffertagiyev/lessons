from cgitb import text
from operator import index
from textwrap import fill
from tkinter import *
import random
import pandas

BACKGROUND_COLOR = '#B1DDC6'
word = {}
data_dict = {}


try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/English_turkish.csv')
    data_dict = original_data.to_dict(orient='records')
else: 
    data_dict = data.to_dict(orient='records')



def next_word():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(data_dict)
    canvas.itemconfig(card_title, text='English', fill='black')
    canvas.itemconfig(card_word, text=word['English'], fill='black')
    canvas.itemconfig(background, image=white_img)
    flip_timer = window.after(3000,func=flip_card)


def is_known():
    data_dict.remove(word)
    data = pandas.DataFrame(data_dict) # it creates list of dictionaries
    data.to_csv('data/words_to_learn.csv', index=False) # it creates new csv file from list of dictionaries
    # if we use index = False  id numbers will not be created for words
    next_word()


def flip_card():
    canvas.itemconfig(background, image=green_img)
    canvas.itemconfig(card_title, text='Turkish', fill='white')
    canvas.itemconfig(card_word, text=word['Turkish'], fill='white')


window = Tk()
window.title('English-Turkish')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,flip_card)


canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
white_img = PhotoImage(file='images/card_front.png')
green_img = PhotoImage(file='images/card_back.png')
background = canvas.create_image(400, 263, image=white_img)
canvas.grid(column=0, row=0, columnspan=2)

# Texts
card_title = canvas.create_text(400, 150, text='title', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='word', font=('Ariel', 60, 'bold'))

# Buttons
wrong_img = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=wrong_img, highlightthickness=0, command=next_word)
unknown_button.grid(column=0, row=1)

right_img = PhotoImage(file='images/right.png')
known_button = Button(image=right_img, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_word()
window.mainloop()
