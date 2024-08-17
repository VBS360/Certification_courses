# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

def Leap(year):
    IsLeapYear = True
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0) :
        return IsLeapYear
    else :
        return not IsLeapYear
        
if Leap(year):
    print(f'{year} is a leap year.')
else:
    print(f'{year} is not a leap year.')