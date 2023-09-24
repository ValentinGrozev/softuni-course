change = float(input())

change_in_coins = int(change * 100)

count = 0

while change_in_coins > 0:
    if 200 <= change_in_coins:
        change_in_coins -= 200
        count += 1
    elif 100 <= change_in_coins:
        change_in_coins -= 100
        count += 1
    elif 50 <= change_in_coins:
        change_in_coins -= 50
        count += 1
    elif 20 <= change_in_coins:
        change_in_coins -= 20
        count += 1
    elif 10 <= change_in_coins:
        change_in_coins -= 10
        count += 1
    elif 5 <= change_in_coins:
        change_in_coins -= 5
        count += 1
    elif 2 <= change_in_coins:
        change_in_coins -= 2
        count += 1
    elif 1 <= change_in_coins:
        change_in_coins -= 1
        count += 1

print(count)
