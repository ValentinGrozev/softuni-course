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
    value = matrix[row_bomb_index][col_bomb_index]
    if value <= 0:
        continue

    for index in exploded_cells:
        row_index = index[0]
        col_index = index[1]
        exploded_row_index = row_bomb_index + row_index
        exploded_col_index = col_bomb_index + col_index

        if 0 <= exploded_row_index < size and 0 <= exploded_col_index < size:
            if matrix[exploded_row_index][exploded_col_index] > 0:
                matrix[exploded_row_index][exploded_col_index] -= value

active_cells = 0
sum_of_active_cells = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] > 0:
            active_cells += 1
            sum_of_active_cells += matrix[row][col]

print(f"Alive cells: {active_cells}")
print(f"Sum: {sum_of_active_cells}")

for row in matrix:
    print(*row, sep=" ")
