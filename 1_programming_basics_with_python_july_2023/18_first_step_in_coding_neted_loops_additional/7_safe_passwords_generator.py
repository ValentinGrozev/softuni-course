first_symbol_a = int(input())
second_symbol_b = int(input())
maximum_passwords = int(input())
password = 0
flag = False

for A in range(35, 55 + 1):
    for B in range(64, 96 + 1):
        for x in range(1, first_symbol_a + 1):
            for y in range(1, second_symbol_b + 1):
                password += 1
                if password > maximum_passwords:
                    flag = True
                    break
                print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}" "|", end="")
                A = A + 1
                if A == 56:
                    A = 35
                B = B + 1
                if B == 97:
                    B = 64
            if flag:
                break
        flag = True
        if flag:
            break
    if flag:
        break
