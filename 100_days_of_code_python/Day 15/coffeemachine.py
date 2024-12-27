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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resource_deficiency():
    global available_water, available_coffee, available_milk, profit, change, espresso_water, latte_water, cappuccino_water, espresso_coffee, latte_coffee, 
    global cappuccino_coffee, latte_milk, cappuccino_milk, total_collection
    
    if change < 0:
            print("Sorry that's not enough money. Money refunded.")
    elif available_water < espresso_water or available_water < latte_water or available_water < cappuccino_water:
        print("Sorry there is not enough water.")
    elif available_coffee >= espresso_coffee or available_coffee< latte_coffee or available_coffee < cappuccino_coffee:
        print("Sorry there is not enough coffee.")
    elif available_milk < latte_milk or available_milk < cappuccino_milk:
        print("Sorry there is not enough milk.")
    return coffee_machine()

def insert_coin():
    print("Please insert coins.")
    no_quarters = 0.25 * int(input("How many quarters?: "))
    no_dimes = 0.10 * int(input("How many dimes?: "))
    no_nickles = 0.05 * int(input("How many nickles?: "))
    no_pennies = 0.01 * int(input("How many pennies?: "))

    total_collection = no_quarters + no_dimes + no_nickles + no_pennies
    return total_collection
    
def coffee_machine():
    global available_water, available_coffee, available_milk, profit, change, espresso_water, latte_water, cappuccino_water, espresso_coffee, latte_coffee, 
    global cappuccino_coffee, latte_milk, cappuccino_milk, total_collection
    
    user_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_coffee == 'espresso':
        insert_coin()
        espresso_water = MENU ['espresso']['ingredients']['water']
        espresso_coffee = MENU ['espresso']['ingredients']['coffee']
        espresso_price = MENU ['espresso']['cost']
        change = round(total_collection - espresso_price,2)

        if change >= 0 and available_water >= espresso_water and available_coffee >= espresso_coffee:
            profit += MENU ['espresso']['cost']
            available_water -= espresso_water
            available_coffee -= espresso_coffee
            print(f"Here is ${change} in change.")
            print(f'Here is your {user_coffee} ☕ Enjoy!')
            coffee_machine()
        else:
            resource_deficiency()
            
    elif user_coffee == 'latte':
        insert_coin()
        latte_water = MENU ['latte']['ingredients']['water']
        latte_coffee = MENU ['latte']['ingredients']['coffee']
        latte_milk = MENU ['latte']['ingredients']['milk']
        latte_price = MENU ['latte']['cost']
        change = round(total_collection - latte_price,2)

        if change >= 0 and available_water >= latte_water and available_coffee >= latte_coffee and available_milk >= latte_milk:
            profit += MENU ['latte']['cost']
            available_water -= latte_water
            available_coffee -= latte_coffee
            available_milk -= latte_milk
            print(f"Here is ${change} in change.")
            print(f'Here is your {user_coffee} ☕ Enjoy!')
            coffee_machine()
        else:
            resource_deficiency()
            
    elif user_coffee == 'cappuccino':
        insert_coin()
        cappuccino_water = MENU ['cappuccino']['ingredients']['water']
        cappuccino_coffee = MENU ['cappuccino']['ingredients']['coffee']
        cappuccino_milk = MENU ['cappuccino']['ingredients']['milk']
        cappuccino_price = MENU ['cappuccino']['cost']
        change = round(total_collection - cappuccino_price,2)

        if change >= 0 and available_water >= cappuccino_water and available_coffee >= cappuccino_coffee and available_milk >= cappuccino_milk:
            profit += MENU ['latte']['cost']
            available_water -= cappuccino_water
            available_coffee -= cappuccino_coffee
            available_milk -= cappuccino_milk
            print(f"Here is ${change} in change.")
            print(f'Here is your {user_coffee} ☕ Enjoy!')
            coffee_machine()
        else:
            resource_deficiency()
    elif user_coffee == 'report':
        print(f"Water: {available_water}ml")
        print(f"Milk: {available_milk}ml")
        print(f"Coffee: {available_coffee}g")
        print(f"Money: ${profit}")
        coffee_machine()
    elif user_coffee == 'off':
        return
    else:
        print('Enter proper value for coffee type.')

profit = 0    
available_water = resources['water']
available_coffee = resources['coffee']
available_milk = resources['milk']

coffee_machine()
