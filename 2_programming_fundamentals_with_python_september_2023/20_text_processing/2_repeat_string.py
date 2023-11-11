sequence_of_strings = input().split()
final_word = ""

for word in range(len(sequence_of_strings)):
    multiply = len(sequence_of_strings[word])
    final_word += sequence_of_strings[word] * multiply

print(final_word)
