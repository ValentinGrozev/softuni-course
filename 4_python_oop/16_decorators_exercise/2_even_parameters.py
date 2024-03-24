def even_parameters(function):
    def wrapper(*args):
        numbers = list(args)
        for arg in numbers:
            if not isinstance(arg, int):
                return "Please use only even numbers!"

        even_arguments = all([number if number % 2 == 0 else False for number in numbers])
        if even_arguments:
            return function(*numbers)
        return "Please use only even numbers!"

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
