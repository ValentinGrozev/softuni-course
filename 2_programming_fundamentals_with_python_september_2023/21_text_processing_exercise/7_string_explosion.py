input_string = input()

explosion_strength = 0

new_string = ""

for char_index in range(len(input_string)):
    if explosion_strength > 0 and input_string[char_index] != ">":
        explosion_strength -= 1
    elif input_string[char_index] == ">":
        explosion_strength += int(input_string[char_index + 1])
        new_string += input_string[char_index]
    elif input_string[char_index].isalpha():
        new_string += input_string[char_index]

print(new_string)
