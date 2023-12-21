number_count = int(input())
numbers_sum = 0

for current_number in range(number_count):
    number = int(input())
    numbers_sum += number

average_sum = numbers_sum / number_count
print(f"{average_sum:.2f}")
