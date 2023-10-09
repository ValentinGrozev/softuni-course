sequence_of_numbers = input().split()
text = input()
numbers_sum = 0
searched_char = []

for index in range(len(sequence_of_numbers)):
    numbers_group = sequence_of_numbers[index]
    for number_index in range(len(numbers_group)):
        current_number = numbers_group[number_index]
        numbers_sum += int(current_number)
    for message in range(len(text)):
        if len(text) > numbers_sum:
            char_from_message = text[numbers_sum]
            searched_char.append(char_from_message)
            text = text.replace(char_from_message, '', 1)
            break
        else:
            char_from_message = text[abs(numbers_sum-len(text))]
            searched_char.append(char_from_message)
            text = text.replace(char_from_message, '', 1)
            break
    numbers_sum = 0

print("".join(searched_char))
