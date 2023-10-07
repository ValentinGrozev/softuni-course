def total_price(product: str, quantity_of_product: int) -> float:
    result = 0
    if product == "coffee":
        price_for_coffe = 1.50
        result = price_for_coffe * quantity_of_product
    elif product == "coke":
        price_for_coke = 1.40
        result = price_for_coke * quantity_of_product
    elif product == "water":
        price_for_water = 1.00
        result = price_for_water * quantity_of_product
    elif product == "snacks":
        price_for_snacks = 2.00
        result = price_for_snacks * quantity_of_product
    return result


product_name = input()
quantity = int(input())
print(f"{total_price(product_name, quantity):.2f}")