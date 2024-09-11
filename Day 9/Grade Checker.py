student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = student_scores

for grades in student_grades:
    if student_grades[grades] > 90:
        student_grades[grades] = "Outstanding"
    elif student_grades[grades] > 80:
        student_grades[grades] = "Exceeds Expectations"
    elif student_grades[grades] > 70:
        student_grades[grades] = "Acceptable"
    else:
        student_grades[grades] = "Fail"
        
print(student_grades)
