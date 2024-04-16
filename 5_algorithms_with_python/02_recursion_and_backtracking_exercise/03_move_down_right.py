def unique_paths(current_row, current_col, lab):
    if current_row < 0 or current_col < 0 or current_row == len(lab) or current_col == len(lab[0]):
        return 0
    if current_row == len(lab) - 1 and current_col == len(lab[0]) - 1:
        return 1

    return unique_paths(current_row, current_col + 1, lab) + unique_paths(current_row + 1, current_col, lab)


rows = int(input())
cols = int(input())
matrix = []

for row in range(rows):

    matrix.append([0] * cols)


print(unique_paths(0, 0, matrix))
