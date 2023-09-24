inherited_money = float(input())
year_to_live = int(input())

sum_even_years = 0
sum_odd_years = 0

for year in range(1800, year_to_live + 1):
    if year % 2 == 0:
        sum_even_years += 12000
    else:
        sum_odd_years += ((year - 1800 + 18) * 50) + 12000

needed_money = sum_even_years + sum_odd_years
diff = abs(inherited_money - needed_money)

if inherited_money >= needed_money:
    print(f"Yes! He will live a carefree life and will have {diff:.2f} dollars left.")
else:
    print(f"He will need {diff:.2f} dollars to survive.")
