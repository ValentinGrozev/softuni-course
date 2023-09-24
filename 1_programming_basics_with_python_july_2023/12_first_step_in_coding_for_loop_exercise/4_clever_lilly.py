lilly_age = int(input())
price_for_washing_machine = float(input())
price_for_toy = int(input())

saved_money = 0
toys_counter = 0
money_in_brother = 0

for year in range(1, lilly_age+1):
    if year % 2 == 0:
        saved_money += (year / 2) * 10
        money_in_brother += 1
    else:
        toys_counter += 1

money_from_toys = toys_counter * price_for_toy
all_money_saved = saved_money + money_from_toys - money_in_brother
diff = abs(all_money_saved - price_for_washing_machine)

if all_money_saved >= price_for_washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")

