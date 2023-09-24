first_letter_from_range = input()
last_letter_from_range = input()
letter_to_skip = input()

first_letter_in_ascii = ord(first_letter_from_range)
last_letter_in_ascii = ord(last_letter_from_range)
letter_to_skip_in_ascii = ord(letter_to_skip)

number_count = 0
for number_1 in range(first_letter_in_ascii, last_letter_in_ascii + 1):
    for number_2 in range(first_letter_in_ascii, last_letter_in_ascii + 1):
        for number_3 in range(first_letter_in_ascii, last_letter_in_ascii + 1):
            while number_1 != letter_to_skip_in_ascii and number_2 != letter_to_skip_in_ascii and number_3 != letter_to_skip_in_ascii:
                number_count += 1
                print(f"{chr(number_1)}{chr(number_2)}{chr(number_3)}", end=' ')
                break
print(f"{number_count}", end=' ')