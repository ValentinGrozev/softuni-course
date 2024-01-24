def multiply(*args):
    total_sum = 1
    for number in args:
        total_sum *= number
    return total_sum


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))
