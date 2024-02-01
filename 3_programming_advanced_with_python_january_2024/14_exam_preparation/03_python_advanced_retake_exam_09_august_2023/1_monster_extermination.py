from collections import deque

monster_armor_points = deque([int(x) for x in input().split(",")])
soldier_strike_impact = [int(x) for x in input().split(",")]
monster_killed = 0

while monster_armor_points and soldier_strike_impact:
    current_monster_ap = monster_armor_points.popleft()
    current_soldier_si = soldier_strike_impact.pop()

    if current_soldier_si >= current_monster_ap:
        left_power = current_soldier_si - current_monster_ap
        if len(soldier_strike_impact) != 0 and left_power > 0:
            soldier_strike_impact[-1] += left_power
        elif len(soldier_strike_impact) == 0 and left_power > 0:
            soldier_strike_impact.append(left_power)
        monster_killed += 1

    else:
        current_monster_ap = current_monster_ap - current_soldier_si
        monster_armor_points.append(current_monster_ap)


if not monster_armor_points:
    print("All monsters have been killed!")

if not soldier_strike_impact:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monster_killed}")
