list_with_numbers = input().split()
command = input().split()

list_with_integer_numbers = [int(number) for number in list_with_numbers]

while command[0] != "end":
    if command[0] == "swap":
        first_number_index = int(command[1])
        second_number_index = int(command[2])
        for index in range(len(list_with_integer_numbers)):
            first_number = list_with_integer_numbers[first_number_index]
            second_number = list_with_integer_numbers[second_number_index]
        list_with_integer_numbers[first_number_index], list_with_integer_numbers[second_number_index] = \
            list_with_integer_numbers[second_number_index], list_with_integer_numbers[first_number_index]
    if command[0] == "multiply":
        first_number_index = int(command[1])
        second_number_index = int(command[2])
        first_number = 0
        second_number = 0
        for index in range(len(list_with_integer_numbers)):
            first_number = list_with_integer_numbers[first_number_index]
            second_number = list_with_integer_numbers[second_number_index]
            break
        multiply_first_element = first_number * second_number
        for element in list_with_integer_numbers:
            first_number = list_with_integer_numbers[first_number_index]
            list_with_integer_numbers.insert(first_number_index, multiply_first_element)
            list_with_integer_numbers.pop(first_number_index + 1)
            break
    if command[0] == "decrease":
        for index, number in enumerate(list_with_integer_numbers):
            number = number - 1
            list_with_integer_numbers.insert(index, number)
            list_with_integer_numbers.pop(index + 1)

    command = input().split()

final_list = [str(number) for number in list_with_integer_numbers]
print(', '.join(final_list))
