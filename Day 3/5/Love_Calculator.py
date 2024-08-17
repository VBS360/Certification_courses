year = int(input("Which year you want to check \n"))

if year%4 == 0 or year%400 ==0:
    if year%100 != 0:
        print("Leap!")
else:
    print("Not Leap!")