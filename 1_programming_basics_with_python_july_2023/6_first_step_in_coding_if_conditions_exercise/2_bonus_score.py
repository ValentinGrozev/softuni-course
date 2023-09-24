number = int(input())

additional_points = 0

if number <= 100:
    additional_points = 5

elif number <= 1000:
    additional_points = 0.2 * number

else:
    additional_points = 0.1 * number

if number % 2 ==0:
    additional_points = additional_points + 1

elif number % 10 ==5:
    additional_points = additional_points + 2

print(additional_points)
print(number+additional_points)
