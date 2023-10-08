def perfect_number(some_number):
    sum_of_all_divisors = 0
    for current_number in range(1, some_number):
        if some_number % current_number == 0:
            sum_of_all_divisors += current_number
    if sum_of_all_divisors == some_number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(perfect_number(number))
