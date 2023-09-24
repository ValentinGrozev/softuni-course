from math import floor, ceil

magnolias_count = int(input())
hyacinth_count = int(input())
rose_count = int(input())
cactus_count = int(input())
price_for_gift = float(input())

magnolias_price = 3.25
hyacinth_price = 4
rose_price = 3.50
cactus_price = 8

turnover = magnolias_count * magnolias_price + hyacinth_count * hyacinth_price + rose_count * rose_price + cactus_count * cactus_price
tax = turnover * 0.05
turnover_after_tax = turnover - tax
diff = abs(turnover_after_tax - price_for_gift)
diff_floor = floor(diff)
diff_ceil = ceil(diff)


if turnover_after_tax >= price_for_gift:
    print(f"She is left with {diff_floor} leva.")
else:
    print(f"She will have to borrow {diff_ceil} leva.")