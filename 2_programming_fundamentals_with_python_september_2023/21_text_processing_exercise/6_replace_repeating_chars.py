input_string = input()

new_word = ""
current_char = ""

for char in input_string:
    if char != current_char:
        new_word += char
        current_char = char

print(new_word)
