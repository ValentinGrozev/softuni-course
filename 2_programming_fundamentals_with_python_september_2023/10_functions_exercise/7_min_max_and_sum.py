def min_max_and_sum(some_numbers):
    list_with_integers = []
    for number in some_numbers:
        list_with_integers.append(int(number))
    return list_with_integers


sequence_of_numbers = input().split()
minimum_number = min(min_max_and_sum(sequence_of_numbers))
maximum_number = max(min_max_and_sum(sequence_of_numbers))
sum_of_all_numbers = sum(min_max_and_sum(sequence_of_numbers))
print(f"The minimum number is {minimum_number}\n"
      f"The maximum number is {maximum_number}\n"
      f"The sum number is: {sum_of_all_numbers}")
