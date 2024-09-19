MENU = {
    "espresso":{
        "ingredients":{
            "water":50,
            "milk":0,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
         "ingredients":{
             "water":200,
             "milk":150,
             "coffee":24,
        },
    "cost":2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
    "cost":3.0,
    }
}

resources = {
        "water":300,
        "milk":200,
        "coffee":100,
}

collection = 0
user_bill = 0
user_payment = 0

def remaining_resouces():
    global resources,collection
    rem_water = resources["water"]
    rem_milk = resources["milk"]
    rem_coffee = resources["coffee"]
    total_collection = collection
    print(f" remaining water = {rem_water}\n remaining milk = {rem_milk}\n remaining coffee = {rem_coffee}\n Total collection = {total_collection}\n")

def machine_start():
    global user_choice, collection, user_bill
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    user_choice = user_choice.lower()
    return make_coffee()


def bill_amount():
    global user_choice, collection, user_bill
    if user_choice == "espresso":
        user_bill = MENU["espresso"]["cost"]
    elif user_choice == "latte":
        user_bill = MENU["latte"]["cost"]
    elif user_choice == "cappuccino":
        user_bill = MENU["cappuccino"]["cost"]

def payment():
    global user_choice, collection, user_bill, user_payment
    print("Please insert coins.\n")
    querter = int(input("How many querter? "))
    querter = querter * 0.25
    dime = int(input("How many dime? "))
    dime = dime * 0.1
    nickel = int(input("How many nickel? "))
    nickel = nickel * 0.05
    penny = int(input("How many penny? "))
    penny = penny * 0.01
    user_payment = penny + nickel + dime + querter
    user_payment = round(user_payment,2)
    bill_amount()
    if user_payment == user_bill:
        collection += user_payment
        print(f"Here is your {user_choice} Enjoy!")
        return machine_start()
    elif user_payment > user_bill:
        refund_amount = user_payment - user_bill
        refund_amount = round(refund_amount,2)
        collection += user_bill
        print(f"Here is ${refund_amount} in change")
        print(f"Here is your {user_choice} Enjoy!")
        return machine_start()
    else:
        print("Sorry that's not enough money. Money refunded.")
        return machine_start()

def make_coffee():
    global user_choice, collection,resources
    if user_choice == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["milk"] >= MENU["espresso"]["ingredients"]["milk"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU["espresso"]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
            payment()
        else:
            for ingredient in resources:
                if resources[ingredient] < MENU["espresso"]["ingredients"][ingredient]:
                    print(f"Sorry there is not enough {ingredient}")
                    return machine_start()
    elif user_choice == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"] and resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
            resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
            payment()
        else:
            for ingredient in resources:
                if resources[ingredient] < MENU["latte"]["ingredients"][ingredient]:
                    print(f"Sorry there is not enough {ingredient}")
                    return machine_start()
    elif user_choice == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"] and resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
            resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
            payment()
        else:
            for ingredient in resources:
                if resources[ingredient] < MENU["cappuccino"]["ingredients"][ingredient]:
                    print(f"Sorry there is not enough {ingredient}")
                    return machine_start()
    elif user_choice == "report":
        remaining_resouces()
        return machine_start()
    else:
        print("Invalid value. Please enter proper value")
        return machine_start()
    
machine_start()
