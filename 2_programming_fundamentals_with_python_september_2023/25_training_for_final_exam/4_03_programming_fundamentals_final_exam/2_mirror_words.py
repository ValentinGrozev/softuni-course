import re

text_string = input()
pattern = r"([@|#])([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})(\1)"
matches = re.findall(pattern, text_string)
if matches:
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")

mirror_words = []

for match in matches:
    first_word = match[1]
    second_word = match[3]
    reversed_word = second_word[::-1]
    if first_word == reversed_word:
        mirror_words.append(f"{first_word} <=> {second_word}")

if len(mirror_words) > 0:
    print("The mirror words are:")
    print(", ".join(mirror_words))
else:
    print("No mirror words!")
