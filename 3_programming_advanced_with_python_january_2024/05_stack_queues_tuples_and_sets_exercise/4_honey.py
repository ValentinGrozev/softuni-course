from collections import deque


def addition(honey_made, bee, current_nectar):
    honey_made += abs(bee + current_nectar)
    return honey_made


def subtract(honey_made, bee, current_nectar):
    honey_made += abs(bee - current_nectar)
    return honey_made


def multiply(honey_made, bee, current_nectar):
    honey_made += abs(bee * current_nectar)
    return honey_made


def division(honey_made, bee, current_nectar):
    if current_nectar == 0:
        pass
    else:
        honey_made += abs(bee / current_nectar)
    return honey_made


def print_message(honey_made, working_bees, nectar):
    print(f"Total honey made: {honey_made}")
    if working_bees:
        print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
    if nectar:
        print(f"Nectar left: {', '.join(str(x) for x in nectar)}")


def pop_nectar(nectar):
    nectar.pop()


def main():
    working_bees = deque([int(x) for x in input().split()])
    nectar = [int(x) for x in input().split()]
    symbols = deque(input().split())

    honey_made = 0

    while working_bees and nectar:
        if working_bees[0] <= nectar[-1]:
            for _ in symbols:
                current_symbol = symbols.popleft()
                bee = working_bees.popleft()
                current_nectar = nectar.pop()
                if current_symbol == "+":
                    honey_made = addition(honey_made, bee, current_nectar)
                elif current_symbol == "-":
                    honey_made = subtract(honey_made, bee, current_nectar)
                elif current_symbol == "*":
                    honey_made = multiply(honey_made, bee, current_nectar)
                elif current_symbol == "/":
                    honey_made = division(honey_made, bee, current_nectar)
                break
        else:
            pop_nectar(nectar)

    print_message(honey_made, working_bees, nectar)


main()
