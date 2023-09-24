chicken_menu = int(input())
fish_menu = int(input())
vege_menu = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
vege_menu_price = 8.15
order_price = 2.50

chicken_menu_cost = chicken_menu * chicken_menu_price
fish_menu_cost = fish_menu * fish_menu_price
vege_menu_cost = vege_menu * vege_menu_price
desert_cost = 0.2 * (chicken_menu_cost + fish_menu_cost + vege_menu_cost)

total_cost = round(chicken_menu_cost + fish_menu_cost + vege_menu_cost + desert_cost + order_price,2)

print(total_cost)