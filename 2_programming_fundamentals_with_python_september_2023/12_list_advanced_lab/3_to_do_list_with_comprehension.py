def list_with_tasks():
    to_do_notes = input().split("-")
    tasks_list = []

    while True:
        if to_do_notes[0] == "End":
            break
        else:
            to_do_notes[0] = int(to_do_notes[0])
            tasks_list.append(to_do_notes)

        to_do_notes = input().split("-")
        tasks_list.sort()

    return list(task[1] for task in tasks_list)


print(list_with_tasks())
