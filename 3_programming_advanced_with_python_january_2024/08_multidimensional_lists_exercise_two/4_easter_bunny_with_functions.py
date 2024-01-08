def create_field(field, size):
    for row in range(size):
        field.append([x for x in input().split()])
    return field


def find_bunny_position(field, size):
    for row in range(size):
        for col in range(size):
            if field[row][col] == "B":
                bunny_position = [row, col]
                return bunny_position


def is_valid_index(next_row_position, next_col_position, size):
    return 0 <= next_row_position < size and 0 <= next_col_position < size


def is_trap(field, row_position, col_position):
    return field[row_position][col_position] == "X"


def is_bunny(field, row_position, col_position):
    return field[row_position][col_position] == "B"


def next_position(bunny_position, move):
    next_row_position = bunny_position[0] + MOVES[move][0]
    next_col_position = bunny_position[1] + MOVES[move][1]
    return next_row_position, next_col_position


MOVES = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}


def main():
    size_of_field = int(input())

    field = []

    field = create_field(field, size_of_field)
    bunny_position = find_bunny_position(field, size_of_field)
    bunny_start_position = bunny_position

    max_number_of_eggs = float('-inf')
    bunny_way = ""
    final_bunny_moves = []

    for move in MOVES:
        current_eggs = 0
        current_bunny_moves = []
        bunny_position = bunny_start_position
        while is_valid_index(bunny_position[0], bunny_position[1], size_of_field):
            if is_trap(field, bunny_position[0], bunny_position[1]):
                break
            elif is_bunny(field, bunny_position[0], bunny_position[1]):
                bunny_position = next_position(bunny_position, move)
                continue
            current_eggs += int(field[bunny_position[0]][bunny_position[1]])
            current_bunny_moves.append([bunny_position[0], bunny_position[1]])
            bunny_position = next_position(bunny_position, move)
        if current_eggs > max_number_of_eggs and current_bunny_moves:
            max_number_of_eggs = current_eggs
            final_bunny_moves = current_bunny_moves
            bunny_way = move

    print(bunny_way)
    for move in final_bunny_moves:
        print(move)
    print(max_number_of_eggs)


main()
