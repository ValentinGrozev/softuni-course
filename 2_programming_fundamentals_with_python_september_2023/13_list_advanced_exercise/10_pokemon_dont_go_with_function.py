sequence_of_integers = input().split()
sequence_of_integers = [int(el) for el in sequence_of_integers]

sum_of_removed_elements = 0


def update_list(to_update, remove_value):
    for idx, el in enumerate(to_update):
        if remove_value >= el:
            to_update[idx] = remove_value + el
        else:
            to_update[idx] = el - remove_value


while len(sequence_of_integers) > 0:
    index = int(input())

    if index < 0:
        to_remove_value = sequence_of_integers[0]
        sequence_of_integers[0] = sequence_of_integers[-1]
    elif index >= len(sequence_of_integers):
        to_remove_value = sequence_of_integers[-1]
        sequence_of_integers[-1] = sequence_of_integers[0]
    else:
        to_remove_value = int(sequence_of_integers[index])
        sequence_of_integers.pop(index)

    sum_of_removed_elements += to_remove_value
    update_list(sequence_of_integers, to_remove_value)

print(sum_of_removed_elements)