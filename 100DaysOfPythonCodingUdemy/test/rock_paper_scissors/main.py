import random
from ascii_art import rock,paper,scissors

all_choices=[rock,paper,scissors]

computer_choice=random.randint(0,2)
user_choice=int(input('Enter your choice.0 for Rock,1 for Paper,2 for Scissors: \n'))


if user_choice>=3 or user_choice<0:
    print("You typed wrong,You lost")
else:
    print(f"Your choice: \n{all_choices[user_choice]}")
    print(f"Computer choice: \n{all_choices[computer_choice]} ")


    user_win='You win'
    computer_win='Computer Wins'

    if user_choice==0 and computer_choice==2:
        print(user_win)
    elif user_choice==2 and computer_choice==0:
        print(computer_win)
    elif user_choice>computer_choice:
        print(user_win)
    elif computer_choice>user_choice:
        print(computer_win)
    else:
        print('Draw')

    