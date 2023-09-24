prize_for_kg_vege = float(input())
prize_for_kg_fruit = float(input())
kg_vege = int(input())
kg_fruit = int(input())
fixed_price_bg_to_euro = 1.94

total_cost_leva = prize_for_kg_fruit * kg_fruit + prize_for_kg_vege * kg_vege
total_cost_euro = total_cost_leva / fixed_price_bg_to_euro

print(f"{total_cost_euro:.2f}")