rows = columns = int(input())

matrix = []

for row in range(rows):
    matrix.append(list(input()))

searched_symbol = input()
is_found = False

for row_index in range(rows):
    for column_index in range(columns):
        if searched_symbol == matrix[row_index][column_index]:
            print((row_index, column_index))
            is_found = True
            break
    if is_found:
        break

if not is_found:
    print(f"{searched_symbol} does not occur in the matrix")
