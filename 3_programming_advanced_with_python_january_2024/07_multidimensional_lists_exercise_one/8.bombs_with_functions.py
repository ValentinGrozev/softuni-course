def check_is_bomb_a_positive_number(matrix, row, col):
    return matrix[row][col] > 0


def cell_to_explode(row_bomb_index, col_bomb_index, row_index, col_index):
    row = row_bomb_index + row_index
    col = col_bomb_index + col_index
    return row, col


def is_valid_index(row_index, col_index, size):
    return 0 <= row_index < size and 0 <= col_index < size


def matrix_change(matrix, row_index, col_index, row_bomb_index, col_bomb_index):
    if matrix[row_index][col_index] > 0:
        matrix[row_index][col_index] -= matrix[row_bomb_index][col_bomb_index]
    return matrix


def sum_of_active_cells_and_their_count(matrix, size):
    active_cells = 0
    sum_of_active_cells = 0

    for row in range(size):
        for col in range(size):
            if matrix[row][col] > 0:
                active_cells += 1
                sum_of_active_cells += matrix[row][col]
    return active_cells, sum_of_active_cells


def main():
    size = int(input())
    matrix = [[int(x) for x in input().split()]for _ in range(size)]
    indices = [[int(c) for c in x.split(",")] for x in input().split()]

    exploded_cells = [
        (-1, 0),   # up
        (-1, -1),  # up-left diagonal
        (-1, 1),   # up-right diagonal
        (0, -1),   # left
        (0, 1),    # right
        (1, 0),    # down
        (1, -1),   # down-left diagonal
        (1, 1),    # down-right diagonal
        (0, 0),    # bomb itself
    ]

    for current_index in indices:
        row_bomb_index = current_index[0]
        col_bomb_index = current_index[1]
        is_valid = check_is_bomb_a_positive_number(matrix, row_bomb_index, col_bomb_index)
        if not is_valid:
            continue

        for index in exploded_cells:
            row_index = index[0]
            col_index = index[1]
            exploded_row_index, exploded_col_index = cell_to_explode(row_bomb_index,
                                                                     col_bomb_index, row_index, col_index)

            if is_valid_index(exploded_row_index, exploded_col_index, size):
                matrix = matrix_change(matrix, exploded_row_index, exploded_col_index, row_bomb_index, col_bomb_index)

    active_cells, sum_of_active_cells = sum_of_active_cells_and_their_count(matrix, size)

    print(f"Alive cells: {active_cells}")
    print(f"Sum: {sum_of_active_cells}")
    [print(*row) for row in matrix]


main()
