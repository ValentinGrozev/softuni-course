def softuni_students(*student_information, **courses):

    def formatted_string(student_name, course):
        return f"*** A student with the username {student_name} has successfully finished the course {course}!"

    invalid_students = []
    valid_students_and_course = {}
    for course_id, name_of_student in student_information:
        if course_id in courses:
            valid_students_and_course[name_of_student] = courses[course_id]
        else:
            invalid_students.append(name_of_student)

    if len(invalid_students) > 0:
        invalid_students.sort()
        invalid_names = ", ".join([name for name in invalid_students])
        invalid_name_to_return = f"!!! Invalid course students: {invalid_names}"
        valid_students = '\n'.join(formatted_string(name, course) for name, course
                                   in sorted(valid_students_and_course.items(), key=lambda x: x[0]))
        text_to_return = valid_students + f"\n{invalid_name_to_return}"
    else:
        text_to_return = '\n'.join(formatted_string(name, course) for name, course
                                   in sorted(valid_students_and_course.items(), key=lambda x: x[0]))

    return text_to_return


print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
