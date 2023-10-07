def all_the_characters_between(first, second):
    my_list = []
    for number in range(ord(first) + 1, ord(second)):
        my_list.append(chr(number))
    return my_list


first_character = input()
second_character = input()
print(" ".join(all_the_characters_between(first_character, second_character)))