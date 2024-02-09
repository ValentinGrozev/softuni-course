from collections import deque

milligrams_of_caffeine = [int(caffeine) for caffeine in input().split(", ")]
energy_drinks = deque([int(drink) for drink in input().split(", ")])

caffeine_drank = 0
MAXIMUM_CAFFEINE = 300

while milligrams_of_caffeine and energy_drinks:
    current_milligrams_of_caffeine = milligrams_of_caffeine.pop()
    current_energy_drink = energy_drinks.popleft()

    result = current_milligrams_of_caffeine * current_energy_drink

    if caffeine_drank + result <= MAXIMUM_CAFFEINE:
        caffeine_drank += result
    else:
        energy_drinks.append(current_energy_drink)
        if caffeine_drank - 30 >= 0:
            caffeine_drank -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join(str(drink) for drink in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {caffeine_drank} mg caffeine.")
