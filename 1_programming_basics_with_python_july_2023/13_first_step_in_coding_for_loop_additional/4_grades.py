number_of_students = int(input())

low_grade_count = 0    # 2.00 to 2.99
med_grade_count = 0    # 3.00 to 3.99
good_grade_count = 0   # 4.00 to 4.99
excellent_grade_count = 0  # 5.00 to 6.00
all_grades = 0

for student in range(number_of_students):
    grade = float(input())
    if 2 <= grade <= 2.99:
        low_grade_count += 1
        all_grades += grade
    elif 3 <= grade <= 3.99:
        med_grade_count += 1
        all_grades += grade
    elif 4 <= grade <= 4.99:
        good_grade_count += 1
        all_grades += grade
    else:
        excellent_grade_count += 1
        all_grades += grade

average_grade = all_grades / number_of_students
low_percent = (low_grade_count / number_of_students) * 100
med_percent = (med_grade_count / number_of_students) * 100
good_percent = (good_grade_count / number_of_students) * 100
excellent_percent = (excellent_grade_count / number_of_students) * 100

print(f"Top students: {excellent_percent:.2f}%")
print(f"Between 4.00 and 4.99: {good_percent:.2f}%")
print(f"Between 3.00 and 3.99: {med_percent:.2f}%")
print(f"Fail: {low_percent:.2f}%")
print(f"Average: {average_grade:.2f}")
