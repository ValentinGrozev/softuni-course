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
        next_row_char_position = char_position[0] - steps
        next_col_char_position = char_position[1] + moves[direction][1]
    elif direction == "down":
        next_row_char_position = char_position[0] + steps
        next_col_char_position = char_position[1] + moves[direction][1]
    elif direction == "left":
        next_row_char_position = char_position[0] + moves[direction][0]
        next_col_char_position = char_position[1] - steps
    else:
        next_row_char_position = char_position[0] + moves[direction][0]
        next_col_char_position = char_position[1] + steps
    return [next_row_char_position, next_col_char_position]


def is_valid_indexes(next_move_indexes, size, char_position, field):
    row = next_move_indexes[0]
    col = next_move_indexes[1]
    if 0 <= row < size and 0 <= col < size:
        if field[row][col] == ".":
            return row, col
        else:
            return char_position
    else:
        return char_position


def shoot(direction, char_position, field):
    current_row_position = char_position[0]
    current_col_position = char_position[1]
    shoot_counter = 0
    shoot_index = []
    if direction == "up":
        left_rows = 5 - current_row_position
        for rows in range(left_rows):
            next_row_char_position = char_position[0] - rows
            if field[next_row_char_position][current_col_position] == "x":
                shoot_counter += 1
                shoot_index.append([next_row_char_position, current_col_position])
                field[next_row_char_position][current_col_position] = "."
                break
        return shoot_counter, shoot_index
    if direction == "down":
        left_rows = 5 - current_row_position
        for rows in range(left_rows):
            next_row_char_position = char_position[0] + rows
            if field[next_row_char_position][current_col_position] == "x":
                shoot_counter += 1
                shoot_index.append([next_row_char_position, current_col_position])
                field[next_row_char_position][current_col_position] = "."
                break
        return shoot_counter, shoot_index
    if direction == "left":
        for cols in range(current_col_position, 0, -1):
            next_col_char_position = char_position[1] - cols
            if field[current_row_position][next_col_char_position] == "x":
                shoot_counter += 1
                shoot_index.append([current_row_position, next_col_char_position])
                field[current_row_position][next_col_char_position] = "."
                break
        return shoot_counter, shoot_index
    if direction == "right":
        left_cols = 5 - current_col_position
        for cols in range(left_cols):
            next_col_char_position = char_position[1] + cols
            if field[current_row_position][next_col_char_position] == "x":
                shoot_counter += 1
                shoot_index.append([current_row_position, next_col_char_position])
                field[current_row_position][next_col_char_position] = "."
                break
        return shoot_counter, shoot_index


moves = {
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
            char_position = is_valid_indexes(next_move_indexes, size, char_position, field)
        elif current_command[0] == "shoot":
            direction = current_command[1]
            targets, targets_index = shoot(direction, char_position, field)
            if len(targets_index) != 0:
                targets_index_down.append(targets_index)
            targets_down += targets
            if targets_down == len(targets_position):
                training_completed = True
                break

    if training_completed:
        print(f"Training completed! All {targets_down} targets hit.")
    else:
        print(f"Training not completed! {len(targets_position) - targets_down} targets left.")
    for target in targets_index_down:
        print(*target)


main()
