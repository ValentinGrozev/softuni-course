number = input()

lst = list(number)
lst.sort(reverse=True)

for i in lst:
    print(i, end="")