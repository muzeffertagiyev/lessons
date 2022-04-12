from optparse import check_choice
from game_data import data
from art import logo,vs
import random
from replit import clear


def printing_data(account):
    """Adding account and Returning data in readable format"""
    account_name=account['name']
    account_desc=account['description']
    account_country=account['country']
    article=''
    if account_desc[0] in ['a','o','e','i','u']:
        article='an'
    else:
        article='a'
    return f"{account_name}, {article} {account_desc}, from {account_country}"
def check_score(guess,account_a,account_b):
    if account_a>account_b and guess=='a':
        return True
    elif account_a<account_b and guess=='b':
        return True
    else:
        return False
        


def game():
    print(logo)
    score=0
    game_should_continue=True
    account_a=random.choice(data)
    account_b=random.choice(data)

    while game_should_continue:
        account_a=account_b
        account_b=random.choice(data)
        while account_a==account_b:
            account_b=random.choice(data)
        account_a_count=account_a['follower_count']
        account_b_count=account_b['follower_count']
        print(f"Compare A: {printing_data(account_a)}")
        print(vs)
        print(f"Against B: {printing_data(account_b)}")
        guess=input("Who has more followers.Type 'A' or 'B' : ").lower()
        is_correct=check_score(guess,account_a_count,account_b_count)
        clear()
        print(logo)
        if is_correct:
            score+=1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue=False
            print(f"Sorry, that's wrong. Final score: {score}")
game()