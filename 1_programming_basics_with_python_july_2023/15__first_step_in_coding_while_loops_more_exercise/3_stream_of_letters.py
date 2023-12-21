character = input()
key_word = ""
searched_word = ""
final_word = ""

while character != "End":
    if 65 <= ord(character) <= 90 or 97 <= ord(character) <= 122:
        if character == "n" or character == "o" or character == "c":
            if character not in key_word:
                key_word += character
            else:
                searched_word += character
        else:
            searched_word += character
        if "n" and "o" and "c" in key_word and len(key_word) == 3:
            final_word += searched_word + " "
            key_word = ""
            searched_word = ""
    else:
        pass

    character = input()

print(final_word)
