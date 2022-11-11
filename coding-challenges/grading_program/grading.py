student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores.keys():
    if student_scores[student] >= 91:
        student_grades.update({student: "Outstanding"})
    elif student_scores[student] >= 81:
        student_grades.update({student: "Exceeds Expectations"})
    elif student_scores[student] >= 71:
        student_grades.update({student: "Acceptable"})
    else:
        student_grades.update({student: "Fail"})
# 🚨 Don't change the code below 👇
print(student_grades)