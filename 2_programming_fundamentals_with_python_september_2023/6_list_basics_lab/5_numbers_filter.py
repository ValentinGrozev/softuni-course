count_of_numbers = int(input())

new_list = []
new_filtered_list = []

for numbers in range(count_of_numbers):
    number = int(input())
    new_list.append(number)

command = input()

if command == "even":
    for number in new_list:
        if number % 2 == 0:
            new_filtered_list.append(number)
elif command == "odd":
    for number in new_list:
        if number % 2 != 0:
            new_filtered_list.append(number)
elif command == "negative":
    for number in new_list:
        if number < 0:
            new_filtered_list.append(number)
elif command == "positive":
    for number in new_list:
        if number >= 0:
            new_filtered_list.append(number)

print(new_filtered_list)