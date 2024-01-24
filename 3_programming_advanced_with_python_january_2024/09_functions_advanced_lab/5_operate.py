def operate(symbol, *args):
    def add():
        return sum(args)

    def subtract():
        result = 0
        for index, arg in enumerate(args):
            if index == 0:
                result += arg
            else:
                result -= arg
        return result

    def multiply():
        result = 1
        for arg in args:
            result *= arg
        return result

    def division():
        result = 0
        for index, arg in enumerate(args):
            if index == 0:
                result += arg
            else:
                result /= arg
        return result

    if symbol == "+":
        return add()
    elif symbol == "-":
        return subtract()
    elif symbol == "*":
        return multiply()
    elif symbol == "/":
        return division()


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))