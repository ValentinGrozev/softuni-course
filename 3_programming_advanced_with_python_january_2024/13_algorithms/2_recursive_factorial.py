def factorial(number):
    if number == 1:
        return number * 1
    else:
        return number * factorial(number - 1)


current_number = int(input())
print(factorial(current_number))
