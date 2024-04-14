def get_fibonacci_iterative(n):
    number_one = 1
    number_two = 1
    result = 0
    for _ in range(n - 1):
        result = number_one + number_two
        number_one, number_two = number_two, result
    return result


first_n = int(input())
print(get_fibonacci_iterative(first_n))


def get_fibonacci_with_recursion(n):
    if n <= 1:
        return 1
    return get_fibonacci_with_recursion(n - 1) + get_fibonacci_with_recursion(n - 2)


second_n = int(input())
print(get_fibonacci_with_recursion(second_n))
