def positive_numbers(numbers):
    return ', '.join(number for number in numbers if int(number) >= 0)


def negative_numbers(numbers):
    return ', '.join(number for number in numbers if int(number) < 0)


def even_numbers(numbers):
    return ', '.join(number for number in numbers if int(number) % 2 == 0)


def odd_numbers(numbers):
    return ', '.join(number for number in numbers if int(number) % 2 != 0)


list_of_numbers = input().split(", ")
print(f"Positive: {positive_numbers(list_of_numbers)}")
print(f"Negative: {negative_numbers(list_of_numbers)}")
print(f"Even: {even_numbers(list_of_numbers)}")
print(f"Odd: {odd_numbers(list_of_numbers)}")