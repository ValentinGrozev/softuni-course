information = input()
students_info = {}

while ":" in information:
    student_information = information.split(":")
    student_name = student_information[0]
    student_id = student_information[1]
    student_course = student_information[2]
    if student_course not in students_info:
        students_info[student_course] = {}
    students_info[student_course][student_id] = student_name

    information = input()

information = ' '.join(information.split("_"))

for key, values in students_info.items():
    if key == information:
        for student_id, student_name in values.items():
            print(f"{student_name} - {student_id}")
