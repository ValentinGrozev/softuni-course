word_one = input()
word_two = input()

new_word = ''

used_word = ''

differance = abs(len(word_two) - len(word_one))

if len(word_one) > len(word_two):
    used_word = word_two
    last_characters = word_one[-differance:]
else:
    used_word = word_one
    last_characters = word_two[-differance:]

for index in range(0, len(used_word)):
    character_1 = word_one[index]
    character_2 = word_two[index]
    if index % 2 == 0:
        new_word += character_1
    else:
        new_word += character_2

print(new_word+last_characters)