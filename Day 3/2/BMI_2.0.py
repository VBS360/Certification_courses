# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = float(weight)/float(height)**2
# BMI = int(round(BMI),2)
# print(weight + " ÷ " + "(" + height + " x " + height + ")" + " = " + str(BMI))
# print(BMI)
BMI_Int = round(BMI)

if BMI <= 18.5:
    print(f"Your BMI is {BMI_Int}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI_Int}, you have a normal weight.")
elif BMI< 30:
    print(f"Your BMI is {BMI_Int}, you are slightly overweight.")
elif BMI< 35:
    print(f"Your BMI is {BMI_Int}, you are obese.")
else:
    print(f"Your BMI is {BMI_Int}, you are clinically obese.")

# print("Your bmi is {BMI_Int}")