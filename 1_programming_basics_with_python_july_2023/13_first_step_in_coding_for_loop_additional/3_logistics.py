number_of_cargos = int(input())

van_all_weight = 0
truck_all_weight = 0
train_all_weight = 0

for _ in range(number_of_cargos):
    weight = int(input())
    if weight <= 3:
        van_all_weight += weight
    elif 3 < weight <= 11:
        truck_all_weight += weight
    elif weight > 11:
        train_all_weight += weight

price_for_van_weight = van_all_weight * 200
price_for_truck_weight = truck_all_weight * 175
price_for_train_weight = train_all_weight * 120

all_weight = van_all_weight + truck_all_weight + train_all_weight
price_for_all = price_for_van_weight + price_for_truck_weight + price_for_train_weight

average_price = price_for_all / all_weight
percent_van = (van_all_weight / all_weight) * 100
percent_truck = (truck_all_weight / all_weight) * 100
percent_train = (train_all_weight / all_weight) * 100

print(f"{average_price:.2f}")
print(f"{percent_van:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")
