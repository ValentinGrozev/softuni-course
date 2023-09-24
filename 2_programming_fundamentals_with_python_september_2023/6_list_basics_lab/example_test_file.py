#
# list_1 = [1, 2, 3, 4, 5, 7, 8, 12, 14, 0, 1, 5, 7, 8, 12, 111]
# print(len(list_1))
# print(list_1)
#
# list_2 = list_1[0:4]
# list_2.append(33)
# print(list_2)
#
# print(list_1 + list_2)
# list_1.extend(list_2)
# print(list_1)
#
# list_1.sort(reverse=True)
# print(list_1)
#
# for index in range(len(list_1)):
#     number = list_1[index]
#     print(index, number)
#
# # for index in range(len(list_2)):
# #     number = list_1[index]
# #     print(f"{number}-{index},", end=' ')
#
#
# fruits = ["apple", "banana", "cherry", "Alaabi", "kiwi", "mango", "Ananas"]
# fruits.sort()
# print(fruits)


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









