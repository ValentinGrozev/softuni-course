number_of_commands = int(input())

parking_place_validation = {}

for command in range(number_of_commands):
    parking_validation = input().split()
    parking_action = parking_validation[0]
    if parking_action == "register":
        name_of_driver = parking_validation[1]
        driver_license_plate = parking_validation[2]
        if name_of_driver not in parking_place_validation:
            parking_place_validation[name_of_driver] = driver_license_plate
            print(f"{name_of_driver} registered {driver_license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {driver_license_plate}")
    elif parking_action == "unregister":
        name_of_driver = parking_validation[1]
        if name_of_driver not in parking_place_validation:
            print(f"ERROR: user {name_of_driver} not found")
        else:
            del parking_place_validation[name_of_driver]
            print(f"{name_of_driver} unregistered successfully")

for key, value in parking_place_validation.items():
    print(f"{key} => {value}")
