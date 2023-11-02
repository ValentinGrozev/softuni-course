products = input().split()
products_dict = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = products[i + 1]
    products_dict[key] = value

searched_products = input().split()

for product in searched_products:
    if product in products_dict.keys():
        print(f"We have {products_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
