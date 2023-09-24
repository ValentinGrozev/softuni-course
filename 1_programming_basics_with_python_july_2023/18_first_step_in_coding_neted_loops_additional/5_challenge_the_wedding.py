man_count = int(input())
women_count = int(input())
maximum_number_of_tables = int(input())

date_counter = 0
flag = False

for man in range(1, man_count + 1):
    for women in range(1, women_count + 1):
        date_counter += 1
        if date_counter == maximum_number_of_tables:
            flag = True
            print(f"({man} <-> {women})", end=" ")
            break
        else:
            print(f"({man} <-> {women})", end=" ")
    if flag:
        break









