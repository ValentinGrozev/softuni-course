# First solution with list, for loop and enumerate:
expression = list(input())
parentheses_index = []

for index, parentheses in enumerate(expression):
    if parentheses == "(":
        parentheses_index.append(index)
    elif parentheses == ")":
        last_index = index + 1
        start_index = parentheses_index.pop()
        print("".join(expression[start_index:last_index]))


# Second solution with string and for loop:
expression = input()
parentheses_index = []

for index in range(len(expression)):
    if expression[index] == "(":
        parentheses_index.append(index)
    elif expression[index] == ")":
        last_index = index + 1
        start_index = parentheses_index.pop()
        print("".join(expression[start_index:last_index]))
