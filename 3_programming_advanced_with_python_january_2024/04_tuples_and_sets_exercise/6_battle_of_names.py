number_of_names = int(input())

odd_sum_set = set()
even_sum_set = set()
current_row = 1

for i in range(number_of_names):  # here range could be (1, number_of_names +1).
    name = input()
    sum_name = int(sum([ord(char) for char in name]) / current_row)  # If we change range here should be divided to "i".
    current_row += 1   # If we change range to (1, number_of_names +1) this won't be needed
    if sum_name % 2 == 0:
        even_sum_set.add(sum_name)
    else:
        odd_sum_set.add(sum_name)

if sum(odd_sum_set) == sum(even_sum_set):
    result = odd_sum_set.union(even_sum_set)
elif sum(odd_sum_set) > sum(even_sum_set):
    result = odd_sum_set.difference(even_sum_set)
else:
    result = odd_sum_set.symmetric_difference(even_sum_set)

print(", ".join(str(x) for x in result))
