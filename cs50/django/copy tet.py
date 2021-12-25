import random


number = random.randint(1,10)


i=0
while True:
    guess=int(input("Guess the number between 1 and 10:  "))
    i+=1
    if i==3:
        print("You Failed,too many tries ")
        break 
    elif guess>number:
        print("You guessed wrong,pick smaller number")
    elif guess<number:
        print("You guessed wrong,pick bigger number")
    else:
        print(f"Congratulations,You guessed correctly,in the {i} try")
        break
    
# def main():

#     number=random.randint(1,10)

#     for i in range(3):
#         guess=int(input("Guess a number between 1 and 10: "))
#         if guess>number :
#             print("Guess smaller")
#         elif guess<number :
#             print("Guess bigger ")
#         else:
#             print(f"you gussed correctly at {i+1} try")
#             return
# main()

        

    
    
    
    



    


