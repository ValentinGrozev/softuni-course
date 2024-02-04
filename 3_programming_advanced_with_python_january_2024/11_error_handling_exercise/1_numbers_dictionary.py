numbers_dictionary = {}

command = input()

while command != "Search":
    number_as_string = command

    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")

    command = input()

command = input()

while command != "Remove":
    searched_number = command

    try:
        print(numbers_dictionary[searched_number])
    except KeyError:
        print("Number does not exist in dictionary")

    command = input()

command = input()

while command != "End":
    searched_number = command

    try:
        del numbers_dictionary[searched_number]
    except KeyError:
        print("Number does not exist in dictionary")

    command = input()

print(numbers_dictionary)
