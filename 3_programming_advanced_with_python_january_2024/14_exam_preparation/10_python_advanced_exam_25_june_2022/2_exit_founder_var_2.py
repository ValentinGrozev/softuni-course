from collections import deque
import re


def create_field(size):
    field = [[row for row in input().split(" ")] for _ in range(size)]
    return field


SIZE = 6

player_1, player_2 = input().split(", ")
players_info = deque([player_1, player_2])
hits_a_wall = {
    "Jerry": False,
    "Tom": False,
}

game_board = create_field(SIZE)

coordinates = input()

while coordinates:
    current_player = players_info.popleft()
    pattern = r"\d+"
    matched_indexes_as_string = re.findall(pattern, coordinates)
    row_index = int(matched_indexes_as_string[0])
    col_index = int(matched_indexes_as_string[1])

    if hits_a_wall[current_player]:
        hits_a_wall[current_player] = False
        players_info.append(current_player)
        coordinates = input()
        continue

    if game_board[row_index][col_index] == "E":
        print(f"{current_player} found the Exit and wins the game!")
        break
    elif game_board[row_index][col_index] == "T":
        print(f"{current_player} is out of the game! The winner is {players_info[0]}.")
        break
    elif game_board[row_index][col_index] == "W":
        print(f"{current_player} hits a wall and needs to rest.")
        hits_a_wall[current_player] = True
    else:
        pass

    players_info.append(current_player)
    coordinates = input()
