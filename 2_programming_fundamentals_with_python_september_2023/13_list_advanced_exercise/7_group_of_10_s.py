sequence_of_numbers = input().split(", ")
sequence_of_int_numbers = []

for index in range(len(sequence_of_numbers)):
    number_as_int = int(sequence_of_numbers[index])
    sequence_of_int_numbers.append(number_as_int)

current_group = 10

while sequence_of_int_numbers:
    filtered_numbers = ([number for number in sequence_of_int_numbers if number <= current_group])
    print(f"Group of {current_group}'s: {filtered_numbers}")
    current_group += 10
    sequence_of_int_numbers = ([number for number in sequence_of_int_numbers if number not in filtered_numbers])

#     Second solution
#
# sequence_of_numbers = input().split(", ")
# sequence_of_int_numbers = []
#
# for index in range(len(sequence_of_numbers)):
#     number_as_int = int(sequence_of_numbers[index])
#     sequence_of_int_numbers.append(number_as_int)
#
# current_group = 10
#
# while sequence_of_int_numbers:
#     filtered_numbers = ([number for number in sequence_of_int_numbers if number <= current_group])
#     print(f"Group of {current_group}'s: {filtered_numbers}")
#     current_group += 10
#     for number in filtered_numbers:
#         for numbers in sequence_of_int_numbers:
#             if number == numbers:
#                 sequence_of_int_numbers.remove(numbers)
