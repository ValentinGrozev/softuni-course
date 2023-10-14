def final_list_and_palindromes(some_words, some_palindromes):
    counter = 0
    new_list = []

    for word in words:
        if palindrome in word:
            counter += 1
        if word == word[::-1]:
            new_list.append(word)
    return f"{new_list}\nFound palindrome {counter} times"


words = input().split()
palindrome = input()

print(final_list_and_palindromes(words, palindrome))
