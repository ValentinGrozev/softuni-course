control_number = int(input())
counter = 0
counter_fourth_number = 0
fourth_number = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d and (a * b) + (c * d) == control_number:
                    counter += 1
                    counter_fourth_number = f"{a}{b}{c}{d}"
                    print(f"{a}{b}{c}{d}", end=' ')
                if counter == 4:
                    fourth_number = counter_fourth_number

if counter < 4:
    print("\nNo!")
else:
    print(f"\nPassword: {fourth_number}")
