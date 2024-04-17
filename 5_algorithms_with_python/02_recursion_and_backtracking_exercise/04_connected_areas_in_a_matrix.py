def find_area_start_indexes(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == "-":
                return row, col


def find_area(row_idx, col_idx, matrix):
    if row_idx < 0 or row_idx == len(matrix) or col_idx < 0 or col_idx == len(matrix[0]):
        return 0
    if matrix[row_idx][col_idx] == "*":
        return 0
    if matrix[row_idx][col_idx] == "V":
        return 0

    matrix[row_idx][col_idx] = "V"

    result = find_area(row_idx, col_idx + 1, matrix)  # right
    result += find_area(row_idx, col_idx - 1, matrix)  # left
    result += find_area(row_idx + 1, col_idx, matrix)  # down
    result += find_area(row_idx - 1, col_idx, matrix)  # up

    return 1 + result


rows = int(input())
cols = int(input())
labyrinth = [[x for x in input()] for _ in range(rows)]
areas = []

while True:
    area_indexes = find_area_start_indexes(labyrinth)
    if area_indexes:
        length = (find_area(area_indexes[0], area_indexes[1], labyrinth))
        areas.append((area_indexes[0], area_indexes[1], length))
    else:
        break

sorted_areas = sorted(areas, key=lambda x: (-x[2], x[0], x[1]))

print(f"Total areas found: {len(sorted_areas)}")

for idx, (row_index, col_index, length) in enumerate(sorted_areas):
    print(f"Area #{idx + 1} at ({row_index}, {col_index}), size: {length}")
