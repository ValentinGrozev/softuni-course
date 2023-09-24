city = input()
volume_sells = float(input())

price = 0
if city == "Sofia":
    if 0 <= volume_sells <= 500:
        price = volume_sells * 0.05
        print(f"{price:.2f}")
    elif 500 < volume_sells <= 1000:
        price = volume_sells * 0.07
        print(f"{price:.2f}")
    elif 1000 < volume_sells <= 10000:
        price = volume_sells * 0.08
        print(f"{price:.2f}")
    elif volume_sells > 10000:
        price = volume_sells * 0.12
        print(f"{price:.2f}")
    elif volume_sells < 0:
        print("error")
elif city == "Varna":
    if 0 <= volume_sells <= 500:
        price = volume_sells * 0.045
        print(f"{price:.2f}")
    elif 500 < volume_sells <= 1000:
        price = volume_sells * 0.075
        print(f"{price:.2f}")
    elif 1000 < volume_sells <= 10000:
        price = volume_sells * 0.10
        print(f"{price:.2f}")
    elif volume_sells > 10000:
        price = volume_sells * 0.13
        print(f"{price:.2f}")
    elif volume_sells < 0:
        print("error")
elif city == "Plovdiv":
    if 0 <= volume_sells <= 500:
        price = volume_sells * 0.055
        print(f"{price:.2f}")
    elif 500 < volume_sells <= 1000:
        price = volume_sells * 0.08
        print(f"{price:.2f}")
    elif 1000 < volume_sells <= 10000:
        price = volume_sells * 0.12
        print(f"{price:.2f}")
    elif volume_sells > 10000:
        price = volume_sells * 0.145
        print(f"{price:.2f}")
    elif volume_sells < 0:
        print("error")
else:
    print("error")


