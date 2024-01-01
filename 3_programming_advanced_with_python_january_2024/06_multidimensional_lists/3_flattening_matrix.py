number_of_matrix_rows = int(input())
matrix = []

for row in range(number_of_matrix_rows):
    matrix.append([int(x) for x in input().split(', ')])

flattened_matrix = []

for current_row in matrix:
    for number in current_row:
        flattened_matrix.append(number)

print(flattened_matrix)

# With list comprehension:

number_of_matrix_rows = int(input())
matrix = []

for row in range(number_of_matrix_rows):
    matrix.append([int(x) for x in input().split(', ')])

flattened_matrix = [number for current_row in matrix for number in current_row]

print(flattened_matrix)
