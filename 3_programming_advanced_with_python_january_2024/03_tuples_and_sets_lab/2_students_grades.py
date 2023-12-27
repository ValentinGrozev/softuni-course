# First solution:
number_of_students = int(input())
students_record = {}

for student in range(number_of_students):
    student_name, grade = input().split()
    if student_name not in students_record:
        students_record[student_name] = []
    students_record[student_name].append(float(grade))

for students, grades in students_record.items():
    formatted_grades = ' '.join([f"{curr_grade:.2f}" for curr_grade in grades])
    print(f"{students} -> {formatted_grades} (avg: {sum(grades) / len(grades):.2f})")


# Second solution:
# number_of_students = int(input())
# students_record = {}
#
# for student in range(number_of_students):
#     student_name, grade = input().split()
#     if student_name not in students_record:
#         students_record[student_name] = []
#     students_record[student_name].append(float(grade))
#
# for students, grades in students_record.items():
#     print(f"{students} -> ", end='')
#     for grade in grades:
#         print(f"{grade:.2f}", end=' ')
#     print(f"(avg: {sum(grades) / len(grades):.2f})")
