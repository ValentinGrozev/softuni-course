def create_field(size):
    field = [[x for x in input().split()] for _ in range(size)]
    return field


def find_char_position(field):
    for row in range(len(field)):
        for col in range(len(field)):
            if field[row][col] == "A":
                char_position = [row, col]
                field[row][col] = "."
                return char_position, field


def find_targets_positions(field):
    targets = []
    for row in range(len(field)):
        for col in range(len(field)):
            if field[row][col] == "x":
                targets.append([row, col])
    return targets


def move_command(direction, steps, char_position):
    if direction == "up":
        next_row_position = char_position[0] - steps
        next_col_position = char_position[1]
    elif direction == "down":
        next_row_position = char_position[0] + steps
        next_col_position = char_position[1]
    elif direction == "left":
        next_row_position = char_position[0]
        next_col_position = char_position[1] - steps
    else:
        next_row_position = char_position[0]
        next_col_position = char_position[1] + steps
    return [next_row_position, next_col_position]


def is_valid_indexes(next_move_indexes, size, field):
    row = next_move_indexes[0]
    col = next_move_indexes[1]
    if 0 <= row < size and 0 <= col < size:
        if field[row][col] == ".":
            return True
    return False


def shoot(direction, current_position, field, size):
    row = current_position[0] + MOVES[direction][0]
    col = current_position[1] + MOVES[direction][1]
    while 0 <= row < size and 0 <= col < size:
        if field[row][col] == "x":
            field[row][col] = "."
            return True, [row, col]
        row += MOVES[direction][0]
        col += MOVES[direction][1]
    return False, None


MOVES = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}


def main():
    size = 5
    field = create_field(size)
    char_position, field = find_char_position(field)
    targets_position = find_targets_positions(field)

    number_of_command = int(input())

    targets_down = 0
    targets_index_down = []
    training_completed = False

    for command in range(number_of_command):
        current_command = input().split()
        if current_command[0] == "move":
            direction = current_command[1]
            steps = int(current_command[2])
            next_move_indexes = move_command(direction, steps, char_position)
            if is_valid_indexes(next_move_indexes, size, field):
                char_position = next_move_indexes
        elif current_command[0] == "shoot":
            direction_command = current_command[1]
            target_hit, target_position = shoot(direction_command, char_position, field, size)
            if target_hit:
                targets_index_down.append(target_position)
                targets_down += 1
            if targets_down == len(targets_position):
                training_completed = True
                break

    if training_completed:
        print(f"Training completed! All {targets_down} targets hit.")
    else:
        print(f"Training not completed! {len(targets_position) - targets_down} targets left.")
    for target in targets_index_down:
        print(target)


main()
