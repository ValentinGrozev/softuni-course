def create_field(size):
    field = [[row for row in input().split(" ")]for _ in range(size)]
    return field


def starting_position(rows, cols, field):
    for row in range(rows):
        for col in range(cols):
            if field[row][col] == "B":
                return [row, col]


def move(current_position, command):
    new_row_position = current_position[0] + DIRECTIONS[command][0]
    new_col_position = current_position[1] + DIRECTIONS[command][1]
    return [new_row_position, new_col_position]


def is_valid_move(row_position, col_position, rows, cols):
    return 0 <= row_position < rows and 0 <= col_position < cols


def is_obstacle(row_position, col_position, field):
    if field[row_position][col_position] == "O":
        return True
    else:
        return False


DIRECTIONS = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}


def main():
    rows, cols = [int(x) for x in input().split()]

    field = create_field(rows)
    current_position = starting_position(rows, cols, field)

    moves_made = 0
    touched_opponents = 0

    command = input()

    while command != "Finish":
        next_position = move(current_position, command)
        if is_valid_move(next_position[0], next_position[1], rows, cols):
            if not is_obstacle(next_position[0], next_position[1], field):
                current_position = next_position
                moves_made += 1
            else:
                command = input()
                continue

        if field[current_position[0]][current_position[1]] == "P":
            field[current_position[0]][current_position[1]] = "-"
            touched_opponents += 1
            if touched_opponents == 3:
                break

        command = input()

    print("Game over!")
    print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")


main()
