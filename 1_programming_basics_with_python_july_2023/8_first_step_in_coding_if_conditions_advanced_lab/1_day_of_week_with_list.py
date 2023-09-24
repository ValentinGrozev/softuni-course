number = int(input())

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
number = number - 1

if 0 <= number <= 7:
    print(days[number])
else:
    print("Error")