def factorial_division(first, second):
    first_factorial = 1
    second_factorial = 1
    for number in range(1, first + 1):
        first_factorial *= number
    for number in range(1, second + 1):
        second_factorial *= number
    return first_factorial / second_factorial


first_number = int(input())
second_number = int(input())
print(f"{factorial_division(first_number, second_number):.2f}")
