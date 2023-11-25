import re

places_on_the_map = input()
pattern = r"([=|\/])(([A-Z]{1})([A-Za-z]{2,}))(\1)"
matches = re.findall(pattern, places_on_the_map)

total_points = 0
destination_list = []

for match in matches:
    place = match[1]
    points = len(place)
    total_points += int(points)
    destination_list.append(place)

print(f"Destinations: {', '.join(destination_list)}")
print(f"Travel Points: {total_points}")
