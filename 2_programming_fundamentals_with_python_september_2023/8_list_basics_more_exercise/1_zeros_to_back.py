input_numbers = input()

input_list = input_numbers.split(", ")
int_list = []
zero_list = []
new_list = len(input_list) * [0]

for text in range(0, len(input_list)):
    new_list[text] = int(input_list[text])
    int_list.append(new_list[text])
for number in int_list:
    if number == 0 and number in int_list:
        zero_list.append(number)
        new_list.remove(number)
for index, number in enumerate(zero_list):
    new_list.append((zero_list[number]))
print(new_list)
