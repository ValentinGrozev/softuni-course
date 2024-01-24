from functools import reduce


def operate(symbol, *args):
    if symbol == "+":
        return reduce(lambda x, y: x + y, args)
    elif symbol == "-":
        return reduce(lambda x, y: x - y, args)
    elif symbol == "*":
        return reduce(lambda x, y: x * y, args)
    elif symbol == "/":
        return reduce(lambda x, y: x / y, args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
