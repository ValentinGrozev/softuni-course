kilometers = int(input())
time_of_a_day = str(input())

z = "day"
y = "night"

if time_of_a_day == z:
    if kilometers < 20:
        taxi_price = 0.70 + 0.79 * kilometers
        print(f"{taxi_price:.2f}")
    elif 20 <= kilometers < 100:
        taxi_price = 0.70 + 0.79 * kilometers
        bus_price = 0.09 * kilometers
        if taxi_price > bus_price:
            print(f"{bus_price:.2f}")
        else:
            print(f"{taxi_price:.2f}")
    elif kilometers >= 100:
        taxi_price = 0.70 + 0.79 * kilometers
        bus_price = 0.09 * kilometers
        train_price = 0.06 * kilometers
        print(f"{train_price:.2f}")

if time_of_a_day == y:
    if kilometers < 20:
        taxi_price = 0.70 + 0.90 * kilometers
        print(f"{taxi_price:.2f}")
    elif 20 <= kilometers < 100:
        taxi_price = 0.70 + 0.90 * kilometers
        bus_price = 0.09 * kilometers
        if taxi_price > bus_price:
            print(f"{bus_price:.2f}")
        else:
            print(f"{taxi_price:.2f}")
    elif kilometers >= 100:
        taxi_price = 0.70 + 0.90 * kilometers
        bus_price = 0.09 * kilometers
        train_price = 0.06 * kilometers
        print(f"{train_price:.2f}")

