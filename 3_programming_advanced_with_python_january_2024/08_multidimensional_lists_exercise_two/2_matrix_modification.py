def is_valid_index(r, c, rows, matrix):
    if 0 <= r < rows and 0 <= c < len(matrix):
        return True
    else:
        print("Invalid coordinates")


def add_number(r, c, value, matrix):
    matrix[r][c] += value
    return matrix


def subtract_number(r, c, value, matrix):
    matrix[r][c] -= value
    return matrix


def main():
    matrix_rows = int(input())

    matrix = []

    for row in range(matrix_rows):
        matrix.append([int(x) for x in input().split()])

    while True:
        command = input().split()
        if command[0] == "END":
            break
        else:
            row_index = int(command[1])
            col_index = int(command[2])
            value = int(command[3])
            if is_valid_index(row_index, col_index, matrix_rows, matrix):
                if command[0] == "Add":
                    add_number(row_index, col_index, value, matrix)
                elif command[0] == "Subtract":
                    subtract_number(row_index, col_index, value, matrix)

    for element in matrix:
        print(*element, sep=" ")


main()
