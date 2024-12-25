def life_in_weeks(current_age):
    remaining_age_years = 90 - current_age
    remaining_age_weeks = remaining_age_years * 52
    print(f"You have {remaining_age_weeks} weeks left.")

current_age = int(input("What is your current age?\n"))
life_in_weeks(current_age)
