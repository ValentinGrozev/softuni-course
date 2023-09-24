length = float(input())
width = float(input())

waste_places_department = 2
waste_places_door = 1
actual_width = width - 1

work_places_per_row = actual_width // 0.7
rows = length // 1.2

work_places = (work_places_per_row * rows) - waste_places_department - waste_places_door

print(work_places)
