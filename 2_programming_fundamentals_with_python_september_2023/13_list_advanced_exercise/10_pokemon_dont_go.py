sequence_of_integers = input().split()
sequence_of_integers = [int(number) for number in sequence_of_integers]

sum_of_removed_elements = 0

while len(sequence_of_integers) > 0:
    input_index = int(input())
    if input_index >= len(sequence_of_integers):
        sum_of_removed_elements += (sequence_of_integers[-1])
        number = sequence_of_integers.pop()
        sequence_of_integers.append(sequence_of_integers[0])
        for current_index, current_number in enumerate(sequence_of_integers):
            if number >= current_number:
                sequence_of_integers[current_index] = number + current_number
            else:
                sequence_of_integers[current_index] = current_number - number

    elif input_index < 0:
        sum_of_removed_elements += sequence_of_integers[0]
        number = sequence_of_integers[0]
        sequence_of_integers[0] = sequence_of_integers[-1]
        for current_index, current_number in enumerate(sequence_of_integers):
            if number >= current_number:
                sequence_of_integers[current_index] = number + current_number
            else:
                sequence_of_integers[current_index] = current_number - number

    else:
        sum_of_removed_elements += sequence_of_integers[input_index]
        number = sequence_of_integers.pop(input_index)
        for current_index, current_number in enumerate(sequence_of_integers):
            if number >= current_number:
                sequence_of_integers[current_index] = number + current_number
            else:
                sequence_of_integers[current_index] = current_number - number

print(sum_of_removed_elements)
