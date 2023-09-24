stadium_cap = int(input())
number_of_fans = int(input())

fans_in_A_sector = 0   # Sectors A
fans_in_B_sector = 0   # Sectors B
fans_in_V_sector = 0  # Sectors V
fans_in_G_sector = 0  # Sectors G

for fans in range(number_of_fans):
    sector = input()
    if sector == "A":
        fans_in_A_sector += 1
    elif sector == "B":
        fans_in_B_sector += 1
    elif sector == "V":
        fans_in_V_sector += 1
    elif sector == "G":
        fans_in_G_sector += 1

all_fans = fans_in_A_sector + fans_in_B_sector + fans_in_V_sector + fans_in_G_sector
percent_fans_A_sector = (fans_in_A_sector / number_of_fans) * 100
percent_fans_B_sector = (fans_in_B_sector / number_of_fans) * 100
percent_fans_V_sector = (fans_in_V_sector / number_of_fans) * 100
percent_fans_G_sector = (fans_in_G_sector / number_of_fans) * 100
percent_all_fans = (all_fans / stadium_cap) * 100

print(f"{percent_fans_A_sector:.2f}%")
print(f"{percent_fans_B_sector:.2f}%")
print(f"{percent_fans_V_sector:.2f}%")
print(f"{percent_fans_G_sector:.2f}%")
print(f"{percent_all_fans:.2f}%")