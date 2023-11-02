list_of_characters = input().split(", ")

dictionary = {element: ord(element) for element in list_of_characters}
print(dictionary)