start_of_interval = int(input())
final_of_interval = int(input())
magic_number = int(input())

combination_counter = 0
flag_break = False
i = 0
j = 0

for i in range(start_of_interval, final_of_interval + 1):
    for j in range(start_of_interval, final_of_interval + 1):
        combination_counter += 1
        if i + j == magic_number:
            flag_break = True
            break
    if flag_break:
        break

if flag_break:
    print(f"Combination N:{combination_counter} ({i} + {j} = {magic_number})")
else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")
