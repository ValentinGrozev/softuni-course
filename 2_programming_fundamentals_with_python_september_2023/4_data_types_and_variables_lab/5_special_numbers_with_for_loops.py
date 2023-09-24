number = int(input())

current_sum = 0

for special_number in range(1, number + 1):
    for digit in str(special_number):
        current_sum += int(digit)
    if current_sum == 5 or current_sum == 7 or current_sum == 11:
        print(f"{special_number} -> True")
    else:
        print(f"{special_number} -> False")
    current_sum = 0

