number = input()

is_found = False

for a in range(1, 10):
    for b in range(9, a, -1):
        for c in range(0, 10):
            for d in range(9, c, -1):
                if (a + b + c + d) == (a * b * c * d) and number[-1] == "5":
                    print(f"{a}{b}{c}{d}")
                    is_found = True
                    break
                elif (a * b * c * d) // (a + b + c + d) == 3 and int(number) % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    is_found = True
                    break

            if is_found:
                break
        if is_found:
            break
    if is_found:
        break

else:
    print("Nothing found")
