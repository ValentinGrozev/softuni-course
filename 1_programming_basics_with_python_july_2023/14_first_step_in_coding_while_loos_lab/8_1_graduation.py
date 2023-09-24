name_of_student = input()

sum_grades = 0
fails = 0
counter_class = 0

while counter_class < 12 and fails < 2:
    grade = float(input())
    if grade >= 4:
        sum_grades += grade
        counter_class += 1
    if grade < 4:
        fails += 1

if fails >= 2:
    counter_class += 1
    print(f"{name_of_student} has been excluded at {counter_class} grade")
if counter_class == 12:
    average_points = sum_grades / 12
    print(f"{name_of_student} graduated. Average grade: {average_points:.2f}")
