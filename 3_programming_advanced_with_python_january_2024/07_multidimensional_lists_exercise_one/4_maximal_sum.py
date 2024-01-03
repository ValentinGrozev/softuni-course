rows, columns = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()]for _ in range(rows)]

max_sum = float("-inf")
max_matrix = []
current_matrix = []
current_sum = 0

for row in range(rows - 2):
    for col in range(columns - 2):
        current_matrix = []
        for sub_row_index in range(row, row + 3):
            current_matrix.append([])
            for sub_col_index in range(col, col + 3):
                current_matrix[sub_row_index - row].append(matrix[sub_row_index][sub_col_index])
                current_sum += matrix[sub_row_index][sub_col_index]
        if current_sum > max_sum:
            max_matrix = current_matrix
            max_sum = current_sum
            current_sum = 0
        else:
            current_sum = 0

print(f"Sum = {max_sum}")
print(" ".join(str(x) for x in max_matrix[0]))
print(" ".join(str(x) for x in max_matrix[1]))
print(" ".join(str(x) for x in max_matrix[2]))
