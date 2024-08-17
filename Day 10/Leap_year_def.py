def is_leap_year(year):
    is_leap_year = True
    if year % 4 != 0 or year % 100 == 0:
        is_leap_year = False
    elif year % 4 == 0 and year % 400 == 0:
        is_leap_year = True
    elif year % 4 == 0:
        is_leap_year = True
    print(is_leap_year)
        
is_leap_year(2400)