text = input()

current_sum = 0

for vowel in text:
    if vowel == "a":
        current_sum += 1
    elif vowel == "e":
        current_sum += 2
    elif vowel == "i":
        current_sum += 3
    elif vowel == "o":
        current_sum += 4
    elif vowel == "u":
        current_sum += 5
print(current_sum)

