def find_areas(key_element, curr_row, curr_col, graph, visited):
    if curr_row < 0 or curr_row >= len(graph) or curr_col < 0 or curr_col >= len(graph[0]):
        return
    if visited[curr_row][curr_col]:
        return
    if graph[curr_row][curr_col] != key_element:
        return

    visited[curr_row][curr_col] = True

    find_areas(key_element, curr_row - 1, curr_col, graph, visited)
    find_areas(key_element, curr_row + 1, curr_col, graph, visited)
    find_areas(key_element, curr_row, curr_col - 1, graph, visited)
    find_areas(key_element, curr_row, curr_col + 1,  graph, visited)


rows = int(input())
cols = int(input())

matrix = [[x for x in list(input())] for _ in range(rows)]
visited_indexes = []
areas = {}
total_areas = 0

for row in range(rows):
    visited_indexes.append([False] * cols)

for row in range(rows):
    for col in range(cols):
        if visited_indexes[row][col]:
            continue
        key = matrix[row][col]
        find_areas(key, row, col, matrix, visited_indexes)

        if key not in areas:
            areas[key] = 0
        areas[key] += 1
        total_areas += 1

print(f"Areas: {total_areas}")
for key, value in sorted(areas.items()):
    print(f"Letter '{key}' -> {value}")
