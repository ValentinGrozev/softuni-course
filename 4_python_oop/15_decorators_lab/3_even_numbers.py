def even_numbers(function):
    def wrapper(numbers):
        result = function(numbers)
        even_numbers_result = [number for number in result if number % 2 == 0]
        return function(even_numbers_result)

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
