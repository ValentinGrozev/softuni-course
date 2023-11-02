count_of_the_words = int(input())

dictionary = {}

for words in range(count_of_the_words):
    first_word = input()
    second_word = input()
    if first_word not in dictionary:
        dictionary[first_word] = []
    dictionary[first_word].append(second_word)


for word in dictionary:
    print(f"{word} - {', '.join(dictionary[word])}")
