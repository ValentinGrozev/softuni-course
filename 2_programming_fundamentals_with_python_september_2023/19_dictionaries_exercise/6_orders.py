order = input()

orders_details = {}

while order != "buy":
    order = order.split()
    product_name = order[0]
    product_price = float(order[1])
    product_quantity = int(order[2])

    if product_name not in orders_details:
        orders_details[product_name] = [product_price, product_quantity]
    else:
        orders_details[product_name][0] = product_price
        orders_details[product_name][1] += product_quantity

    order = input()

for product_name, value in orders_details.items():
    final_price = value[0] * value[1]
    print(f"{product_name} -> {final_price:.2f}")
