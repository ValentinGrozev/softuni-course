word = input()

word_case_insensitive = word.lower()
words_in_list_to_check = ["Sand".lower(), "Water".lower(), "Fish".lower(), "Sun".lower()]
counter = 0

for searched_word in words_in_list_to_check:
    counter += word_case_insensitive.count(searched_word)

print(counter)



