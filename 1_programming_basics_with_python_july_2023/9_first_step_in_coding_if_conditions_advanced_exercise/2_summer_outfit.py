degrees = int(input())
daytime = input()

Outfit = ""
Shoes = ""

if daytime == "Morning":
    if 10 <= degrees <= 18:
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
    elif 18 < degrees <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
    elif degrees > 24:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
elif daytime == "Afternoon":
    if 10 <= degrees <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
    elif 18 < degrees <= 24:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
    elif degrees > 24:
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
elif daytime == "Evening":
    if 10 <= degrees <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
    elif 18 < degrees <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")
    elif degrees > 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {Outfit} and {Shoes}.")



