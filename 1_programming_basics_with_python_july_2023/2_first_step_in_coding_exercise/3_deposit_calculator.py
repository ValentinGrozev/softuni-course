deposited_amount = float(input())
duration = int(input())
annual_rate = float(input())

additional_amount = deposited_amount * (annual_rate / 100)
monthly_add_amount = additional_amount / 12
total_amount = deposited_amount + monthly_add_amount * duration

print(total_amount)