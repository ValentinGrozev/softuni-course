square_meters_to_landscape = float(input())

Price = square_meters_to_landscape * 7.61
Discount = Price * 0.18
Final_price = Price - Discount

print(f"The final price is: {Final_price} lv")
print(f"The discount is: {Discount} lv")
