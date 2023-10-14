def containing_substrings(first, second):
    substring_list = []
    for current_word_in_first_sequences_of_words in first:
        for current_word_in_second_sequences_of_words in second:
            if current_word_in_first_sequences_of_words in current_word_in_second_sequences_of_words:
                substring_list.append(current_word_in_first_sequences_of_words)
                break

    return substring_list


first_sequences_of_words = input().split(", ")
second_sequences_of_words = input().split(", ")
print(containing_substrings(first_sequences_of_words, second_sequences_of_words))
