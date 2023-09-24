number = int(input())

current_number = 1
break_flag = False

for row in range(1, number + 1):
    for column in range(1, row + 1):
        if current_number > number:
            break_flag = True
            break
        print(str(current_number), end=" ")
        current_number += 1

    if break_flag:
        break
    print()


