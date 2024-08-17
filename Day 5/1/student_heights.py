# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
#Write your code below this row 👇
Total_height = 0
for height in student_heights:
    Total_height += height
# print(Total_height)

No_Of_Student = 0
for student in student_heights:
  No_Of_Student += 1
# print(No_Of_Student)

Average_height = Total_height/No_Of_Student
print(round(Average_height))