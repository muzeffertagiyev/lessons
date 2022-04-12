from time import sleep

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 150,
}


def is_resources_sufficient(value_of_ingredients):
    """Return True if resources is sufficient ,but false is resources is insufficient"""
    for item in value_of_ingredients:
        if value_of_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return (quarters*0.25)+(dimes*0.1)+(nickles*0.05)+(pennies*0.01)


def transaction_successful(money_received, drink_cost):
    """It returns True if Transaction successful,else returns false"""
    if money_received >= drink_cost:
        change = round(money_received - drink['cost'], 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deducting value of resources"""
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]

    print(f"Here is your {drink_name} ☕️. Enjoy!")


profit = 0
machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        print("Turning off...")
        sleep(2)
        print("Coffee machine turned off")
        machine_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink['ingredients']):
            your_money = coins()
            if transaction_successful(your_money, drink['cost']):
                make_coffee(choice, drink['ingredients'])
