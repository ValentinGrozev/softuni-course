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

if price == "special":
    taxes = (1.20 * total_price) - total_price
    final_price = total_price + taxes
    final_price = 0.9 * final_price
else:
    taxes = (1.20 * total_price) - total_price
    final_price = total_price + taxes

if total_price == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {final_price:.2f}$")