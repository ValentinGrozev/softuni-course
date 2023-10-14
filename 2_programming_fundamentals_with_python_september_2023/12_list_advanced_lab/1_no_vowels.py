text = input()
list_with_vowels = ["a", "o", "u", "e", "i"]

new_text = (char for char in text if char.lower() not in list_with_vowels)
print("".join(new_text))