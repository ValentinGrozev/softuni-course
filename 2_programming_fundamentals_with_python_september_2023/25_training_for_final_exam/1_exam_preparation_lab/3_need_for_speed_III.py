number_of_cars_to_obtain = int(input())
car_dict = {}

for current_car in range(number_of_cars_to_obtain):
    car_information = input().split("|")
    car_model = car_information[0]
    mileage = int(car_information[1])
    fuel = int(car_information[2])
    if car_model not in car_dict:
        car_dict[car_model] = {"mileage": 0, "fuel": 0}
    car_dict[car_model]["mileage"] += mileage
    car_dict[car_model]["fuel"] += fuel

command = input().split(" : ")

while command[0] != "Stop":
    action = command[0]
    if action == "Drive":
        car_name = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if car_dict[car_name]["fuel"] >= fuel:
            car_dict[car_name]["mileage"] += distance
            car_dict[car_name]["fuel"] -= fuel
            print(f"{car_name} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if car_dict[car_name]["mileage"] >= 100000:
                print(f"Time to sell the {car_name}!")
                car_dict.pop(car_name)
        else:
            print(f"Not enough fuel to make that ride")
    elif action == "Refuel":
        car_name = command[1]
        fuel = int(command[2])
        current_car_fuel = car_dict[car_name]["fuel"]
        car_dict[car_name]["fuel"] += fuel
        if car_dict[car_name]["fuel"] > 75:
            car_dict[car_name]["fuel"] = 75
            refuel = 75 - current_car_fuel
            print(f"{car_name} refueled with {refuel} liters")
        else:
            print(f"{car_name} refueled with {fuel} liters")
    elif action == "Revert":
        car_name = command[1]
        mileage = int(command[2])
        car_dict[car_name]["mileage"] -= mileage
        if car_dict[car_name]["mileage"] < 10000:
            car_dict[car_name]["mileage"] = 10000
        else:
            print(f"{car_name} mileage decreased by {mileage} kilometers")

    command = input().split(" : ")

for current_car, car_information in car_dict.items():
    print(f"{current_car} -> Mileage: {car_dict[current_car]['mileage']}"
          f" kms, Fuel in the tank: {car_dict[current_car]['fuel']} lt.")
