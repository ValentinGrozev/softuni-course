n = int(input())
result = 0
count = 0

for i in range(0, n + 1):
    for j in range(0, n + 1):
        for k in range(0, n + 1):
            result = i + j + k
            if result == n:
                count += 1
print(count)


