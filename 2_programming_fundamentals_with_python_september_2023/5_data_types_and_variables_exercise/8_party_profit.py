from math import floor

group_size = int(input())
days = int(input())

earned_coins = 0
spend_coins = 0
day = 1

for day in range(1, days + 1):
    if day % 10 == 0:
        group_size = group_size - 2
    if day % 15 == 0:
        group_size = group_size + 5

    earned_coins += 50
    spend_coins += 2 * group_size

    if day % 3 == 0:
        spend_coins += 3 * group_size
    if day % 5 == 0:
        earned_coins += 20 * group_size
        if day % 3 == 0:
            spend_coins += 2 * group_size

coin_for_each_companion = floor((earned_coins - spend_coins) / group_size)
print(f"{group_size} companions received {coin_for_each_companion} coins each.")