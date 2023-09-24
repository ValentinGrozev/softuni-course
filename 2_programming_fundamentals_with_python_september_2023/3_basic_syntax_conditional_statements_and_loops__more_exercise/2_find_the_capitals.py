word = input()

my_list = []

for index in range(0, len(word)):
    character = word[index]
    if character.isupper():
        my_list.append(index)

print(my_list)

