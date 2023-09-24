jury_number = int(input())
presentation_name = input()

average_grade = 0
all_grades = 0
grades = 0

while presentation_name != "Finish":
    for grade in range(0, jury_number):
        presentation_grade = float(input())
        average_grade += presentation_grade
        all_grades += presentation_grade
        grades += 1
    print(f"{presentation_name} - {average_grade / jury_number:.2f}.")

    presentation_name = input()
    average_grade = 0

print(f"Student's final assessment is {all_grades / grades:.2f}.")