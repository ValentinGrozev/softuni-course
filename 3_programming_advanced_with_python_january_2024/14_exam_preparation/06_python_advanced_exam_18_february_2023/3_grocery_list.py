def shop_from_grocery_list(budget, products_to_buy, *product_name_and_price):
    bought_products = []
    products_needed_to_buy = len(products_to_buy)

    for product, price in product_name_and_price:
        if budget >= float(price):
            if product in products_to_buy and product not in bought_products:
                budget -= float(price)
                bought_products.append(product)
            else:
                continue
        else:
            break

    result_to_print = ''

    if len(bought_products) == products_needed_to_buy:
        result_to_print += f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        missed_products = set(products_to_buy).difference(set(bought_products))
        result_to_print += f"You did not buy all the products. Missing products: {', '.join(missed_products)}."

    return result_to_print


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
