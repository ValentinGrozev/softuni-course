command = input()
products_in_stock = {}

while command != "statistics":
    product = command.split(":")
    key = product[0]
    value = int(product[1])
    if key in products_in_stock.keys():
        products_in_stock[key] += value
    else:
        products_in_stock[key] = value

    command = input()

total_products = len(products_in_stock.keys())
total_quantity = sum(products_in_stock.values())

print("Products in stock:")
for keys, values in products_in_stock.items():
    print(f"- {keys}: {values}")
print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")
