random_numbers = input().split()
command = input()

random_numbers_as_integers = [int(number) for number in random_numbers]

while command != "Finish":
    command = command.split()
    title = command[0]
    if title == "Add":
        number = int(command[1])
        random_numbers_as_integers.append(number)
    elif title == "Remove":
        number = int(command[1])
        if number in random_numbers_as_integers:
            random_numbers_as_integers.remove(number)
    elif title == "Replace":
        number_to_replace = int(command[1])
        new_number = int(command[2])
        if number_to_replace in random_numbers_as_integers:
            for index in range(len(random_numbers_as_integers)):
                if random_numbers_as_integers[index] == number_to_replace:
                    random_numbers_as_integers[index] = new_number
                    break
    elif title == "Collapse":
        number = int(command[1])
        random_numbers_as_integers = [element for element in random_numbers_as_integers if element >= number]

    command = input()

random_list_as_str = [str(number) for number in random_numbers_as_integers]
print(" ".join(random_list_as_str))
