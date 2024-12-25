## Simplified

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

n1 = float(input("What is the first number? \n"))

repeat = True
while repeat == True:
    operation = input("""+\n-\n*\n/\nPick an opeartion: """)
    n2 = float(input("What is the second number? \n"))

    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    final_num = operations[operation](n1,n2)

    cont_cal = input(f"Type 'y' to continue calculation with {final_num}, or type 'n' start a new calculation").lower()

    if cont_cal == 'y':
        n1 = final_num
    else:
        repeat = False
