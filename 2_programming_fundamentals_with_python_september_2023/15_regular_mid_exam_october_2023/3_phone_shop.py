list_of_phones = input().split(", ")
command = input()

while command != "End":
    command = command.split(" - ")
    title = command[0]
    if title == "Add":
        phone_model = command[1]
        if phone_model not in list_of_phones:
            list_of_phones.append(phone_model)
    elif title == "Remove":
        phone_model = command[1]
        if phone_model in list_of_phones:
            list_of_phones.remove(phone_model)
    elif title == "Bonus phone":
        phones = command[1]
        final_phone_command = phones.split(":")
        old_phone_model = final_phone_command[0]
        new_phone_model = final_phone_command[1]
        if old_phone_model in list_of_phones:
            for phone_index in range(len(list_of_phones)):
                if old_phone_model == list_of_phones[phone_index]:
                    list_of_phones.insert(phone_index + 1, new_phone_model)
                    break
    elif title == "Last":
        phone_model = command[1]
        if phone_model in list_of_phones:
            list_of_phones.remove(phone_model)
            list_of_phones.append(phone_model)

    command = input()

print(", ".join(list_of_phones))
