input_string = input()

new_list = input_string.split()
opposite_list = []

for index in range(len(new_list)):
    number = new_list[index]
    opposite_number = -int(number)
    opposite_list.append(opposite_number)

print(opposite_list)

