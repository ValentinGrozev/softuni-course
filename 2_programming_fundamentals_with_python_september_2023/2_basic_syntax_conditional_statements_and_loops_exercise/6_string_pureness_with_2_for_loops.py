number_of_strings = int(input())
flag = False

for i in range(number_of_strings):
    string = input()
    for index in range(len(string)):
        if string[index] == "." or string[index] == "," or string[index] == "_":
            flag = True
            break
        else:
            continue

    if flag:
        print(f"{string} is not pure!")
        flag = False
    else:
        print(f"{string} is pure.")