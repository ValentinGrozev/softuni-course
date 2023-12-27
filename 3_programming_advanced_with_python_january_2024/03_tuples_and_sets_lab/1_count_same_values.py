numbers = tuple(float(x) for x in input().split())
unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
        print(f"{number} - {numbers.count(number)} times")
