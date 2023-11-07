course_and_student_name = input()

course_information = {}

while ":" in course_and_student_name:
    information = course_and_student_name.split(" : ")
    course = information[0]
    student_name = information[1]
    if course not in course_information:
        course_information[course] = []
    course_information[course].append(student_name)

    course_and_student_name = input()

for key, values in course_information.items():
    print(f"{key}: {len(course_information[key])}")
    for name in values:
        print(f"-- {name}")
