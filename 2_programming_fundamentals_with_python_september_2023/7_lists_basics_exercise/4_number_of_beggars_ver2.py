money_offers_as_string = input().split(", ")
number_of_beggars = int(input())

money_offers_as_int = []

for current_money in money_offers_as_string:
    money_offers_as_int.append(int(current_money))

final_sum = []
start_index = 0
while start_index < number_of_beggars:
    current_beggar_sum = 0
    for current_index in range (start_index, len(money_offers_as_int), number_of_beggars):
        current_beggar_sum += money_offers_as_int[current_index]
    final_sum.append(current_beggar_sum)
    start_index += 1

print(final_sum)
