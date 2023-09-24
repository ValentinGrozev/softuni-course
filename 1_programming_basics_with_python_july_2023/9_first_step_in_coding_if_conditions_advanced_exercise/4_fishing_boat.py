budget = int(input())
season = input()
number_of_fisherman = int(input())

price = 0

if season == "Spring":
    if 6 >= number_of_fisherman:
        price = 3000 * 0.9
    elif 6 < number_of_fisherman <= 11:
        price = 3000 * 0.85
    elif number_of_fisherman > 11:
        price = 3000 * 0.75

elif season == "Summer" or season == "Autumn":
    if 6 >= number_of_fisherman:
        price = 4200 * 0.9
    elif 6 < number_of_fisherman <= 11:
        price = 4200 * 0.85
    elif number_of_fisherman > 11:
        price = 4200 * 0.75

elif season == "Winter":
    if 6 >= number_of_fisherman:
        price = 2600 * 0.9
    elif 6 < number_of_fisherman <= 11:
        price = 2600 * 0.85
    elif number_of_fisherman > 11:
        price = 2600 * 0.75

if number_of_fisherman % 2 == 0 and season != "Autumn":
    price = price * 0.95
else:
    price = price

diff = abs(budget - price)

if budget >= price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")