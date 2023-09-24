flower_type = input()
quantity_flowers = int(input())
budget = int(input())

price = 0
if flower_type == "Roses":
    if quantity_flowers > 80:
        price = (quantity_flowers * 5) * 0.90
    else:
        price = quantity_flowers * 5
elif flower_type == "Dahlias":
    if quantity_flowers > 90:
        price = (quantity_flowers * 3.80) * 0.85
    else:
        price = quantity_flowers * 3.80
elif flower_type == "Tulips":
    if quantity_flowers > 80:
        price = (quantity_flowers * 2.80) * 0.85
    else:
        price = quantity_flowers * 2.80
elif flower_type == "Narcissus":
    if quantity_flowers < 120:
        price = (quantity_flowers * 3.00) * 1.15
    else:
        price = quantity_flowers * 3.00
elif flower_type == "Gladiolus":
    if quantity_flowers < 80:
        price = (quantity_flowers * 2.50) * 1.20
    else:
        price = quantity_flowers * 2.50

diff = abs(budget - price)

if budget >= price:
    print(f"Hey, you have a great garden with {quantity_flowers} {flower_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")