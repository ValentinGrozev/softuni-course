def calculator(operation: str, number_one: int, number_two: int) -> int:
    if operation == "multiply":
        return number_one * number_two
    elif operation == "divide":
        return int(number_one / number_two)
    elif operation == "add":
        return number_one + number_two
    elif operation == "subtract":
        return number_one - number_two


operator = input()
first_number = int(input())
second_number = int(input())
print(calculator(operator, first_number, second_number))