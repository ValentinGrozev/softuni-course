number_of_el_in_set_1, number_of_el_in_set_2 = [int(x) for x in input().split()]

first_set = set()
second_set = set()

for number in range(number_of_el_in_set_1):
    first_set.add(input())

for number in range(number_of_el_in_set_2):
    second_set.add(input())

unique_numbers = first_set.intersection(second_set)
print(*unique_numbers, sep='\n')
