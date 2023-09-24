name_of_student = input()

sum_grades = 0
fails = 0
counter_class = 0

while True:
    grade = float(input())
    if grade >= 4:
        sum_grades += grade
        counter_class += 1
    else:
        fails += 1
    if counter_class == 12:
        break
    if fails >= 2:
        counter_class += 1
        break

if counter_class == 12:
    average_points = sum_grades / 12
    print(f"{name_of_student} graduated. Average grade: {average_points:.2f}")
else:
    print(f"{name_of_student} has been excluded at {counter_class} grade")
