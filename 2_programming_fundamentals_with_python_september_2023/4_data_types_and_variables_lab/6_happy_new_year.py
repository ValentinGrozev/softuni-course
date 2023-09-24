import sys

number = int(input())
current_sum = 0
is_not_unique = False

for year in range(number+1, sys.maxsize):
    year = str(year)
    for first_index in range(0, len(year)):
        for all_other_index in range(first_index + 1, len(year)):
            if year[first_index] == year[all_other_index]:
                is_not_unique = True
                break
        if is_not_unique:
            break

    if is_not_unique:
        is_not_unique = False
    else:
        print(year)
        break


