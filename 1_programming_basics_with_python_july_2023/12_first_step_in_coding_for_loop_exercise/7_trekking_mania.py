number_of_groups = int(input())

musala_groups = 0
monblan_groups = 0
kilimandjaro_groups = 0
k2_groups = 0
everest_groups = 0
all_people = 0

for _ in range(number_of_groups):
    number_of_people_in_group = int(input())
    if number_of_people_in_group <= 5:
        musala_groups += number_of_people_in_group
    elif 5 < number_of_people_in_group <= 12:
        monblan_groups += number_of_people_in_group
    elif 12 < number_of_people_in_group <= 25:
        kilimandjaro_groups += number_of_people_in_group
    elif 25 < number_of_people_in_group <= 40:
        k2_groups += number_of_people_in_group
    elif number_of_people_in_group > 40:
        everest_groups += number_of_people_in_group

all_people = musala_groups + monblan_groups + kilimandjaro_groups + k2_groups + everest_groups
musala_percent = (musala_groups / all_people) * 100
monblan_percent = (monblan_groups / all_people) * 100
kilimandjaro_percent = (kilimandjaro_groups / all_people) * 100
k2_percent = (k2_groups / all_people) * 100
everest_percent = (everest_groups / all_people) * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimandjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")

