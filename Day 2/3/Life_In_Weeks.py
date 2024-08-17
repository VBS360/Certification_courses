# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
Max_Age_Year = int(90-int(age))
Max_Age_Months = int(12*int(Max_Age_Year))
Max_Age_Weeks = int(52*int(Max_Age_Year))
Max_Age_Days = int(365*int(Max_Age_Year))

print(f"You have {Max_Age_Days} days, {Max_Age_Weeks} weeks, and {Max_Age_Months} months left.")