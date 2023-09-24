product = input()
city = input()
quantity = float(input())

sofia_dict = {
    "coffee" : 0.50,
    "water" : 0.80,
    "beer" : 1.20,
    "sweets" : 1.45,
    "peanuts" : 1.60}
plovdiv_dict = {
    "coffee" : 0.40,
    "water" : 0.70,
    "beer" : 1.15,
    "sweets" : 1.30,
    "peanuts" : 1.50}
varna_dict = {
    "coffee" : 0.45,
    "water" : 0.70,
    "beer" : 1.10,
    "sweets" : 1.35,
    "peanuts" : 1.55}

total_price = 0
if city == "Sofia":
    total_price = sofia_dict[product] * quantity
elif city == "Plovdiv":
    total_price = plovdiv_dict[product] * quantity
elif city == "Varna":
    total_price = varna_dict[product] * quantity
print(total_price)
