amount_of_nylon = int(input())
amount_of_paint = int(input())
amount_of_thinner = int(input())
workers_hours = int(input())

prize_for_nylon = 1.50
prize_for_paint = 14.50
prize_for_thinner = 5.00
prize_for_bag = 0.40

total_sum_for_needed_nyoln = (amount_of_nylon + 2) * prize_for_nylon
total_sum_for_paint = (amount_of_paint*1.10) * prize_for_paint
total_sum_for_thinner = amount_of_thinner * prize_for_thinner

total_sum_materials = total_sum_for_needed_nyoln + total_sum_for_paint + total_sum_for_thinner + prize_for_bag

workers_sum = 0.30 * total_sum_materials * workers_hours
all_cost = total_sum_materials + workers_sum

print(all_cost)
