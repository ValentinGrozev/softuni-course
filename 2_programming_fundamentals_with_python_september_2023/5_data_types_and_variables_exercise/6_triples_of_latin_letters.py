num = int(input())

for j in range(0, num):
    for k in range(0, num):
        for l in range(0, num):
            print(f"{chr(97 + j)}{chr(97 + k)}{chr(97 + l)}")
