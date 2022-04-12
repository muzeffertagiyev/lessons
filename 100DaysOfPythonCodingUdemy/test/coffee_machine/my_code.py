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


def coins():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)


# TODO: Costs for espresso
espresso_water_cost = MENU['espresso']['ingredients']['water']
espresso_coffee_cost = MENU['espresso']['ingredients']['coffee']
espresso_cost = MENU['espresso']['cost']
# TODO:costs for latte
latte_water_cost = MENU['latte']['ingredients']['water']
latte_milk_cost = MENU['latte']['ingredients']['milk']
latte_coffee_cost = MENU['latte']['ingredients']['coffee']
latte_cost = MENU['latte']['cost']
# TODO: costs for cappuccino
cappuccino_water_cost = MENU['cappuccino']['ingredients']['water']
cappuccino_milk_cost = MENU['cappuccino']['ingredients']['milk']
cappuccino_coffee_cost = MENU['cappuccino']['ingredients']['coffee']
cappuccino_cost = MENU['cappuccino']['cost']

water_left = resources['water']
milk_left = resources['milk']
coffee_left = resources['coffee']


money_inside_machine = 0
machine_works = True
your_exchange = float(0)
while machine_works:

    question = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if question == 'off':
        machine_works = False
    elif question == 'report':
        print(f"Water: {water_left}\nMilk: {milk_left}\nCoffee: {coffee_left}\nMoney:${money_inside_machine}")
    elif question == 'espresso':
        if water_left >= espresso_water_cost and coffee_left >= espresso_coffee_cost:
            your_money = coins()
            if your_money >= espresso_cost:
                water_left -= espresso_water_cost
                coffee_left -= espresso_coffee_cost
                your_exchange = round(your_money-espresso_cost, 2)
                money_inside_machine += espresso_cost
                print(f"Here is ${your_exchange} dollars in change.")
                print("Here is your espresso ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        elif water_left < espresso_water_cost:
            print("Sorry there is not enough water.")
        elif coffee_left < espresso_coffee_cost:
            print("Sorry there is not enough coffee.")
    elif question == 'latte':
        if water_left >= latte_water_cost and coffee_left >= latte_coffee_cost:
            your_money = coins()
            if your_money >= latte_cost:
                water_left -= latte_water_cost
                coffee_left -= latte_coffee_cost
                milk_left -= latte_milk_cost
                your_exchange = round(your_money-latte_cost, 2)
                money_inside_machine += latte_cost
                print(f"Here is ${your_exchange} dollars in change.")
                print("Here is your latte ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        elif water_left < latte_water_cost:
            print("Sorry there is not enough water.")
        elif coffee_left < latte_coffee_cost:
            print("Sorry there is not enough coffee.")
        elif milk_left < latte_milk_cost:
            print("Sorry there is not enough milk.")
    elif question == 'cappuccino':
        if water_left >= cappuccino_water_cost and coffee_left >= cappuccino_coffee_cost:
            your_money = coins()
            if your_money >= cappuccino_cost:
                water_left -= cappuccino_water_cost
                coffee_left -= cappuccino_coffee_cost
                milk_left -= cappuccino_milk_cost
                your_exchange = round(your_money-cappuccino_cost, 2)
                money_inside_machine += cappuccino_cost
                print(f"Here is ${your_exchange} dollars in change.")
                print("Here is your cappuccino ☕️. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        elif water_left < cappuccino_water_cost:
            print("Sorry there is not enough water.")
        elif coffee_left < cappuccino_coffee_cost:
            print("Sorry there is not enough coffee.")
        elif milk_left < cappuccino_milk_cost:
            print("Sorry there is not enough milk.")
    else:
        print("You misstyped the name of coffee")