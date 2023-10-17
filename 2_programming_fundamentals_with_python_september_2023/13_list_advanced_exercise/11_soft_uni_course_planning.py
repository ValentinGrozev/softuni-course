schedule_of_lessons = input().split(", ")
lesson = input()

schedule_of_lessons = [el.strip() for el in schedule_of_lessons]

while lesson != "course start":
    current_lesson = lesson.split(":")
    if current_lesson[0] == "Add":
        if current_lesson[1] not in schedule_of_lessons:
            schedule_of_lessons.append(current_lesson[1])
    elif current_lesson[0] == "Insert":
        if current_lesson[1] not in schedule_of_lessons:
            index = int(current_lesson[2])
            schedule_of_lessons.insert(index, current_lesson[1])
    elif current_lesson[0] == "Remove":
        title_of_lesson = current_lesson[1]
        if title_of_lesson in schedule_of_lessons:
            if (title_of_lesson + "-Exercise") in schedule_of_lessons:
                schedule_of_lessons.remove(title_of_lesson + "-Exercise")
                schedule_of_lessons.remove(title_of_lesson)
            else:
                schedule_of_lessons.remove(title_of_lesson)
    elif current_lesson[0] == "Swap":
        title_of_first_lesson = current_lesson[1]
        title_of_second_lesson = current_lesson[2]
        if title_of_first_lesson and title_of_second_lesson in schedule_of_lessons:
            first_index = schedule_of_lessons.index(title_of_first_lesson, 0, len(schedule_of_lessons))
            second_index = schedule_of_lessons.index(title_of_second_lesson, 0, len(schedule_of_lessons))
            schedule_of_lessons[first_index], schedule_of_lessons[second_index] = \
                schedule_of_lessons[second_index], schedule_of_lessons[first_index]
            if (title_of_first_lesson + "-Exercise") in schedule_of_lessons:
                exercise = schedule_of_lessons.pop(first_index + 1)
                schedule_of_lessons.insert(second_index + 1, exercise)
            if (title_of_second_lesson + "-Exercise") in schedule_of_lessons:
                exercise = schedule_of_lessons.pop(second_index + 1)
                schedule_of_lessons.insert(first_index + 1, exercise)
    elif current_lesson[0] == "Exercise":
        if current_lesson[1] not in schedule_of_lessons:
            schedule_of_lessons.append(current_lesson[1])
            schedule_of_lessons.append(f"{current_lesson[1]}-Exercise")
        elif current_lesson[1] in schedule_of_lessons and f"{current_lesson[1]}-Exercise" not in schedule_of_lessons:
            index_of_current_lesson = schedule_of_lessons.index(current_lesson[1], 0, len(schedule_of_lessons))
            schedule_of_lessons.insert(index_of_current_lesson + 1, f"{current_lesson[1]}-Exercise")

    lesson = input()

number = 1
for every_lesson in schedule_of_lessons:
    print(f"{number}.{every_lesson}")
    number += 1
