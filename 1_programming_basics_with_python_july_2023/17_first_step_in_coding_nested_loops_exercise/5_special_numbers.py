number = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            for l in range(1, 10):
                if number % i == 0 and number % j == 0 and number % k == 0 and number % l == 0:
                    print(f"{i}{j}{k}{l}", end=" ")
