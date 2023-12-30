from collections import deque


def addition(numbers, first_number, second_number):
    numbers.appendleft(first_number + second_number)
    return numbers


def multiply(numbers, first_number, second_number):
    numbers.appendleft(first_number * second_number)
    return numbers


def subtraction(numbers, first_number, second_number):
    numbers.appendleft(first_number - second_number)
    return numbers


def division(numbers, first_number, second_number):
    numbers.appendleft(first_number // second_number)
    return numbers


def main():
    expression = input().split()
    operators = ["*", "+", "-", "/"]
    numbers = deque()

    for char in expression:
        if char not in operators:
            numbers.append(int(char))
        else:
            while len(numbers) > 1:
                first_number = numbers.popleft()
                second_number = numbers.popleft()
                if char == "*":
                    multiply(numbers, first_number, second_number)
                elif char == "+":
                    addition(numbers, first_number, second_number)
                elif char == "-":
                    subtraction(numbers, first_number, second_number)
                elif char == "/":
                    division(numbers, first_number, second_number)

    print(''.join(str(x) for x in numbers))


main()
