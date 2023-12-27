parentheses = list()

opening = {"}": "{", ")": "(", "]": "["}
balanced = True

text = input()
for char in text:
    if char in ["(", "[", "{"]:
        parentheses.append(char)
    else:
        if parentheses:
            if parentheses[-1] == opening[char]:
                parentheses.pop()
            else:
                balanced = False
        else:
            balanced = False
            break

if balanced and len(parentheses) == 0:
    print("YES")
else:
    print("NO")
