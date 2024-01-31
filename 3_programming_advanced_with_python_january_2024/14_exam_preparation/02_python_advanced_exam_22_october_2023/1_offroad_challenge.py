from collections import deque

fuel_quantity = [int(fuel) for fuel in input().split()]
consumption_index_of_fuel = deque([int(fuel) for fuel in input().split()])
altitude = deque([int(fuel) for fuel in input().split()])

altitude_reached = 0

insufficient_fuel = False
top_reached = False

while fuel_quantity and consumption_index_of_fuel:
    current_fuel = fuel_quantity.pop()
    current_consumption_index = consumption_index_of_fuel.popleft()
    current_altitude = altitude.popleft()

    if current_fuel - current_consumption_index >= current_altitude:
        altitude_reached += 1
    else:
        insufficient_fuel = True
        break

    if not altitude:
        top_reached = True
        break

if altitude_reached >= 0:
    for altitude in range(1, altitude_reached + 1):
        print(f"John has reached: Altitude {altitude}")
    if not top_reached:
        print(f"John did not reach: Altitude {altitude_reached + 1}")

if insufficient_fuel and altitude_reached > 0:
    print("John failed to reach the top.")
    print(f"Reached altitudes: Altitude "
          f"{', Altitude '.join(str(altitude) for altitude in range(1, altitude_reached + 1))}", end=" ")
elif insufficient_fuel and altitude_reached == 0:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")

if top_reached:
    print("John has reached all the altitudes and managed to reach the top!")
