number_of_moves = int(input())

result = 0
range_0_to_9 = 0
range_10_to_19 = 0
range_20_to_29 = 0
range_30_to_39 = 0
range_40_to_50 = 0
invalid = 0


for _ in range(number_of_moves):
    new_number = int(input())
    if 0 <= new_number <= 9:
        result += 0.2 * new_number
        range_0_to_9 += 1
    elif 10 <= new_number <= 19:
        result += 0.3 * new_number
        range_10_to_19 += 1
    elif 20 <= new_number <= 29:
        result += 0.4 * new_number
        range_20_to_29 += 1
    elif 30 <= new_number <= 39:
        result += 50
        range_30_to_39 += 1
    elif 40 <= new_number <= 50:
        result += 100
        range_40_to_50 += 1
    elif new_number < 0 or new_number > 50:
        result = result / 2
        invalid += 1

result = result
percent_0_to_9 = (range_0_to_9 / number_of_moves) * 100
percent_10_to_19 = (range_10_to_19 / number_of_moves) * 100
percent_20_to_29 = (range_20_to_29 / number_of_moves) * 100
percent_30_to_39 = (range_30_to_39 / number_of_moves) * 100
percent_40_to_50 = (range_40_to_50 / number_of_moves) * 100
percent_invalid = (invalid / number_of_moves) * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {percent_0_to_9:.2f}%")
print(f"From 10 to 19: {percent_10_to_19:.2f}%")
print(f"From 20 to 29: {percent_20_to_29:.2f}%")
print(f"From 30 to 39: {percent_30_to_39:.2f}%")
print(f"From 40 to 50: {percent_40_to_50:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")
