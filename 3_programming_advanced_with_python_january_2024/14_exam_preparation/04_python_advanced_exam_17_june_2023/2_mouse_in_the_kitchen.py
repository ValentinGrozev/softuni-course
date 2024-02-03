def create_cupboards_area(rows):
    cupboard_area = [[row for row in list(input())]for _ in range(rows)]
    return cupboard_area


def find_mouse_position(rows, cols, cupboard_area):
    for row in range(rows):
        for col in range(cols):
            if cupboard_area[row][col] == "M":
                return [row, col]


def find_all_cheeses(rows, cols, cupboard_area):
    counter = 0
    for row in range(rows):
        for col in range(cols):
            if cupboard_area[row][col] == "C":
                counter += 1
    return counter


def next_move(mouse_position, command):
    next_row_position = mouse_position[0] + MOVES[command][0]
    next_col_position = mouse_position[1] + MOVES[command][1]
    return [next_row_position, next_col_position]


def is_valid_position(next_row_pos, next_col_pos, rows, cols):
    if 0 <= next_row_pos < rows and 0 <= next_col_pos < cols:
        return [next_row_pos, next_col_pos]
    else:
        return False


def is_position_wall(next_row_pos, next_col_pos, cupboard_area):
    return cupboard_area[next_row_pos][next_col_pos] == "@"


MOVES = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}


def main():
    rows, cols = [int(x) for x in input().split(",")]
    cupboard_area = create_cupboards_area(rows)

    mouse_position = find_mouse_position(rows, cols, cupboard_area)
    cupboard_area[mouse_position[0]][mouse_position[1]] = "*"
    cheeses = find_all_cheeses(rows, cols, cupboard_area)

    trapped = False
    out_of_the_board = False

    command = None

    while cheeses:
        command = input()

        if command == "danger":
            break

        new_position = next_move(mouse_position, command)

        if is_valid_position(new_position[0], new_position[1], rows, cols):
            if is_position_wall(new_position[0], new_position[1], cupboard_area):
                continue
            else:
                mouse_position = new_position
        else:
            print("No more cheese for tonight!")
            out_of_the_board = True
            break

        if cupboard_area[mouse_position[0]][mouse_position[1]] == "*":
            continue
        elif cupboard_area[mouse_position[0]][mouse_position[1]] == "T":
            print("Mouse is trapped!")
            trapped = True
            break
        elif cupboard_area[mouse_position[0]][mouse_position[1]] == "C":
            cupboard_area[mouse_position[0]][mouse_position[1]] = "*"
            cheeses -= 1
            if cheeses == 0:
                print("Happy mouse! All the cheese is eaten, good night!")
                break

    cupboard_area[mouse_position[0]][mouse_position[1]] = "M"

    if command == "danger" and cheeses != 0 and (not trapped) and (not out_of_the_board):
        print("Mouse will come back later!")

    for row in cupboard_area:
        print(''.join(row))


main()
