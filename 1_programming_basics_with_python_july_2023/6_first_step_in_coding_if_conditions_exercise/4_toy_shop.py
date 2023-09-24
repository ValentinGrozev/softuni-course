price_for_vacation = float(input())
puzzle_count = int(input())
dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
truck_count = int(input())

puzzle_price = 2.60
dolls_price = 3
teddy_bears_price = 4.10
minions_price = 8.20
truck_price = 2

total_price_puzzle = puzzle_count * puzzle_price
total_prize_dolls = dolls_count * dolls_price
total_price_teddy_bears = teddy_bears_count * teddy_bears_price
total_minions_price = minions_count * minions_price
total_truck_prize = truck_count * truck_price

total_toys_purached = puzzle_count + dolls_count + teddy_bears_count + minions_count + truck_count

total_cost = total_price_puzzle + total_prize_dolls + total_price_teddy_bears + total_minions_price + total_truck_prize

if total_toys_purached >= 50:
    total_cost = total_cost * 0.75

rent = 0.1 * total_cost
final_cost = total_cost - rent

diff = abs(final_cost - price_for_vacation)

if final_cost >= price_for_vacation:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2F} lv needed.")



