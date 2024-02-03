def gather_credits(needed_credits, *course_info):
    courses_and_credits = {}

    for course, course_credits in course_info:
        if sum(courses_and_credits.values()) < needed_credits:
            if course not in courses_and_credits:
                courses_and_credits[course] = course_credits
        else:
            break

    if sum(courses_and_credits.values()) >= needed_credits:
        return (f"Enrollment finished! Maximum credits: {sum(courses_and_credits.values())}.\n"
                f"Courses: {', '.join(sorted(courses_and_credits.keys()))}")

    else:
        return (f"You need to enroll in more courses! You have to gather "
                f"{needed_credits - sum(courses_and_credits.values())} credits more.")


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
