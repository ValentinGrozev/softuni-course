def create_field(size):
    game_field = [[x for x in input().split()]for _ in range(size)]
    return game_field


def find_char_location(game_field, size):
    for row_index in range(size):
        for col_index in range(size):
            if game_field[row_index][col_index] == "s":
                char_location = [row_index, col_index]
                game_field[row_index][col_index] = "*"
                return char_location, game_field


def find_bomb_location(game_field, size):
    for row_index in range(size):
        for col_index in range(size):
            if game_field[row_index][col_index] == "e":
                return [row_index, col_index]


def find_all_coals(game_field, size):
    coals = 0
    for row_index in range(size):
        for col_index in range(size):
            if game_field[row_index][col_index] == "c":
                coals += 1
    return coals


def is_valid_move(next_row_move, next_col_move, size):
    return 0 <= next_row_move < size and 0 <= next_col_move < size


def next_move(field, row_move, col_move):
    char_location = [row_move, col_move]
    coals = 0
    for _ in field:
        if field[row_move][col_move] == "c":
            coals += 1
            field[row_move][col_move] = "*"
        return char_location, coals


def main():
    field_size = int(input())
    direction_commands = input().split()

    field = create_field(field_size)
    char_coordinates, field = find_char_location(field, field_size)
    bomb_location = find_bomb_location(field, field_size)
    all_coals_on_field = find_all_coals(field, field_size)

    possible_moves = {
        "up": [-1, 0],
        "down": [1, 0],
        "left": [0, -1],
        "right": [0, 1],
    }

    current_coals = 0
    game_over = False

    for command in direction_commands:
        row_move = char_coordinates[0] + possible_moves[command][0]
        col_move = char_coordinates[1] + possible_moves[command][1]
        is_valid = is_valid_move(row_move, col_move, field_size)
        if is_valid:
            char_coordinates, coals = next_move(field, row_move, col_move)
            current_coals += coals
            if char_coordinates == bomb_location:
                print(f"Game over! ({', '.join(str(x) for x in bomb_location)})")
                game_over = True
                break
            elif current_coals == all_coals_on_field:
                print(f"You collected all coal! ({', '.join(str(x) for x in char_coordinates)})")
                game_over = True
                break

    if not game_over:
        print(f"{all_coals_on_field - current_coals} pieces of coal left. "
              f"({', '.join(str(x) for x in char_coordinates)})")


main()
