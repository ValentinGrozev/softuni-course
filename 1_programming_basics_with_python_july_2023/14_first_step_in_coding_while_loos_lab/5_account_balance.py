total_money = 0
deposits = input()

while deposits != "NoMoreMoney":
    deposits = float(deposits)

    if deposits >= 0:
        print(f"Increase: {deposits:.2f}")
        total_money += deposits
        deposits = input()

    elif deposits < 0:
        print("Invalid operation!")
        break

total_money = total_money
print(f"Total: {total_money:.2f}")





