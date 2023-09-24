centuries = int(input())

years = int(centuries * 100)
days = int(years * 365.2422)
hours = int(days * 24)
minutes = int(hours * 60)

print(f"{centuries:.0f} centuries = {years:.0f} years = {days:.0f} days = {hours:.0f} hours = {minutes:.0f} minutes")
