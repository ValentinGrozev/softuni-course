def sorted_list(numbers):
    list_with_numbers = []
    for number in numbers:
        list_with_numbers.append(int(number))
    return sorted(list_with_numbers)


sequence_of_numbers = input().split()
print(sorted_list(sequence_of_numbers))