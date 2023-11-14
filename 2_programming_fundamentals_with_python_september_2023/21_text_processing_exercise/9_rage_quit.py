string_number_pairs = input()

string_to_multiply = ""
multiply_digit = ""
final_string = ""

for index in range(len(string_number_pairs)):
    if not string_number_pairs[index].isdigit():
        string_to_multiply += string_number_pairs[index]
    else:
        for number in range(index, len(string_number_pairs)):
            if not string_number_pairs[number].isdigit():
                break
            multiply_digit += string_number_pairs[number]
        final_string += string_to_multiply * int(multiply_digit)
        string_to_multiply = ""
        multiply_digit = ""

unique_symbol_used = len(set(final_string.upper()))
print(f"Unique symbols used: {unique_symbol_used}")
print(final_string.upper())
