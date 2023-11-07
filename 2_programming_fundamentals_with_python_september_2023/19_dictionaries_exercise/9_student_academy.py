number_of_students = int(input())

students_grade_register = {}

for student in range(number_of_students):
    student_name = input()
    student_grade = float(input())
    if student_name not in students_grade_register:
        students_grade_register[student_name] = 0
        students_grade_register[student_name] = student_grade
    else:
        students_grade_register[student_name] += student_grade
        students_grade_register[student_name] /= 2


for name, average_grade in students_grade_register.items():
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
