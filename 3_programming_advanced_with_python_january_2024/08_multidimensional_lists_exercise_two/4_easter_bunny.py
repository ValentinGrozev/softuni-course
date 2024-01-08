size_of_field = int(input())

field = []
bunny_position = [0, 0]

for row in range(size_of_field):
    field.append([x for x in input().split()])
    for col in range(size_of_field):
        if field[row][col] == "B":
            bunny_position = [row, col]

moves = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
max_number_of_eggs = float('-inf')
bunny_way = ""
final_bunny_moves = []

for move in moves:
    current_eggs = 0
    current_bunny_moves = []
    for row in range(size_of_field):
        for col in range(size_of_field):
            next_row_position = bunny_position[0] + moves[move][0]
            next_col_position = bunny_position[1] + moves[move][1]
            if 0 <= next_row_position < size_of_field and 0 <= next_col_position < size_of_field:
                if field[next_row_position][next_col_position] == "X":
                    break
                else:
                    current_eggs += int(field[next_row_position][next_col_position])
                    current_bunny_moves.append([next_row_position, next_col_position])
                    if move == "up":
                        moves[move][0] += -1
                    elif move == "down":
                        moves[move][0] += 1
                    elif move == "left":
                        moves[move][1] += -1
                    elif move == "right":
                        moves[move][1] += 1
            else:
                break
    if current_eggs > max_number_of_eggs and current_bunny_moves:
        max_number_of_eggs = current_eggs
        final_bunny_moves = current_bunny_moves
        bunny_way = move

print(bunny_way)
for move in final_bunny_moves:
    print(move)
print(max_number_of_eggs)
