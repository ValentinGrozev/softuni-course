month = input()
nights_count = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    if 14 >= nights_count > 7:
        apartment_price = 65 * nights_count
        studio_price = (50 * 0.95) * nights_count
        print(f"Apartment: {apartment_price:.2f} lv.")
        print(f"Studio: {studio_price:.2f} lv.")
    elif nights_count <= 7:
        apartment_price = 65 * nights_count
        studio_price = 50 * nights_count
        print(f"Apartment: {apartment_price:.2f} lv.")
        print(f"Studio: {studio_price:.2f} lv.")
    else:
        apartment_price = (65 * 0.90) * nights_count
        studio_price = (50 * 0.70) * nights_count
        print(f"Apartment: {apartment_price:.2f} lv.")
        print(f"Studio: {studio_price:.2f} lv.")

elif month == "June" or month == "September":
    if nights_count > 14:
        apartment_price = (68.7 * 0.90) * nights_count
        studio_price = (75.2 * 0.80) * nights_count
        print(f"Apartment: {apartment_price:.2f} lv.")
        print(f"Studio: {studio_price:.2f} lv.")
    else:
        apartment_price = 68.7 * nights_count
        studio_price = 75.2 * nights_count
        print(f"Apartment: {apartment_price:.2f} lv.")
        print(f"Studio: {studio_price:.2f} lv.")

elif month == "July" or month == "August":
    if nights_count > 14:
        apartment_price = (77 * 0.90) * nights_count
        studio_price = 76 * nights_count
        print(f"Apartment: {apartment_price:.2f} lv.")
        print(f"Studio: {studio_price:.2f} lv.")
    else:
        apartment_price = 77 * nights_count
        studio_price = 76 * nights_count
        print(f"Apartment: {apartment_price:.2f} lv.")
        print(f"Studio: {studio_price:.2f} lv.")