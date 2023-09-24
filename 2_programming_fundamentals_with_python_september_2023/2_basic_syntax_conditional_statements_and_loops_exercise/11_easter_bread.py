budget = float(input())
price_for_1_kg_flour = float(input())

price_for_1_pack_of_eggs = 0.75 * price_for_1_kg_flour
price_for_1_l_milk = 1.25 * price_for_1_kg_flour

cost_for_one_loaf = price_for_1_pack_of_eggs + price_for_1_kg_flour + 0.25 * price_for_1_l_milk

money_spend = 0
colored_eggs = 0
current_count_of_bread = 0

while money_spend + cost_for_one_loaf <= budget:
    colored_eggs += 3
    current_count_of_bread += 1
    money_spend += cost_for_one_loaf
    if current_count_of_bread % 3 == 0:
        colored_eggs -= current_count_of_bread - 2

money_left = budget - money_spend
print(f"You made {current_count_of_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")