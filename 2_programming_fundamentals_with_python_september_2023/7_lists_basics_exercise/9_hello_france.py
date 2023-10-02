item_prices = input()
budget = float(input())

budget_left = budget
train_ticket_price = 150
bought_items_price_list = []
money_from_sold_items_list = []
profit = 0

item_prices_list = item_prices.split("|")

for prices in item_prices_list:
    [type_of_product, price] = prices.split("->")
    if type_of_product == "Clothes":
        if budget_left >= float(price) and 0 < float(price) <= 50:
            bought_items_price_list.append(float(price))
            budget_left -= float(price)
            resell_price = (float(price) + 0.4 * float(price))
            money_from_sold_items_list.append(resell_price)

    elif type_of_product == "Shoes":
        if budget_left >= float(price) and 0 < float(price) <= 35:
            bought_items_price_list.append(float(price))
            budget_left -= float(price)
            resell_price = (float(price) + 0.4 * float(price))
            money_from_sold_items_list.append(resell_price)

    elif type_of_product == "Accessories" and 0 < float(price) <= 20.50:
        if budget_left >= float(price):
            bought_items_price_list.append(float(price))
            budget_left -= float(price)
            resell_price = (float(price) + 0.4 * float(price))
            money_from_sold_items_list.append(resell_price)

for money in money_from_sold_items_list:
    print(f"{money:.2f}", end=" ")

final_budget = budget_left + sum(money_from_sold_items_list)
profit = sum(money_from_sold_items_list) - sum(bought_items_price_list)

print(f"\nProfit: {profit:.2f}")

if final_budget > train_ticket_price:
    print(f"Hello, France!")
else:
    print("Not enough money.")