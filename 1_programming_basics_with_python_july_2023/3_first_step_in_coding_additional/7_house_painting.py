x_side_house = float(input())
y_side_house = float(input())
h_height_house = float(input())

squares_paint_with_liter_green_paint = 3.4
squares_paint_with_liter_red_paint = 4.3

door_without_paint = 2.4
window_without_paint = 2.25

side_walls = x_side_house * y_side_house
front_walls = x_side_house * x_side_house
area_green = side_walls * 2 + front_walls * 2 - door_without_paint - 2 * window_without_paint
green_paint_litres = area_green / squares_paint_with_liter_green_paint

side_roof = x_side_house * y_side_house
front_roof = (x_side_house * h_height_house * 2) / 2
area_roof = side_roof * 2 + front_roof
red_paint_litres = area_roof / squares_paint_with_liter_red_paint

print(f"{green_paint_litres:.2f}")
print(f"{red_paint_litres:.2f}")

