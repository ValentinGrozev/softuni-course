def even_numbers_index(numbers):
    list_with_index = []
    for index, number in enumerate(numbers):
        if int(number) % 2 == 0:
            list_with_index.append(index)
    return list_with_index


list_with_numbers = input().split(", ")

print(even_numbers_index(list_with_numbers))