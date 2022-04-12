from tracemalloc import stop
from art import logo

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}



def calculator():
    print(logo)
    num1=int(input("Enter a number: "))
    for operator in operations:
        print(operator)


    stop_calculator=False
    while not stop_calculator:
        choose_operator=input("Choose an operation: ")
        num2=int(input("Enter the next number: "))
        calculation_function=operations[choose_operator]
        answer=calculation_function(num1,num2)
        print(f"{num1} {choose_operator} {num2} = {answer}")

        if input(f"Type 'y' to continue with {answer},or type 'n' to start a new calculation: ")=='y':
            num1=answer
        else:
            stop_calculator=True
            calculator()

calculator()