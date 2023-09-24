days = int(input())

total_amount_of_brandy = 0
degrees = 0

for _ in range(days):
    amount_of_brandy = float(input())
    degrees_of_brandy = float(input())
    total_amount_of_brandy += amount_of_brandy
    degrees += amount_of_brandy * degrees_of_brandy

average_degree_of_brandy = (degrees / total_amount_of_brandy)

print(f"Liter: {total_amount_of_brandy:.2f}")
print(f"Degrees: {average_degree_of_brandy:.2f}")

if average_degree_of_brandy < 38:
    print("Not good, you should baking!")
elif 38 <= average_degree_of_brandy <= 42:
    print("Super!")
elif average_degree_of_brandy > 42:
    print("Dilution with distilled water!")
