def get_submatrix_sum(matrix, row, col, sub_size):
    submatrix = get_submatrix(matrix, row, col, sub_size)
    return sum([number for current_row in submatrix for number in current_row])


def get_submatrix(matrix, row, col, sub_size):
    sub_matrix = []
    for i in range(row, row + sub_size):
        sub_matrix.append([])
        for j in range(col, col + sub_size):
            sub_matrix[i - row].append(matrix[i][j])
    return sub_matrix


def main():
    rows, columns = [int(x) for x in input().split()]

    matrix = [[int(x) for x in input().split()]for _ in range(rows)]

    max_sum = float("-inf")
    sub_matrix_size = 3
    max_i = rows - sub_matrix_size
    max_j = columns - sub_matrix_size
    max_pair = 0

    for i in range(0, max_i + 1):
        for j in range(0, max_j + 1):
            current_sum = get_submatrix_sum(matrix, i, j, sub_matrix_size)
            if current_sum > max_sum:
                max_sum = current_sum
                max_pair = (i, j)

    found_submatrix = get_submatrix(matrix, *max_pair, sub_matrix_size)
    print(f"Sum = {max_sum}")
    print(*found_submatrix[0])
    print(*found_submatrix[1])
    print(*found_submatrix[2])


main()
