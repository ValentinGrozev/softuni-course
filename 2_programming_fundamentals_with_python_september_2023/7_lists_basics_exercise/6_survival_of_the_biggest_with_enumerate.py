import sys

list_of_numbers = input().split()
numbers_to_remove = int(input())

list_of_int_numbers = []
final_list = []
smallest_number = sys.maxsize
smallest_index = 0
numbers_to_delete = 0

for number in range(len(list_of_numbers)):
    list_of_int_numbers.append(int(list_of_numbers[number]))

while numbers_to_delete < numbers_to_remove:
    for current_index, current_number in enumerate(list_of_int_numbers):
        if current_number < smallest_number:
            smallest_number = current_number
            smallest_index = current_index
    list_of_int_numbers.pop(smallest_index)
    numbers_to_delete += 1
    smallest_number = sys.maxsize
    smallest_index = 0

for elements in range(len(list_of_int_numbers)):
    element = str(list_of_int_numbers[elements])
    final_list.append(element)

print(", ".join(final_list))
