from math import ceil

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

max_bonus_points = 0
current_student_attendance = 0

for student in range(1, number_of_students + 1):
    attendance_of_each_student = int(input())
    total_bonus = attendance_of_each_student / number_of_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus_points:
        max_bonus_points = total_bonus
        current_student_attendance = attendance_of_each_student

print(f"Max Bonus: {ceil(max_bonus_points):.0f}.")
print(f"The student has attended {ceil(current_student_attendance):.0f} lectures.")