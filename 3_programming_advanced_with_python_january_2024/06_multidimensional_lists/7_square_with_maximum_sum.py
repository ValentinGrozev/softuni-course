rows, columns = [int(x) for x in input().split(', ')]

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

max_sum = 0
max_matrix = []

for row_index in range(rows - 1):
    for column_index in range(columns - 1):
        first_element = matrix[row_index][column_index]
        second_element = matrix[row_index][column_index + 1]
        below_first_element = matrix[row_index + 1][column_index]
        below_second_element = matrix[row_index + 1][column_index + 1]
        total_sum = first_element + second_element + below_first_element + below_second_element
        if total_sum > max_sum:
            max_sum = total_sum
            max_matrix = [[first_element, second_element], [below_first_element, below_second_element]]

print(" ".join(str(x) for x in max_matrix[0]))
print(" ".join(str(x) for x in max_matrix[1]))
print(max_sum)
