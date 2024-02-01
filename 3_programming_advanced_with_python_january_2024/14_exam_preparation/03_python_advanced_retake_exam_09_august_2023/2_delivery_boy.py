def create_neighborhood(rows):
    neighborhood = [[row for row in list(input())]for _ in range(rows)]
    return neighborhood


def position(rows, cols, neighborhood):
    for row in range(rows):
        for col in range(cols):
            if neighborhood[row][col] == "B":
                return [row, col]


def next_move(deliver_position, command, rows, cols, neighborhood):
    next_row_position = deliver_position[0] + MOVES[command][0]
    next_col_position = deliver_position[1] + MOVES[command][1]
    if is_valid_position(next_row_position, next_col_position, rows, cols):
        if is_there_a_obstacle(next_row_position, next_col_position, neighborhood):
            return [deliver_position[0], deliver_position[1]]
        else:
            return [next_row_position, next_col_position]
    else:
        return False


def is_valid_position(next_row, next_col, rows, cols):
    return 0 <= next_row < rows and 0 <= next_col < cols


def is_there_a_obstacle(next_row, next_col, neighborhood):
    if neighborhood[next_row][next_col] == "*":
        return True
    else:
        return False


MOVES = {
    "up": [-1, 0],
    "down": [1, 0],
    "right": [0, 1],
    "left": [0, -1],
}


def main():
    rows_of_neighborhood, cols_of_neighborhood = [int(x) for x in input().split(" ")]
    neighborhood = create_neighborhood(rows_of_neighborhood)
    delivery_boy_position = position(rows_of_neighborhood, cols_of_neighborhood, neighborhood)
    starting_position = [delivery_boy_position[0], delivery_boy_position[1]]
    out_of_neighborhood = False

    command = input()

    while command:
        delivery_boy_position = next_move(delivery_boy_position, command,
                                          rows_of_neighborhood, cols_of_neighborhood, neighborhood)
        if not delivery_boy_position:
            print("The delivery is late. Order is canceled.")
            out_of_neighborhood = True
            break
        elif neighborhood[delivery_boy_position[0]][delivery_boy_position[1]] == "P":
            print("Pizza is collected. 10 minutes for delivery.")
            neighborhood[delivery_boy_position[0]][delivery_boy_position[1]] = "R"
        elif neighborhood[delivery_boy_position[0]][delivery_boy_position[1]] == "A":
            neighborhood[delivery_boy_position[0]][delivery_boy_position[1]] = "P"
            print("Pizza is delivered on time! Next order...")
            break
        elif neighborhood[delivery_boy_position[0]][delivery_boy_position[1]] == "-":
            neighborhood[delivery_boy_position[0]][delivery_boy_position[1]] = "."

        command = input()

    if out_of_neighborhood:
        neighborhood[starting_position[0]][starting_position[1]] = " "
    else:
        neighborhood[starting_position[0]][starting_position[1]] = "B"

    for row in neighborhood:
        print("".join(row))


main()
