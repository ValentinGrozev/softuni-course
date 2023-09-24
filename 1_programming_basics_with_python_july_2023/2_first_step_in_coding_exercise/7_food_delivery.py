count_chicken_menus = int(input())
count_fish_menus = int(input())
count_vege_menus = int(input())

chicken_menu_prize = 10.35
fish_menu_prize = 12.40
vege_menu_price = 8.15
delivery = 2.50

total_prize_chicken_menu = count_chicken_menus * chicken_menu_prize
total_price_fish_menu = count_fish_menus * fish_menu_prize
total_price_vege_menu = count_vege_menus * vege_menu_price
total_cost = total_prize_chicken_menu + total_price_fish_menu + total_price_vege_menu
desert = 0.2 * total_cost
final_cost = total_cost + desert + delivery

print(final_cost)

