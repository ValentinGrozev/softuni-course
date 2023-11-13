word = input()
reversed_word = ""

while word != "end":
    for char in word[-1::-1]:
        reversed_word += str(char)
    print(f"{word} = {reversed_word}")
    reversed_word = ""

    word = input()


# second solution
# word = input()
# reversed_word = ""
#
# while word != "end":
#     for char in reversed(word):
#         reversed_word += char
#     print(f"{word} = {reversed_word}")
#     reversed_word = ""
#
#     word = input()


# # third solution
# word = input()
#
# while word != "end":
#     reversed_word = word[::-1]
#     print(f"{word} = {reversed_word}")
#     reversed_word = ""
#
#     word = input()
