from dis import dis
from hangman_art import stages,logo
from hangman_words import word_list

from replit import clear
import random


random_word=random.choice(word_list)
word_length=len(random_word)
game_ends=False
lives=6

print(logo)

print(f"psss word is {random_word}")


display=[]
for _ in range(word_length):
    display+='_'

while not game_ends:
    guess=input('Choose a letter: ').lower()
    clear()
    if guess  in display:
        print(f"You've already guessed letter: {guess}")
    for position in range(word_length):
        letter=random_word[position]
        if letter==guess:
            display[position]=letter
          
   
    if guess not in random_word:
        lives-=1
        print(f"You choosed a letter {guess} ,That is not in word.You lose a life")
        if lives==0:
            game_ends=True
            print('You Lose')
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        game_ends=True
        print("You win")
    
    print(stages[lives])
    