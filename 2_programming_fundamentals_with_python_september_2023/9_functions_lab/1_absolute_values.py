numbers_list = input().split()
list_with_absolute_values = []

for number in numbers_list:
    list_with_absolute_values.append(abs(float(number)))

print(list_with_absolute_values)