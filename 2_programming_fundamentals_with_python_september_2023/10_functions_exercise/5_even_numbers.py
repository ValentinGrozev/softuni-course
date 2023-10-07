def even_numbers(numbers):
    list_with_even_numbers = []
    for number in numbers:
        if int(number) % 2 == 0:
            list_with_even_numbers.append(int(number))
    return list_with_even_numbers


sequence_of_numbers = input().split()
print(even_numbers(sequence_of_numbers))