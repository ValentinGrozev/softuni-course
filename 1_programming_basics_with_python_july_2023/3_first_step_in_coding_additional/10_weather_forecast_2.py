degrees = float(input())

z = degrees

if  26 <= z <= 35:
    print("Hot")
elif 20.1 <= z <= 25.9:
    print("Warm")
elif 15 <= z <= 20:
    print("Mild")
elif 12 <= z <= 14.9:
    print("Cool")
elif 5 <= z <= 11.9:
    print("Cold")
else:
    print("unknown")