divisor = int(input())
boundary = int(input())

maximum_number = 0

for number in range(divisor, boundary + 1):
    if number % divisor == 0:
        maximum_number = number

print(maximum_number)

