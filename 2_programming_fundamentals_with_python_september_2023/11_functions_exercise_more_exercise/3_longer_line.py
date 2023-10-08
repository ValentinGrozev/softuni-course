def longer_line(line_1_x_1, line_1_y_1, line_1_x_2, line_1_y_2, line_2_x_1, line_2_y_1, line_2_x_2, line_2_y_2):
    if abs(line_1_x_1) + abs(line_1_y_1) + abs(line_1_x_2) + abs(line_1_y_2) >= abs(line_2_x_1)\
            + abs(line_2_y_1) + abs(line_2_x_2) + abs(line_2_y_2):
        if abs(line_1_x_1) + abs(line_1_y_1) <= abs(line_1_x_2) + abs(line_1_y_2):
            return f"({int(line_1_x_1)}, {int(line_1_y_1)})({int(line_1_x_2)}, {int(line_1_y_2)})"
        else:
            return f"({int(line_1_x_2)}, {int(line_1_y_2)})({int(line_1_x_1)}, {int(line_1_y_1)})"
    else:
        if abs(line_2_x_1) + abs(line_2_y_1) <= abs(line_2_x_2) + abs(line_2_y_2):
            return f"({int(line_2_x_1)}, {int(line_2_y_1)})({int(line_2_x_2)}, {int(line_2_y_2)})"
        else:
            return f"({int(line_2_x_2)}, {int(line_2_y_2)})({int(line_2_x_1)}, {int(line_2_y_1)})"


value_for_x_1_line_1 = float(input())
value_for_y_1_line_1 = float(input())
value_for_x_2_line_1 = float(input())
value_for_y_2_line_1 = float(input())
value_for_x_1_line_2 = float(input())
value_for_y_1_line_2 = float(input())
value_for_x_2_line_2 = float(input())
value_for_y_2_line_2 = float(input())
print(longer_line(value_for_x_1_line_1, value_for_y_1_line_1, value_for_x_2_line_1, value_for_y_2_line_1,
                  value_for_x_1_line_2, value_for_y_1_line_2, value_for_x_2_line_2, value_for_y_2_line_2))
