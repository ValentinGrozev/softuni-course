prize_for_mackerel = float(input())
prize_for_sprinkle = float(input())
quantity_of_bonito = float(input())
quantity_of_safrid = float(input())
quantity_of_mussels = int(input())

prize_for_bonito = 1.6 * prize_for_mackerel
prize_for_sarid = 1.8 * prize_for_sprinkle
prize_for_mussels = 7.5

cost_for_bonito = quantity_of_bonito * prize_for_bonito
cost_for_safrid = quantity_of_safrid * prize_for_sarid
cost_for_mussels = quantity_of_mussels * prize_for_mussels
total_cost = cost_for_bonito + cost_for_safrid + cost_for_mussels

print(f"{total_cost:.2f}")
