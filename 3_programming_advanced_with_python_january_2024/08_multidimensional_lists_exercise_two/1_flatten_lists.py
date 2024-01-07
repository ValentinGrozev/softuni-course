text = input().split("|")

matrix = []
reworked_matrix = []

for sub_matrix in text:
    matrix.append(sub_matrix.split())

for current_sub_matrix in range(len(matrix) - 1, -1, - 1):
    if len(matrix[current_sub_matrix]) > 0:
        reworked_matrix.append(matrix[current_sub_matrix])

for element in reworked_matrix:
    print(" ".join(element), end=" ")
