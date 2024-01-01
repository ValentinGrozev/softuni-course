rows, columns = [int(x) for x in input().split(', ')]

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split()])

for column_index in range(columns):
    sum_of_column = 0
    for row_index in range(rows):
        sum_of_column += matrix[row_index][column_index]
    print(sum_of_column)
