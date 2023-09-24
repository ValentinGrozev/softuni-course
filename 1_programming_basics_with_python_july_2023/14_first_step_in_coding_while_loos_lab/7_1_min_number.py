import sys

number = input()

min_number = sys.maxsize

while number != "Stop":
    number = int(number)

    if number < min_number:
        min_number = number

    number = input()

    if number == "Stop":
        break

print(min_number)
