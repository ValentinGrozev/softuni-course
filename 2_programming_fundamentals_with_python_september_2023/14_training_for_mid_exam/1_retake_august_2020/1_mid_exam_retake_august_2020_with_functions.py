def is_special(price_without_taxes):
    taxes_price = 0.2 * price_without_taxes
    all_price = price_without_taxes + taxes_price
    all_price = 0.9 * all_price
    return taxes_price, all_price


def is_regular(price_without_taxes):
    taxes_price = 0.2 * price_without_taxes
    all_price = price_without_taxes + taxes_price
    return taxes_price, all_price


price = input()

total_price = 0

while True:
    if price == "special":
        break
    if price == "regular":
        break
    price = float(price)
    if price < 0:
        print("Invalid price!")
    else:
        total_price += price

    price = input()

if total_price == 0:
    print("Invalid order!")

elif price == "special":
    taxes, final_price = is_special(total_price)
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {final_price:.2f}$")
else:
    taxes, final_price = is_regular(total_price)
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {final_price:.2f}$")