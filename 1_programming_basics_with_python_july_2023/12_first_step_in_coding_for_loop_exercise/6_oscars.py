name_of_actor = input()
points_from_academy = float(input())
number_of_voters = int(input())
nominated = False

final_points = points_from_academy

for _ in range(number_of_voters):
    name_of_voter = input()
    points_from_voter = float(input())
    final_points += (len(name_of_voter) * points_from_voter) / 2

    if final_points >= 1250.5:
        nominated = True
        break

if nominated:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {final_points:.1f}!")
else:
    diff = 1250.5 - final_points
    print(f"Sorry, {name_of_actor} you need {diff:.1f} more!")
