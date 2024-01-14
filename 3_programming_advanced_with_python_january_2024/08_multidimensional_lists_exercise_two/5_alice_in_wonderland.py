def create_field(size):
    field = [([x for x in input().split()]) for _ in range(size)]
    return field


def find_alice(field, size):
    for row in range(size):
        for col in range(size):
            if field[row][col] == "A":
                return [row, col]


def find_rabbit_hole(field, size):
    for row in range(size):
        for col in range(size):
            if field[row][col] == "R":
                return [row, col]


def is_rabbit_hole(rabbit_hole, field, current_row_index, current_col_index):
    if field[current_row_index][current_col_index] == field[rabbit_hole[0]][rabbit_hole[1]]:
        return True


def is_outside_field(current_row_index, current_col_index, size):
    if not (0 <= current_row_index < size and 0 <= current_col_index < size):
        return True


def next_move(direction, row_position, col_position, moves):
    if direction == "up":
        alice_next_row_move = row_position + moves["up"][0]
        alice_next_col_move = col_position + moves["up"][1]
    elif direction == "down":
        alice_next_row_move = row_position + moves["down"][0]
        alice_next_col_move = col_position + moves["down"][1]
    elif direction == "left":
        alice_next_row_move = row_position + moves["left"][0]
        alice_next_col_move = col_position + moves["left"][1]
    else:
        alice_next_row_move = row_position + moves["right"][0]
        alice_next_col_move = col_position + moves["right"][1]
    return alice_next_row_move, alice_next_col_move


def main():
    size_of_matrix = int(input())
    collected_bags = 0
    miss_the_party = False
    moves = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
    field = create_field(size_of_matrix)
    alice_spot = find_alice(field, size_of_matrix)
    rabbit_hole = find_rabbit_hole(field, size_of_matrix)
    field[alice_spot[0]][alice_spot[1]] = "*"

    while collected_bags < 10:
        command = input()
        current_alice_row_move = int(alice_spot[0])
        current_alice_col_move = int(alice_spot[1])
        al_next_row_move, al_next_col_move = next_move(command, current_alice_row_move, current_alice_col_move, moves)
        if is_outside_field(al_next_row_move, al_next_col_move, size_of_matrix):
            miss_the_party = True
            break
        elif is_rabbit_hole(rabbit_hole, field, al_next_row_move, al_next_col_move):
            miss_the_party = True
            field[al_next_row_move][al_next_col_move] = "*"
            break
        else:
            if field[al_next_row_move][al_next_col_move] not in [".", "*"]:
                collected_bags += int(field[al_next_row_move][al_next_col_move])
                alice_spot = [al_next_row_move, al_next_col_move]
            else:
                alice_spot = [al_next_row_move, al_next_col_move]
            field[al_next_row_move][al_next_col_move] = "*"

    if miss_the_party:
        print("Alice didn't make it to the tea party.")
    else:
        print("She did it! She went to the party.")
    for current_row in field:
        print(f"{' '.join(current_row)}")


main()
