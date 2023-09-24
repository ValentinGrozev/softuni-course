number_of_orders = int(input())
final_price = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_needed_per_day <= 2000:
        total_price = price_per_capsule * days * capsules_needed_per_day
        final_price += total_price
        print(f"The price for the coffee is: ${total_price:.2f}")
    else:
        continue

print(f"Total: ${final_price:.2f}")


