def create_field(size):
    board = [[row for row in input().split(" ")]for _ in range(size)]
    return board


def rover_starting_position(board, size):
    for row in range(size):
        for col in range(size):
            if board[row][col] == "E":
                return [row, col]


def validating_move(position, command, size):
    row_position = position[0] + DIRECTIONS[command][0]
    col_position = position[1] + DIRECTIONS[command][1]

    if row_position < 0:
        row_position = size - 1
    elif row_position >= size:
        row_position = 0

    if col_position < 0:
        col_position = size - 1
    elif col_position >= size:
        col_position = 0

    return [row_position, col_position]


SIZE_OF_FIELD = 6
DIRECTIONS = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}


def main():
    field = create_field(SIZE_OF_FIELD)
    commands = [command for command in input().split(", ")]
    rover_position = rover_starting_position(field, SIZE_OF_FIELD)

    resources = {
        "water deposit": 0,
        "metal deposit": 0,
        "concrete deposit": 0,
    }

    for command in commands:
        rover_position = validating_move(rover_position, command, SIZE_OF_FIELD)

        if field[rover_position[0]][rover_position[1]] == "W":
            resources["water deposit"] += 1
            print(f'Water deposit found at ({rover_position[0]}, {rover_position[1]})')
        elif field[rover_position[0]][rover_position[1]] == "M":
            resources["metal deposit"] += 1
            print(f'Metal deposit found at ({rover_position[0]}, {rover_position[1]})')
        elif field[rover_position[0]][rover_position[1]] == "C":
            resources["concrete deposit"] += 1
            print(f'Concrete deposit found at ({rover_position[0]}, {rover_position[1]})')
        elif field[rover_position[0]][rover_position[1]] == "R":
            print(f"Rover got broken at ({rover_position[0]}, {rover_position[1]})")
            break

    if all(resources.values()) != 0:
        print("Area suitable to start the colony.")
    else:
        print("Area not suitable to start the colony.")


main()
