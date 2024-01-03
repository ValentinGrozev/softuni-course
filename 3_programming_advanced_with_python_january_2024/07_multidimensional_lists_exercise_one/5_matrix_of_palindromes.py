rows, cols = [int(x) for x in input().split()]

matrix = []

for row in range(rows):
    matrix.append([])
    for col in range(cols):
        matrix[row].append(chr(97 + row) + chr(97 + row + col) + chr(97 + row))

for current_row in matrix:
    print(*current_row)
