rows = int(input())

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

diagonal_sum = 0

for row_index in range(rows):
    for column_index in range(len(matrix[row_index])):
        if row_index == column_index:
            diagonal_sum += matrix[row_index][column_index]

print(diagonal_sum)
