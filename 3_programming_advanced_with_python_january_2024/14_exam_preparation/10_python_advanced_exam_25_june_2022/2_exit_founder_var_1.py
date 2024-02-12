import re


def create_field(size):
    field = [[row for row in input().split(" ")]for _ in range(size)]
    return field


SIZE = 6

player_1, player_2 = input().split(", ")
is_first_next = True

hits_a_wall = {
    "Jerry": False,
    "Tom": False,
}

game_board = create_field(SIZE)

coordinates = input()

while coordinates:
    current_player = player_1 if is_first_next else player_2
    pattern = r"\d+"
    matched_indexes_as_string = re.findall(pattern, coordinates)
    row_index = int(matched_indexes_as_string[0])
    col_index = int(matched_indexes_as_string[1])

    if hits_a_wall[current_player]:
        hits_a_wall[current_player] = False
        is_first_next = not is_first_next
        coordinates = input()
        continue

    if game_board[row_index][col_index] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break
    elif game_board[row_index][col_index] == "T":
        print(f"{current_player} is out of the game! The winner is {player_2 if is_first_next else player_1}.")
        break
    elif game_board[row_index][col_index] == "W":
        print(f"{current_player} hits a wall and needs to rest.")
        hits_a_wall[current_player] = True
    else:
        pass

    is_first_next = not is_first_next
    coordinates = input()
