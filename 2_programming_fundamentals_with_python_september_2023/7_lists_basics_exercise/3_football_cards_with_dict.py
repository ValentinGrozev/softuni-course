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

red_card_list_team_A = list(dict.fromkeys(red_card_list_team_A))
red_card_list_team_B = list(dict.fromkeys(red_card_list_team_B))
team_A_left_players = 11 - len(red_card_list_team_A)
team_B_left_players = 11 - len(red_card_list_team_B)

if team_A_left_players < 7:
    print(f"Team A - {6}; Team B - {team_B_left_players}")
    print("Game was terminated")
elif team_B_left_players < 7:
    print(f"Team A - {team_A_left_players}; Team B - {6}")
    print("Game was terminated")
else:
    print(f"Team A - {team_A_left_players}; Team B - {team_B_left_players}")



