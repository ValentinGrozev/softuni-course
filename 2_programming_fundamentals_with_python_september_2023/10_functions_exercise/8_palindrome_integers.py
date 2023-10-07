def is_palindrome(some_numbers):
    return some_numbers == some_numbers[::-1]


numbers_as_string = input().split(", ")
for numbers_as_string in numbers_as_string:
    if is_palindrome(numbers_as_string):
        print(is_palindrome(numbers_as_string))
    else:
        print(is_palindrome(numbers_as_string))