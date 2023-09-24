import sys

number = input()

min_number = sys.maxsize

while True:
    if number == "Stop":
        break
    else:
        number = int(number)

        if number < min_number:
            min_number = number

        number = input()

print(min_number)