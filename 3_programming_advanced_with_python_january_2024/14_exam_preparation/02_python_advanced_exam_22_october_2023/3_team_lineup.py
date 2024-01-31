def team_lineup(*players_info):
    team_information = {}
    for player, country in players_info:
        if country not in team_information:
            team_information[country] = []
        team_information[country].append(player)
    sorted_team = sorted(team_information.items(), key=lambda x: (-len(x[1]), x[0]))

    final_team = []

    for country, player_names in sorted_team:
        final_team.append(f"{country}:")
        for player_name in player_names:
            final_team.append(f"  -{player_name}")
    return '\n'.join(text for text in final_team)


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
