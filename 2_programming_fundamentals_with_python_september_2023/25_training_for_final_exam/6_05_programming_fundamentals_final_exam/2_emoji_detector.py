import re

piece_of_string = input()

pattern_for_threshold = r"\d"
match_for_threshold = re.findall(pattern_for_threshold, piece_of_string)
sum_of_threshold = 1
for match in range(len(match_for_threshold)):
    number = int(match_for_threshold[match])
    sum_of_threshold *= number

pattern_for_valid_emojis = r"([:]{2}|[*]{2})([A-Z]{1}[a-z]{2,})(\1)"
match_for_valid_emojis = re.findall(pattern_for_valid_emojis, piece_of_string)

cool_emojis = []
for emoji in match_for_valid_emojis:
    coolness = 0
    for letter in emoji[1]:
        coolness += ord(letter)
    if coolness > sum_of_threshold:
        cool_emojis.append(emoji)

print(f"Cool threshold: {sum_of_threshold}")
print(f"{len(match_for_valid_emojis)} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(''.join(emoji))
