# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S":                                         #Small Pizza Conditions
    bill = 15
    print("Small Pizza: $15")
    if add_pepperoni == "Y":                            #Small Pizza Pepperoni
        bill += 2
        print("Pepperroni will be $2")
elif size == "M":                                       #Medium Pizza Conditions
    bill = 20
    print("Medium Pizza: $20")
    if add_pepperoni == "Y":                            #Medium Pizza Pepperoni
        bill += 3
        print("Pepperroni will be $3")
elif size == "L":                                       #Large Pizza Conditions
    bill = 25
    print("Large Pizza: $25")
    if add_pepperoni == "Y":                            #Large Pizza Pepperoni
        bill += 3
        print("Pepperroni will be $3")
if extra_cheese == "Y":                                 #Extra cheese Condition
    bill += 1
    print("Extra cheese will be $1")
print(f"Your final bill is: ${bill}")                   #Final bill Amount