def rectangle(length, width):
    if isinstance(length, int) and isinstance(width, int):
        def area():
            return f"Rectangle area: {length * width}"

        def perimeter():
            return f"Rectangle perimeter: {2 * (length + width)}"
        return f"{area()}\n{perimeter()}"
    else:
        return "Enter valid values!"


print(rectangle(2, 10))
print(rectangle('2', 10))
