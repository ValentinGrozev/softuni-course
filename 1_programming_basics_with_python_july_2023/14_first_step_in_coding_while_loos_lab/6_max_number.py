import sys

number = input()

max_number = -sys.maxsize

while True:
    if number == "Stop":
        break
    else:
        number = int(number)

        if number > max_number:
            max_number = number

        number = input()
print(max_number)




