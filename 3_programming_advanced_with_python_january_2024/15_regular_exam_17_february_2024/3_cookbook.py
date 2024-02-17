def cookbook(*foods_and_meals):
    cook_book = {}

    for recipe_name, cuisine, products in foods_and_meals:
        if cuisine not in cook_book:
            cook_book[cuisine] = [(recipe_name, products)]
        else:
            cook_book[cuisine] += [(recipe_name, products)]

    sorted_cook_book = sorted(cook_book.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''

    for cuisine, meals_and_products in sorted_cook_book:
        result += f"{cuisine} cuisine contains {len(meals_and_products)} recipes:\n"
        for meal, products in sorted(meals_and_products):
            result += f"  * {meal} -> Ingredients: {', '.join(products)}\n"

    return result


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
