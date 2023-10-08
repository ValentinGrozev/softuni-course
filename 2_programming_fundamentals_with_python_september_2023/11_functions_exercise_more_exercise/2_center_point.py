from math import floor


def closet_points_to_center(x_first, y_first, x_second, y_second):
    if abs(x_first) + abs(y_first) <= abs(x_second) + abs(y_second):
        x = floor(x_first)
        y = floor(y_first)
    else:
        x = floor(x_second)
        y = floor(y_second)
    return f"({x}, {y})"


value_for_x_1 = float(input())
value_for_y_1 = float(input())
value_for_x_2 = float(input())
value_for_y_2 = float(input())
print(closet_points_to_center(value_for_x_1, value_for_y_1, value_for_x_2, value_for_y_2))