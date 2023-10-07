def odd_and_even_sum(some_number):
    odd_sum = 0
    even_sum = 0
    for number in some_number:
        if int(number) % 2 == 0:
            even_sum += int(number)
        else:
            odd_sum += int(number)
    return odd_sum, even_sum


number_as_string = input()
sum_of_odds, sum_of_evens = odd_and_even_sum(number_as_string)
print(f"Odd sum = {sum_of_odds}, Even sum = {sum_of_evens}")