import random
from art import logo
from replit import clear

def get_random_card():
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  get_card=random.choice(cards)
  return get_card
def calculate_score(cards):
  if sum(cards)==21 and len(cards)==2:
    return 0
  if sum(cards)>21 and 11 in cards:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
def compare(user_score,computer_score):
  if computer_score==user_score:
    return "Draw"
  elif computer_score==0:
    return "You Lose,Opponent has a Blackjack"
  elif user_score==0:
    return "You win,You have a Blackjack"
  elif user_score>21:
    return "You went over,You lose"
  elif computer_score>21:
    return "Opponent went over,You win"
  elif user_score>computer_score:
    return "You win"
  else:
    return "You lose"


def blackjack_game():
  print(logo)
  user_cards=[]
  computer_cards=[]
  get_a_new_card=False
  for _ in range(2):
    user_cards.append(get_random_card())
    computer_cards.append(get_random_card())

  while not get_a_new_card:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score>21 or user_score==0 or computer_score==0:
      get_a_new_card=True
    else:
      asking_for_card=input("Type 'y' to get another card,type 'n' to pass: ")
      if asking_for_card=='y':
        user_cards.append(get_random_card())
      else:
        get_a_new_card=True
  while computer_score!=0 and computer_score<17:
    computer_cards.append(get_random_card())
    computer_score=(calculate_score(computer_cards))    
      
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")    
  print(compare(user_score,computer_score))
  

while input("Do you want to play a game of blackjack? Type 'y' or 'n': ")=='y':
  clear()
  blackjack_game()
  



