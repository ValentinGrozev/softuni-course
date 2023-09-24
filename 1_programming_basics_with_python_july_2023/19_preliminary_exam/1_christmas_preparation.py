rolls_of_wrapping_paper = int(input())
rolls_of_cloth = int(input())
glue_liters = float(input())
discount_percentage = int(input())

price_for_roll_of_wrapping_paper = 5.80
price_for_roll_of_cloth = 7.20
price_for_liter_glue = 1.20

price_for_all_stuffs = rolls_of_wrapping_paper * price_for_roll_of_wrapping_paper + rolls_of_cloth * \
                       price_for_roll_of_cloth + glue_liters * price_for_liter_glue
discount = price_for_all_stuffs * (discount_percentage / 100)
needed_money = price_for_all_stuffs - discount
print(f"{needed_money:.3f}")
