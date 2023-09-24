quantity_of_decorations = int(input())
days_left_until_christmas = int(input())
passed_days = 1

# outputs
money_spent = 0
spirit_points = 0

while days_left_until_christmas > 0:
    if passed_days % 30 == 0:
        pass
    if passed_days % 11 == 0:
        quantity_of_decorations += 2

    if passed_days % 2 == 0:
        spirit_points += 5
        money_spent += 2 * quantity_of_decorations
    if passed_days % 3 == 0:
        spirit_points += 13
        money_spent += 8 * quantity_of_decorations
    if passed_days % 5 == 0:
        spirit_points += 17
        money_spent += 15 * quantity_of_decorations

        # special case
        if passed_days % 3 == 0:
            spirit_points += 30

    if passed_days % 10 == 0:
        spirit_points -= 20
        money_spent += 23

    passed_days += 1
    days_left_until_christmas -= 1

if passed_days % 10 == 1:
    spirit_points -= 30

print(f"Total cost: {money_spent}")
print(f"Total spirit: {spirit_points}")
