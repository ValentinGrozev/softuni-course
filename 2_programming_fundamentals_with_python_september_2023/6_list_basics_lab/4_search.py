number_of_strings = int(input())
special_word = input()
my_list_1 = []
my_list_2 = []

for all_strings in range(number_of_strings):
    current_string = input()
    my_list_1.append(current_string)

for word in my_list_1:
    if special_word in word:
        my_list_2.append(word)

print(my_list_1)
print(my_list_2)
