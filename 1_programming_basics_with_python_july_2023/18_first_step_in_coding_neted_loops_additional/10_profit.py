number_of_one_leva_coins = int(input())
number_of_two_leva_coins = int(input())
number_of_five_leva_banknote = int(input())
final_sum = int(input())

for first in range(0, number_of_one_leva_coins + 1):
    for second in range(0, number_of_two_leva_coins + 1):
        for third in range(0, number_of_five_leva_banknote + 1):
            if first * 1 + second * 2 + third * 5 == final_sum:
                print(f"{first} * 1 lv. + {second} * 2 lv. + {third} * 5 lv. = {final_sum} lv.")

