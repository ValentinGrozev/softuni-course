sequence_of_cards = input()

red_card_list = sequence_of_cards.split()
red_card_list_team_A = []
red_card_list_team_B = []
team_A_left_players = 0
team_B_left_players = 0

for x in red_card_list:
    if "A" in x:
        red_card_list_team_A.append(x)
    else:
        red_card_list_team_B.append(x)

num_repetitions_A = 0
occurrences_a = [False, False, False, False, False, False, False, False, False, False, False]
for idx in range(len(red_card_list_team_A)):
    player_number = int(red_card_list_team_A[idx][2:])
    if occurrences_a[player_number-1]:
        num_repetitions_A += 1
    else:
        occurrences_a[player_number-1] = True

num_repetitions_B = 0
occurrences_b = [False, False, False, False, False, False, False, False, False, False, False]
for idx in range(len(red_card_list_team_B)):
    player_number = int(red_card_list_team_B[idx][2:])
    if occurrences_b[player_number-1]:
        num_repetitions_B += 1
    else:
        occurrences_b[player_number-1] = True

team_A_left_players = 11 - len(red_card_list_team_A) + num_repetitions_A
team_B_left_players = 11 - len(red_card_list_team_B) + num_repetitions_B

if team_A_left_players < 7:
    print(f"Team A - {6}; Team B - {team_B_left_players}")
    print("Game was terminated")
elif team_B_left_players < 7:
    print(f"Team A - {team_A_left_players}; Team B - {6}")
    print("Game was terminated")
else:
    print(f"Team A - {team_A_left_players}; Team B - {team_B_left_players}")



