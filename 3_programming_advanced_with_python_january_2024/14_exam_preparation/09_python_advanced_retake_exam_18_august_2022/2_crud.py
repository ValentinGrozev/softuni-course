def create_matrix(size):
    matrix = [[row for row in input().split(" ")] for _ in range(size)]
    return matrix


def next_coordinates(coordinates, direction):
    next_row_index = coordinates[0] + DIRECTIONS[direction][0]
    next_col_index = coordinates[1] + DIRECTIONS[direction][1]
    coordinates = [next_row_index, next_col_index]
    return coordinates


def create(coordinates, matrix, direction, value):
    coordinates = next_coordinates(coordinates, direction)

    if matrix[coordinates[0]][coordinates[1]] == ".":
        matrix[coordinates[0]][coordinates[1]] = value
        return matrix, coordinates
    else:
        return matrix, coordinates


def update(coordinates, matrix, direction, value):
    coordinates = next_coordinates(coordinates, direction)

    if matrix[coordinates[0]][coordinates[1]] != ".":
        matrix[coordinates[0]][coordinates[1]] = value
        return matrix, coordinates
    else:
        return matrix, coordinates


def delete(coordinates, matrix, direction):
    coordinates = next_coordinates(coordinates, direction)

    if matrix[coordinates[0]][coordinates[1]] != ".":
        matrix[coordinates[0]][coordinates[1]] = "."
        return matrix, coordinates
    else:
        return matrix, coordinates


def read(coordinates, matrix, direction):
    coordinates = next_coordinates(coordinates, direction)

    if matrix[coordinates[0]][coordinates[1]] != ".":
        print(matrix[coordinates[0]][coordinates[1]])
        return coordinates
    return coordinates


SIZE = 6
DIRECTIONS = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}


def main():
    matrix = create_matrix(SIZE)

    starting_coordinates = input()

    coordinates = []

    for coordinate in starting_coordinates:
        if coordinate.isdigit():
            coordinates.append(int(coordinate))

    while True:
        command = input()

        command_info = command.split(", ")
        command_title = command_info[0]

        if command_title == "Stop":
            break
        elif command_title == "Create":
            direction = command_info[1]
            value = command_info[2]
            matrix, coordinates = create(coordinates, matrix, direction, value)
        elif command_title == "Update":
            direction = command_info[1]
            value = command_info[2]
            matrix, coordinates = update(coordinates, matrix, direction, value)
        elif command_title == "Delete":
            direction = command_info[1]
            matrix, coordinates = delete(coordinates, matrix, direction)
        elif command_title == "Read":
            direction = command_info[1]
            coordinates = read(coordinates, matrix, direction)

    print(*[' '.join(row) for row in matrix], sep="\n")


main()
