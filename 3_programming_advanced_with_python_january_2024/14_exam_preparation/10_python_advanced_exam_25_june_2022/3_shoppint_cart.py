def shopping_cart(*meals_information):
    max_products = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2}

    meals_and_products = {
        "Soup": [],
        "Pizza": [],
        "Dessert": []}

    products_in_cart = False

    for type_of_meals_and_products in meals_information:
        if type_of_meals_and_products == "Stop":
            break
        else:
            products_in_cart = True
            meal = type_of_meals_and_products[0]
            product = type_of_meals_and_products[1]
            if len(meals_and_products[meal]) < max_products[meal] and product not in meals_and_products[meal]:
                meals_and_products[meal].append(product)

    if not products_in_cart:
        return f"No products in the cart!"
    else:
        sorted_meals_and_products = sorted(meals_and_products.items(), key=lambda x: (-len(x[1]), x[0]))

        result = ""

        for current_meal, products in sorted_meals_and_products:
            result += f"{current_meal}:\n"
            for current_product in sorted(products):
                result += f" - {current_product}\n"

        return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
