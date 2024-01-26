def even_odd(*args):
    command = args[-1]
    list_with_numbers = []
    if command == "even":
        list_with_numbers.append([num for num in args[:-1] if num % 2 == 0])
    else:
        list_with_numbers.append([num for num in args[:-1] if num % 2 != 0])
    return list_with_numbers[0]


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
