size_of_board = int(input())

chess_table = []
knights = []

for _ in range(size_of_board):
    chess_table.append([x for x in input()])

for row in range(size_of_board):
    for col in range(size_of_board):
        if chess_table[row][col] == "K":
            knights.append([row, col])

possible_moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
removed_knights = 0

while True:
    max_attacks = 0
    max_knights = [0, 0]

    for k_row, k_col in knights:
        hits = 0
        for move in possible_moves:
            current_move_for_row = move[0] + k_row
            current_move_for_col = move[1] + k_col
            if 0 <= current_move_for_row < size_of_board and 0 <= current_move_for_col < size_of_board:
                if chess_table[current_move_for_row][current_move_for_col] == "K":
                    hits += 1
        if hits > max_attacks:
            max_attacks = hits
            max_knights = [k_row, k_col]

    if max_attacks == 0:
        break
    knights.remove(max_knights)
    chess_table[max_knights[0]][max_knights[1]] = "0"
    removed_knights += 1

print(removed_knights)
