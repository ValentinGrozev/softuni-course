number = int(input())

count_number_1 = 0
count_number_2 = 0
count_number_3 = 0
count_number_4 = 0
count_number_5 = 0
percent_1 = 0
percent_2 = 0
percent_3 = 0
percent_4 = 0
percent_5 = 0

for number in range(1, number+1):
    current_number = int(input())
    if current_number < 200:
        count_number_1 += 1
    elif 200 <= current_number <= 399:
        count_number_2 += 1
    elif 400 <= current_number <= 599:
        count_number_3 += 1
    elif 600 <= current_number <= 799:
        count_number_4 += 1
    elif current_number >= 800:
        count_number_5 += 1

percent_1 = (count_number_1 / number) * 100
percent_2 = (count_number_2 / number) * 100
percent_3 = (count_number_3 / number) * 100
percent_4 = (count_number_4 / number) * 100
percent_5 = (count_number_5 / number) * 100
print(f"{percent_1:.2f}%")
print(f"{percent_2:.2f}%")
print(f"{percent_3:.2f}%")
print(f"{percent_4:.2f}%")
print(f"{percent_5:.2f}%")











