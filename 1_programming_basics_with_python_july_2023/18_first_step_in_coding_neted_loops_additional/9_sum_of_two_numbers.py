start_of_interval = int(input())
final_of_interval = int(input())
magical_number = int(input())

combination_counts = 0
flag = False

for number_1 in range(start_of_interval, final_of_interval + 1):
    for number_2 in range(start_of_interval, final_of_interval + 1):
        combination_counts += 1
        if number_1 + number_2 == magical_number:
            flag = True
            break
    if flag:
        break

if flag:
    print(f"Combination N:{combination_counts} ({number_1} + {number_2} = {magical_number})")
else:
    print(f"{combination_counts} combinations - neither equals {magical_number}")
