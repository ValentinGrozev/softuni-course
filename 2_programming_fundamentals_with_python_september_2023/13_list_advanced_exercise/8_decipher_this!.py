def count_numbers_at_start(string):
    length = 0
    for every_symbol in string:
        if every_symbol.isdigit():
            length += 1
        else:
            break
    return length


def replace_digits_with_letter(word):
    digits = word[:count_numbers_at_start(word)]
    text = word[count_numbers_at_start(word):]
    return chr(int(digits)) + text


def swap_second_and_last_index(word):
    if len(word) > 2:
        return word[0] + word[-1] + word[2:-1] + word[1]
    else:
        return word


message_to_decipher = input().split()

final_list = []
for current_word in message_to_decipher:
    transformed_word = replace_digits_with_letter(current_word)
    final_word = swap_second_and_last_index(transformed_word)
    final_list.append(final_word)

print(' '.join(final_list))
