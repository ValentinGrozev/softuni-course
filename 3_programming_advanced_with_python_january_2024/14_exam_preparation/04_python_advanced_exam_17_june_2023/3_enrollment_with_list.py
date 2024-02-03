def gather_credits(needed_credits, *course_info):
    courses = []
    credits_got = 0

    for course, course_credits in course_info:
        if course not in courses:
            if credits_got < needed_credits:
                courses.append(course)
                credits_got += course_credits
            else:
                break

    if credits_got >= needed_credits:
        return (f"Enrollment finished! Maximum credits: {credits_got}.\n"
                f"Courses: {', '.join(sorted(courses))}")

    else:
        return (f"You need to enroll in more courses! You have to gather "
                f"{needed_credits - credits_got} credits more.")


print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
