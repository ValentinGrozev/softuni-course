bottles_of_detergent = int(input())
detergent_in_ml = bottles_of_detergent * 750
days = 0
used_detergent = 0
clean_dishes = 0
clean_pots = 0
information = input()

while information != "End":
    number_of_dishes_or_pots = int(information)
    days += 1
    if days % 3 == 0:
        used_detergent += 15 * number_of_dishes_or_pots
        clean_pots += number_of_dishes_or_pots
    else:
        clean_dishes += number_of_dishes_or_pots
        used_detergent += 5 * number_of_dishes_or_pots
    if used_detergent > detergent_in_ml:
        break
    information = input()

diff = abs(used_detergent - detergent_in_ml)

if used_detergent > detergent_in_ml:
    print(f"Not enough detergent, {diff} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{clean_dishes} dishes and {clean_pots} pots were washed.")
    print(f"Leftover detergent {diff} ml.")