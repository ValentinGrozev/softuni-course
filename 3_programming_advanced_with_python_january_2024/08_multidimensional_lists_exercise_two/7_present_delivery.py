def create_neighborhood(size):
    neighborhood = [[x for x in input().split()] for _ in range(size)]
    return neighborhood


def find_santa(neighborhood, size):
    for row in range(size):
        for col in range(size):
            if neighborhood[row][col] == "S":
                return [row, col]


def nice_kids_counter(neighborhood, size):
    counter = 0
    for row in range(size):
        for col in range(size):
            if neighborhood[row][col] == "V":
                counter += 1
    return counter


def next_move_position(direction, santa_position):
    next_row_position = santa_position[0] + MOVES[direction][0]
    next_col_position = santa_position[1] + MOVES[direction][1]
    return [next_row_position, next_col_position]


def eat_cookie(presents, good_kids, neighborhood, santa_position):
    for move in MOVES:
        next_row_position = santa_position[0] + MOVES[move][0]
        next_col_position = santa_position[1] + MOVES[move][1]

        if neighborhood[next_row_position][next_col_position] == "V":
            good_kids += 1
            presents -= 1
            neighborhood[next_row_position][next_col_position] = "-"
        elif neighborhood[next_row_position][next_col_position] == "X":
            presents -= 1
            neighborhood[next_row_position][next_col_position] = "-"

        if presents == 0:
            break

    return presents, good_kids


MOVES = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}


def main():
    presents = int(input())
    size_of_neighborhood = int(input())
    neighborhood = create_neighborhood(size_of_neighborhood)
    santa_position = find_santa(neighborhood, size_of_neighborhood)
    neighborhood[santa_position[0]][santa_position[1]] = "-"
    good_kids = nice_kids_counter(neighborhood, size_of_neighborhood)
    good_kids_got_present = 0

    command = input()
    while command != "Christmas morning":
        santa_position = next_move_position(command, santa_position)
        if neighborhood[santa_position[0]][santa_position[1]] == "V":
            presents -= 1
            good_kids_got_present += 1
        elif neighborhood[santa_position[0]][santa_position[1]] == "C":
            presents, good_kids_got_present = eat_cookie(presents, good_kids_got_present, neighborhood, santa_position)

        neighborhood[santa_position[0]][santa_position[1]] = "-"

        if not presents or good_kids_got_present == good_kids:
            break

        command = input()

    neighborhood[santa_position[0]][santa_position[1]] = "S"

    if not presents and good_kids_got_present < good_kids:
        print("Santa ran out of presents!")
    for current_row in neighborhood:
        print(*current_row)

    if good_kids_got_present == good_kids:
        print(f"Good job, Santa! {good_kids_got_present} happy nice kid/s.")
    else:
        print(f"No presents for {good_kids - good_kids_got_present} nice kid/s.")


main()
