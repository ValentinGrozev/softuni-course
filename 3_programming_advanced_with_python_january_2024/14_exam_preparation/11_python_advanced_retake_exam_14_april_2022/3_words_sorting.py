def words_sorting(*words):
    words_dictionary = {}

    for word in words:
        if word not in words_dictionary:
            words_dictionary[word] = 0
        current_word_sum = 0

        for symbol in word:
            current_word_sum += ord(symbol)
        words_dictionary[word] = current_word_sum

    values_sum = sum(words_dictionary.values())

    sorted_words_dictionary = sorted(words_dictionary.items(), key=lambda x: -x[1] if values_sum % 2 != 0 else x[0])

    result = ""

    for word, number in sorted_words_dictionary:
        result += f"{word} - {number}\n"

    return result


print(
    words_sorting(
        'cacophony',
        'accolade')
)
