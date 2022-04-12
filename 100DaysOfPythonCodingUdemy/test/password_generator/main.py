from base import letters,symbols,numbers
import random

print("Welcome to the PyPassword Generator!")

nr_letters=int(input("How many letters do you want to be in your password:\n"))
nr_symbols=int(input("How many symbols do you want to be in your password:\n"))
nr_numbers=int(input("How many numbers do you want to be in your password:\n"))

password=[]
for char in range(1,nr_letters+1):
    password+=random.choice(letters)
for char in range(1,nr_symbols+1):
    password+=random.choice(symbols)
for char in range(1,nr_numbers+1):
    password+=random.choice(numbers)

random.shuffle(password)

final_password=''
for unsorted_password in password:
    final_password+=unsorted_password
print(f"Your generated password is: {final_password}")

