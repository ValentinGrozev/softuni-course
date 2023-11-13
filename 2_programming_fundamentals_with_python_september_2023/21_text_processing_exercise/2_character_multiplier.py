two_strings = input().split()
first_string = two_strings[0]
second_string = two_strings[1]

multiplied_sum = 0

for element_1, element_2 in zip(first_string, second_string):
    current_sum = ord(element_1) * ord(element_2)
    multiplied_sum += current_sum

if len(first_string) > len(second_string):
    difference = len(first_string) - len(second_string)
    counter = 0
    for element in first_string[::-1]:
        if counter == difference:
            break
        counter += 1
        multiplied_sum += ord(element)

elif len(second_string) > len(first_string):
    difference = len(second_string) - len(first_string)
    counter = 0
    for element in second_string[::-1]:
        if counter == difference:
            break
        counter += 1
        multiplied_sum += ord(element)

print(multiplied_sum)
