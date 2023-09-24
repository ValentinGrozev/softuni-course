number = int(input())

current_sum = 0

for special_number in range(1, number + 1):
    current_sum = 0
    digits = special_number

    while digits > 0:
        current_sum += digits % 10
        digits = int(digits / 10)
    if current_sum == 5 or current_sum == 7 or current_sum == 11:
        print(f"{special_number} -> True")
    else:
        print(f"{special_number} -> False")