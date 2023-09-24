lost_battles_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_cost = 0

for lost_battle in range(1, lost_battles_count + 1):
    if lost_battle % 2 == 0:
        total_cost += helmet_price
    if lost_battle % 3 == 0:
        total_cost += sword_price
    if lost_battle % 6 == 0:
        total_cost += shield_price
    if lost_battle % 12 == 0:
        total_cost += armor_price

print(f"Gladiator expenses: {total_cost:.2f} aureus")
