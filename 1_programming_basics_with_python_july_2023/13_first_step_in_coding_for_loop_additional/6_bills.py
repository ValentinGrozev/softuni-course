number_of_months = int(input())

all_bills = 0
electricity_bill = 0
water_bill = 0
internet_bill = 0
other_bill = 0

for _ in range(number_of_months):
    bill_for_electricity = float(input())
    electricity_bill += bill_for_electricity
    water_bill += 20
    internet_bill += 15
    other_bill += (bill_for_electricity + 20 + 15) * 1.20

all_bills = electricity_bill + water_bill + internet_bill + other_bill
average_bills = all_bills / number_of_months

print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {other_bill:.2f} lv")
print(f"Average: {average_bills:.2f} lv")


