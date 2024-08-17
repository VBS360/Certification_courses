#Write your code below this row 👇
Number = 0
for Numbers in range (1,101):
    Number += 1
    if Number % 3 == 0 and Number% 5 != 0:
        print("Fizz")
    elif Number % 5 == 0 and Number% 3 != 0:
        print("Buzz")
    elif Number % 3 == 0 and Number % 5 ==0:
        print("FizzBuzz")
    else:
        print(Number)