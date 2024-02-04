def create_field(size):
    field = [[row for row in list(input())]for _ in range(size)]
    return field


def squirrel_position(size, field):
    for row in range(size):
        for col in range(size):
            if field[row][col] == "s":
                return [row, col]


def next_move(squirrel_pos, command):
    next_row_move = squirrel_pos[0] + DIRECTIONS[command][0]
    next_col_move = squirrel_pos[1] + DIRECTIONS[command][1]
    return [next_row_move, next_col_move]


def is_valid_position(row_position, col_position, size):
    return 0 <= row_position < size and 0 <= col_position < size


DIRECTIONS = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}


def main():
    size_of_field = int(input())
    commands = [command for command in input().split(", ")]

    field = create_field(size_of_field)
    squirrel_pos = squirrel_position(size_of_field, field)

    hazelnuts = 0
    hazelnut_collected = False
    trap_or_out_of_field = False

    for command in commands:
        next_position = next_move(squirrel_pos, command)

        if is_valid_position(next_position[0], next_position[1], size_of_field):
            squirrel_pos = next_position
        else:
            print("The squirrel is out of the field.")
            trap_or_out_of_field = True
            break

        if field[next_position[0]][next_position[1]] == "t":
            print("Unfortunately, the squirrel stepped on a trap...")
            trap_or_out_of_field = True
            break
        elif field[next_position[0]][next_position[1]] == "h":
            hazelnuts += 1
            field[next_position[0]][next_position[1]] = "*"
            if hazelnuts == 3:
                hazelnut_collected = True
                break

    if hazelnut_collected:
        print("Good job! You have collected all hazelnuts!")
    else:
        if not trap_or_out_of_field:
            print("There are more hazelnuts to collect.")

    print(f"Hazelnuts collected: {hazelnuts}")


main()
