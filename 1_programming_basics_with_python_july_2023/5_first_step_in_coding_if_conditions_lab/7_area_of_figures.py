from math import pi

type_figure = input()

area = 0

if type_figure == "square":
    x = float(input())
    area = x * x

elif type_figure == "rectangle":
    x = float(input())
    y = float(input())
    area = x * y

elif type_figure == "circle":
    r = float(input())
    area = pi * r * r

elif type_figure == "triangle":
    a = float(input())
    h = float(input())
    area = 1 / 2 * a * h

print(f"{area:.3f}")