word = input()

my_list = []

for index, character in enumerate(word):
    if character.isupper():
        my_list.append(index)

print(my_list)