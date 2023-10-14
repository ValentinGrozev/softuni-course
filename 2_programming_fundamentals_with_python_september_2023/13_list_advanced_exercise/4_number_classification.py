def checked_numbers(numbers):
    positive_numbers = []
    negative_numbers = []
    even_numbers = []
    odd_numbers = []
    for number in numbers:
        if int(number) >= 0:
            positive_numbers.append(number)
            if int(number) % 2 == 0:
                even_numbers.append(number)
            else:
                odd_numbers.append(number)
        else:
            negative_numbers.append(number)
            if int(number) % 2 == 0:
                even_numbers.append(number)
            else:
                odd_numbers.append(number)
    return f"Positive: {', '.join(positive_numbers)}\nNegative: {', '.join(negative_numbers)}\nEven: {', '.join(even_numbers)}" \
           f"\nOdd: {', '.join(odd_numbers)}"


list_of_numbers = input().split(", ")
print(checked_numbers(list_of_numbers))
