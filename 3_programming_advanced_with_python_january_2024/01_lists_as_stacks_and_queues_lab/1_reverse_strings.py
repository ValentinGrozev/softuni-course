text = list(input())
reversed_text = []

for index in range(len(text)):
    removed_char = text.pop()
    reversed_text.append(removed_char)

print(''.join(reversed_text))
