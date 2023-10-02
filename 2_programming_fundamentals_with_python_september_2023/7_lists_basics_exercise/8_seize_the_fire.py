fires = input()
water = int(input())

fire_list = fires.split("#")
total_effort = 0
total_fire = 0
water_left = water
fire_levels = []

for element in fire_list:
    [lvl, number] = element.split(" = ")
    if lvl == "High" and 81 <= int(number) <= 125:
        if water_left >= 0 and water_left >= int(number):
            water_left -= int(number)
            total_fire += int(number)
            total_effort += 0.25 * int(number)
            fire_levels.append(int(number))
    elif lvl == "Medium" and 51 <= int(number) <= 80:
        if water_left >= 0 and water_left >= int(number):
            water_left -= int(number)
            total_fire += int(number)
            total_effort += 0.25 * int(number)
            fire_levels.append(int(number))
    elif lvl == "Low" and 1 <= int(number) <= 50:
        if water_left >= 0 and water_left >= int(number):
            water_left -= int(number)
            total_fire += int(number)
            total_effort += 0.25 * int(number)
            fire_levels.append(int(number))

print("Cells:")
for fire in fire_levels:
    print(f" - {fire}")
print(f"Effort: {total_effort:.2f} \nTotal Fire: {total_fire}")