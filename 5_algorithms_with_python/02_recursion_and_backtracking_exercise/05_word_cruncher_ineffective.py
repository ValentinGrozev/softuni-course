from itertools import permutations


def find_words(parts, target_word, words):
    if parts:
        current_part = parts[0]
        if target_word.startswith(current_part):
            parts.remove(current_part)
            target_word = target_word[len(current_part):]
            words.append(current_part)
            if not target_word:
                return " ".join(words)
        else:
            parts.remove(current_part)

        return find_words(parts, target_word, words)


parts_of_word = input().split(", ")
target_string = input()
unique_words = set()

generate_permutations = permutations(parts_of_word)

for permutation in generate_permutations:
    for index in range(len(permutation)):
        unique_words.add(find_words(list(permutation[index:]), target_string, []))

for word in unique_words:
    if word:
        print(word)
