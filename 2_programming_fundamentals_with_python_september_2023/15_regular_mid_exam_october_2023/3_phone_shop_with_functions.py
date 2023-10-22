def add_phone(phone_model, list_with_phones):
    if phone_model not in list_with_phones:
        list_with_phones.append(phone_model)


def remove_phone(phone_model, list_with_phones):
    if phone_model in list_with_phones:
        list_with_phones.remove(phone_model)


def bonus_phone(phone_model, list_with_phones):
    final_phone_command = phone_model.split(":")
    old_phone_model = final_phone_command[0]
    new_phone_model = final_phone_command[1]
    if old_phone_model in list_with_phones:
        for phone_index in range(len(list_with_phones)):
            if old_phone_model == list_with_phones[phone_index]:
                list_with_phones.insert(phone_index + 1, new_phone_model)
                break


def last(phone_model, list_with_phones):
    if phone_model in list_with_phones:
        list_with_phones.remove(phone_model)
        list_with_phones.append(phone_model)


list_of_phones = input().split(", ")
command = input()

while command != "End":
    command = command.split(" - ")
    title = command[0]
    if title == "Add":
        add_phone(command[1], list_of_phones)
    elif title == "Remove":
        remove_phone(command[1], list_of_phones)
    elif title == "Bonus phone":
        bonus_phone(command[1], list_of_phones)
    elif title == "Last":
        last(command[1], list_of_phones)

    command = input()

print(", ".join(list_of_phones))
