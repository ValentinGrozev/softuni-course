first_word = input()
second_word = input()

for char_idx in range(len(first_word)):
    if second_word[char_idx] == first_word[char_idx]:
        continue
    first_word = first_word[:char_idx] + second_word[char_idx] + first_word[char_idx + 1:]
    print(first_word)