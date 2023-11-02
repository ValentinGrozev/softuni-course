list_of_characters = input().split(", ")

dictionary = {}

for element in range(0, len(list_of_characters)):
    key = list_of_characters[element]
    value = ord(key)
    dictionary[key] = value

print(dictionary)
