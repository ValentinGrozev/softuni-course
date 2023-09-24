number_of_chrysanthemums = int(input())
number_of_roses = int(input())
number_of_tulips = int(input())
season = input()
day_is_holiday = input()

if day_is_holiday == "Y":
    if season == "Spring":
        if number_of_tulips > 7:
            price_for_tulips = 2.50
            price_for_chrysanthemums = 2
            price_for_roses = 4.10
            arrange = 2
            cost_for_bouquet = number_of_tulips * price_for_tulips + number_of_roses * price_for_roses + \
                               number_of_chrysanthemums * price_for_chrysanthemums
            holiday_day = cost_for_bouquet * 1.15
            final_cost_bouquet = holiday_day * 0.95
            number_of_all_flowers = number_of_chrysanthemums + number_of_roses + number_of_tulips
            if number_of_all_flowers > 20:
                final_cost_bouquet = final_cost_bouquet * 0.80
                final_cost_bouquet = final_cost_bouquet + 2
                print(f"{final_cost_bouquet:.2f}")
            else:
                final_cost_bouquet = final_cost_bouquet + 2
                print(f"{final_cost_bouquet:.2f}")
        else:
            price_for_tulips = 2.50
            price_for_chrysanthemums = 2
            price_for_roses = 4.10
            arrange = 2
            cost_for_bouquet = number_of_tulips * price_for_tulips + number_of_roses * price_for_roses + \
                               number_of_chrysanthemums * price_for_chrysanthemums
            holiday_day = cost_for_bouquet * 1.15
            final_cost_bouquet = holiday_day
            number_of_all_flowers = number_of_chrysanthemums + number_of_roses + number_of_tulips
            if number_of_all_flowers > 20:
                final_cost_bouquet = final_cost_bouquet * 0.80
                final_cost_bouquet = final_cost_bouquet + 2
                print(f"{final_cost_bouquet:.2f}")
            else:
                final_cost_bouquet = final_cost_bouquet + 2
                print(f"{final_cost_bouquet:.2f}")
    elif season == "Winter":
        if number_of_roses >= 10:
            price_for_tulips = 4.15
            price_for_chrysanthemums = 3.75
            price_for_roses = 4.50
            arrange = 2
            cost_for_bouquet = number_of_tulips * price_for_tulips + number_of_roses * price_for_roses + \
                               number_of_chrysanthemums * price_for_chrysanthemums
            holiday_day = cost_for_bouquet * 1.15
            final_cost_bouquet = holiday_day * 0.90
            number_of_all_flowers = number_of_chrysanthemums + number_of_roses + number_of_tulips
            if number_of_all_flowers > 20:
                final_cost_bouquet = final_cost_bouquet * 0.80
                final_cost_bouquet = final_cost_bouquet + 2
                print(f"{final_cost_bouquet:.2f}")
            else:
                final_cost_bouquet = final_cost_bouquet + 2
                print(f"{final_cost_bouquet:.2f}")
        else:
            price_for_tulips = 4.15
            price_for_chrysanthemums = 3.75
            price_for_roses = 4.50
            arrange = 2
            cost_for_bouquet = number_of_tulips * price_for_tulips + number_of_roses * price_for_roses + \
                               number_of_chrysanthemums * price_for_chrysanthemums
            holiday_day = cost_for_bouquet * 1.15
            final_cost_bouquet = holiday_day
            number_of_all_flowers = number_of_chrysanthemums + number_of_roses + number_of_tulips
            if number_of_all_flowers > 20:
                final_cost_bouquet = final_cost_bouquet * 0.80
                final_cost_bouquet = final_cost_bouquet + 2
                print(f"{final_cost_bouquet:.2f}")
            else:
                final_cost_bouquet = final_cost_bouquet + 2
                print(f"{final_cost_bouquet:.2f}")
    elif season == "Autumn":
        price_for_tulips = 4.15
        price_for_chrysanthemums = 3.75
        price_for_roses = 4.50
        arrange = 2
        cost_for_bouquet = number_of_tulips * price_for_tulips + number_of_roses * price_for_roses + \
                           number_of_chrysanthemums * price_for_chrysanthemums
        holiday_day = cost_for_bouquet * 1.15
        final_cost_bouquet = holiday_day
        number_of_all_flowers = number_of_chrysanthemums + number_of_roses + number_of_tulips
        if number_of_all_flowers > 20:
            final_cost_bouquet = final_cost_bouquet * 0.80
            final_cost_bouquet = final_cost_bouquet + 2
            print(f"{final_cost_bouquet:.2f}")
        else:
            final_cost_bouquet = final_cost_bouquet + 2
            print(f"{final_cost_bouquet:.2f}")
    elif season == "Summer":
        price_for_tulips = 2.50
        price_for_chrysanthemums = 2
        price_for_roses = 4.10
        arrange = 2
        cost_for_bouquet = number_of_tulips * price_for_tulips + number_of_roses * price_for_roses + \
                           number_of_chrysanthemums * price_for_chrysanthemums
        holiday_day = cost_for_bouquet * 1.15
        final_cost_bouquet = holiday_day
        number_of_all_flowers = number_of_chrysanthemums + number_of_roses + number_of_tulips
        if number_of_all_flowers > 20:
            final_cost_bouquet = final_cost_bouquet * 0.80
            final_cost_bouquet = final_cost_bouquet + 2
            print(f"{final_cost_bouquet:.2f}")
        else:
            final_cost_bouquet = final_cost_bouquet + 2
            print(f"{final_cost_bouquet:.2f}")

elif day_is_holiday == "N":
    if season == "Spring":
        if number_of_tulips > 7:
            price_for_tulips = 2.50
            price_for_chrysanthemums = 2
            price_for_roses = 4.10
            arrange = 2
            cost_for_bouquet = number_of_tulips * price_for_tulips + number_of_roses * price_for_roses + \
                               number_of_chrysanthemums * price_for_chrysanthemums
            final_cost_bouquet = cost_for_bouquet * 0.95
            number_of_all_flowers = number_of_chrysanthemums + number_of_roses + number_of_tulips
            if number_of_all_flowers > 20:
                final_cost_bouquet = final_cost_bouquet * 0.80
                final_cost_bouquet = final_cost_bouquet + 2
                print(f"{final_cost_bouquet:.2f}")
            else:
                final_cost_bouquet = final_cost_bouquet + 2
                print(f"{final_cost_bouquet:.2f}")
        else:
            price_for_tulips = 2.50
            price_for_chrysanthemums = 2
            price_for_roses = 4.10
            arrange = 2
            cost_for_bouquet = number_of_tulips * price_for_tulips + number_of_roses * price_for_roses + \
                               number_of_chrysanthemums * price_for_chrysanthemums
            final_cost_bouquet = cost_for_bouquet
            number_of_all_flowers = number_of_chrysanthemums + number_of_roses + number_of_tulips
            if number_of_all_flowers > 20:
                final_cost_bouquet = final_cost_bouquet * 0.80
                final_cost_bouquet = final_cost_bouquet + 2
                print(f"{final_cost_bouquet:.2f}")
            else:
                final_cost_bouquet = final_cost_bouquet + 2
                print(f"{final_cost_bouquet:.2f}")
    elif season == "Winter":
        if number_of_roses >= 10:
            price_for_tulips = 4.15
            price_for_chrysanthemums = 3.75
            price_for_roses = 4.50
            arrange = 2
            cost_for_bouquet = number_of_tulips * price_for_tulips + number_of_roses * price_for_roses + \
                               number_of_chrysanthemums * price_for_chrysanthemums
            final_cost_bouquet = cost_for_bouquet * 0.90
            number_of_all_flowers = number_of_chrysanthemums + number_of_roses + number_of_tulips
            if number_of_all_flowers > 20:
                final_cost_bouquet = final_cost_bouquet * 0.80
                final_cost_bouquet = final_cost_bouquet + 2
                print(f"{final_cost_bouquet:.2f}")
            else:
                final_cost_bouquet = final_cost_bouquet + 2
                print(f"{final_cost_bouquet:.2f}")
        else:
            price_for_tulips = 4.15
            price_for_chrysanthemums = 3.75
            price_for_roses = 4.50
            arrange = 2
            cost_for_bouquet = number_of_tulips * price_for_tulips + number_of_roses * price_for_roses + \
                               number_of_chrysanthemums * price_for_chrysanthemums
            final_cost_bouquet = cost_for_bouquet
            number_of_all_flowers = number_of_chrysanthemums + number_of_roses + number_of_tulips
            if number_of_all_flowers > 20:
                final_cost_bouquet = final_cost_bouquet * 0.80
                final_cost_bouquet = final_cost_bouquet + 2
                print(f"{final_cost_bouquet:.2f}")
            else:
                final_cost_bouquet = final_cost_bouquet + 2
                print(f"{final_cost_bouquet:.2f}")
    elif season == "Autumn":
        price_for_tulips = 4.15
        price_for_chrysanthemums = 3.75
        price_for_roses = 4.50
        arrange = 2
        cost_for_bouquet = number_of_tulips * price_for_tulips + number_of_roses * price_for_roses + \
                           number_of_chrysanthemums * price_for_chrysanthemums
        final_cost_bouquet = cost_for_bouquet
        number_of_all_flowers = number_of_chrysanthemums + number_of_roses + number_of_tulips
        if number_of_all_flowers > 20:
            final_cost_bouquet = final_cost_bouquet * 0.80
            final_cost_bouquet = final_cost_bouquet + 2
            print(f"{final_cost_bouquet:.2f}")
        else:
            final_cost_bouquet = final_cost_bouquet + 2
            print(f"{final_cost_bouquet:.2f}")
    elif season == "Summer":
        price_for_tulips = 2.50
        price_for_chrysanthemums = 2
        price_for_roses = 4.10
        arrange = 2
        cost_for_bouquet = number_of_tulips * price_for_tulips + number_of_roses * price_for_roses + \
                           number_of_chrysanthemums * price_for_chrysanthemums
        final_cost_bouquet = cost_for_bouquet
        number_of_all_flowers = number_of_chrysanthemums + number_of_roses + number_of_tulips
        if number_of_all_flowers > 20:
            final_cost_bouquet = final_cost_bouquet * 0.80
            final_cost_bouquet = final_cost_bouquet + 2
            print(f"{final_cost_bouquet:.2f}")
        else:
            final_cost_bouquet = final_cost_bouquet + 2
            print(f"{final_cost_bouquet:.2f}")