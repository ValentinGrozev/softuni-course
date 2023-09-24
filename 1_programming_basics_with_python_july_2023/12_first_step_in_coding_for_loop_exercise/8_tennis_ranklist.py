import math

number_of_tournaments = int(input())
starting_points = int(input())

average_points = 0
won_tournaments = 0
final_points = 0

for _ in range(number_of_tournaments):
    stage_of_tournament = input()

    if stage_of_tournament == "W":
        points = 2000
        final_points += points
        won_tournaments += 1
    elif stage_of_tournament == "F":
        points = 1200
        final_points += points
    elif stage_of_tournament == "SF":
        points = 720
        final_points += points

final_points = final_points + starting_points
average_points = (final_points - starting_points) / number_of_tournaments
average_points = math.floor(average_points)
percent_of_wining_tournaments = (won_tournaments / number_of_tournaments) * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{percent_of_wining_tournaments:.2f}%")

