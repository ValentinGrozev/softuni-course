from collections import deque

rows, columns = [int(x) for x in input().split()]
text = deque(input())

matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(columns):
        if row % 2 == 0:
            matrix[row].append(text[0])
        else:
            matrix[row].append(text[0])
        text.rotate(-1)
    if row % 2 != 0:
        matrix[row].reverse()

for current_row in matrix:
    print(*current_row, sep="")


# Second solution:
#
# from collections import deque
#
# rows, columns = [int(x) for x in input().split()]
# text = deque(input())
#
# matrix = []
#
# for row in range(rows):
#     matrix.append([""] * columns)
#     for col in range(columns):
#         if row % 2 == 0:
#             matrix[row][col] = text[0]
#         else:
#             matrix[row][columns - col - 1] = text[0]
#         text.rotate(-1)
#
# for current_row in matrix:
#     print(*current_row, sep="")
