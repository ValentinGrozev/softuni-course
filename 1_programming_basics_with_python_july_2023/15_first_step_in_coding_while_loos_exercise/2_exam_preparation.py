bad_grades = int(input())
name_of_task = input()

total_grades = 0
number_of_tasks_done = 0
last_problem = ""
bad_grades_got = 0

while True:
    if name_of_task != "Enough":
        grade = int(input())
        if grade <= 4:
            bad_grades_got += 1

        total_grades += grade
        number_of_tasks_done += 1
        last_problem = name_of_task

        if bad_grades == bad_grades_got:
            break
    else:
        break

    name_of_task = input()

average_score = total_grades / number_of_tasks_done

if bad_grades_got < bad_grades:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {number_of_tasks_done}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {bad_grades_got} poor grades.")
