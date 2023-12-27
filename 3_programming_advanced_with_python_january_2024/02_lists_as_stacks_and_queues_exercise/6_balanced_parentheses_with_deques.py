from collections import deque

sequence_of_parentheses = deque(input())
parentheses = {"{": "}", "(": ")", "[": "]"}
opening_parentheses = "({["
closing_parentheses = ")}]"
rotates = 0
counter_for_back_rotates = 0

while sequence_of_parentheses:
    if sequence_of_parentheses[0] in closing_parentheses:
        print("NO")
        break
    elif rotates == (len(sequence_of_parentheses) / 2):
        print("NO")
        break
    elif sequence_of_parentheses[0] in opening_parentheses:
        symbol_for_second_parentheses = parentheses[sequence_of_parentheses[0]]
        if sequence_of_parentheses[1] == symbol_for_second_parentheses:
            sequence_of_parentheses.popleft()
            sequence_of_parentheses.popleft()
            sequence_of_parentheses.rotate(counter_for_back_rotates)
            rotates = 0
            counter_for_back_rotates = 0
        else:
            sequence_of_parentheses.rotate(-1)
            rotates += 1
            counter_for_back_rotates += 1


if not sequence_of_parentheses:
    print("YES")
