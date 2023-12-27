number_of_commands = int(input())

parking_lot_record = set()

for car in range(number_of_commands):
    direction, car_license = input().split(", ")
    if direction == "IN":
        parking_lot_record.add(car_license)
    elif direction == "OUT":
        if parking_lot_record:
            parking_lot_record.remove(car_license)

if parking_lot_record:
    for current_car_licence in parking_lot_record:
        print(current_car_licence)
else:
    print("Parking Lot is Empty")
