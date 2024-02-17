from collections import deque

amount_of_money = [int(money) for money in input().split(" ")]
prices_of_food = deque([int(price) for price in input().split(" ")])
foods_ate = 0

while amount_of_money and prices_of_food:
    current_amount = amount_of_money.pop()
    current_price_of_food = prices_of_food.popleft()

    if current_amount == current_price_of_food:
        foods_ate += 1
    elif current_amount > current_price_of_food:
        difference = current_amount - current_price_of_food
        foods_ate += 1
        if amount_of_money:
            next_amount = amount_of_money.pop()
            next_amount += difference
            amount_of_money.append(next_amount)
    else:
        continue

if foods_ate >= 4:
    print(f"Gluttony of the day! Henry ate {foods_ate} foods.")

if 1 < foods_ate < 4:
    print(f"Henry ate: {foods_ate} foods.")

if foods_ate == 1:
    print(f"Henry ate: {foods_ate} food.")

if foods_ate == 0:
    print("Henry remained hungry. He will try next weekend again.")
