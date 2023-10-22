def add(number, list_with_integers):
    list_with_integers.append(number)


def remove(number, list_with_integers):
    if number in random_numbers_as_integers:
        list_with_integers.remove(number)


def replace(number_to_replace, new_number, list_with_integers):
    if number_to_replace in list_with_integers:
        for index in range(len(list_with_integers)):
            if list_with_integers[index] == number_to_replace:
                list_with_integers[index] = new_number
                break


def collapse(number, list_with_integers):
    return [element for element in list_with_integers if element >= number]


random_numbers = input().split()
command = input()

random_numbers_as_integers = [int(number) for number in random_numbers]

while command != "Finish":
    command = command.split()
    title = command[0]
    if title == "Add":
        add(int(command[1]), random_numbers_as_integers)
    elif title == "Remove":
        remove(int(command[1]), random_numbers_as_integers)
    elif title == "Replace":
        replace(int(command[1]), int(command[2]), random_numbers_as_integers)
    elif title == "Collapse":
        random_numbers_as_integers = collapse(int(command[1]), random_numbers_as_integers)

    command = input()

random_list_as_str = [str(number) for number in random_numbers_as_integers]
print(" ".join(random_list_as_str))
