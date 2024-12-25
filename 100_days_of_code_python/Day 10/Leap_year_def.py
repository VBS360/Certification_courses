year = int(input("Enter the year.: "))

def is_leap_year(year):
    is_leap = True
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return  True
            return False
        return True

if is_leap_year(year):
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")
