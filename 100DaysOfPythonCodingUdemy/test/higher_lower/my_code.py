from game_data import data
from art import logo,vs
from random import randint
from replit import clear

def random_user():
  random_number=randint(0,len(data)-1)
  user=data[random_number]
  return user

def printing_user(users):
  our_user=users
  article=''
  if our_user['description'][0].lower() in ['a','o','u','e','i']:
    article='an'
  else:
    article='a'
  return f"{our_user['name']}, {article} {our_user['description']}, from {our_user['country']}."

def game():
  end_game=False
  score=0
  user_a=random_user()
  
  while not end_game:
    clear()
    print(logo)
    if score>0:
        print(f"You get it right,your current score is {score}")
    user_b=random_user()
    
    if user_a==user_b:
      user_b=random_user()
    printing_user_a=printing_user(user_a)
    printing_user_b=printing_user(user_b)
    user_a_score=user_a['follower_count']
    user_b_score=user_b['follower_count']
    print(f"user a: {user_a['follower_count']}")
    print(f"user b: {user_b['follower_count']}")
    print(f"Compare A: {printing_user_a}")
    print(vs)
    print(f"Against B: {printing_user_b}")
    question=input("Who has more followers? Type 'A' or 'B': ").upper()
    if question=='A':
      if user_a_score>user_b_score:
        score+=1 
        user_a=user_b
      else:
        print(logo)
        print(f"You got it wrong,Your final score is {score}")
        end_game=True
    elif question=='B':
      if user_b_score>user_a_score:
        score+=1
        user_a=user_b
      else:
        clear()
        print(logo)
        print(f"You got it wrong, Your final score is {score}")
        end_game=True
game() 
