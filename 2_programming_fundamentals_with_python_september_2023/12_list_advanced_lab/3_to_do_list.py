def list_with_tasks():
    to_do_notes = input().split("-")
    tasks_list = []

    while True:
        if to_do_notes[0] != "End":
            to_do_notes[0] = int(to_do_notes[0])
            tasks_list.append(to_do_notes)
        else:
            break

        to_do_notes = input().split("-")
    tasks_list.sort()

    new_list = []
    for task in tasks_list:
        task_needed = task[1]
        new_list.append(task_needed)

    return new_list


print(list_with_tasks())
