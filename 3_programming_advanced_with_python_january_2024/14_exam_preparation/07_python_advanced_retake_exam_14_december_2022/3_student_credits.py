def students_credits(*course_information):
    courses_and_credits = {}

    for course_info in course_information:
        course_name, max_credits, max_points, student_points = course_info.split("-")
        student_earned_credits = f"{((int(student_points) / int(max_points)) * int(max_credits))}"
        courses_and_credits[course_name] = float(student_earned_credits)

    result = ""

    if sum(courses_and_credits.values()) >= 240:
        result += f"Diyan gets a diploma with {sum(courses_and_credits.values()):.1f} credits.\n"
    else:
        result += f"Diyan needs {(240 - sum(courses_and_credits.values())):.1f} credits more for a diploma.\n"

    sorted_courses_and_credits = sorted(courses_and_credits.items(), key=lambda x: -x[1])

    for course, course_credits in sorted_courses_and_credits:
        result += f"{course} - {course_credits:.1f}\n"

    return result


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
