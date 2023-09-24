number_of_lines = int(input())

chars_sum = 0

for chars in range(number_of_lines):
    input_char = input()
    chars_sum += ord(input_char)

print(f"The sum equals: {chars_sum}")

