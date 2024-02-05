from collections import deque

textiles = deque([int(textile) for textile in input().split(" ")])
medicaments = [int(medicaments) for medicaments in input().split(" ")]

healing_items = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit",
}

created_items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0,
}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()

    result = current_textile + current_medicament

    if result in healing_items:
        item = healing_items[result]
        created_items[item] += 1

    elif result > 100:
        difference = result - 100
        created_items["MedKit"] += 1

        next_medicament_element = medicaments.pop()
        next_medicament_element += difference
        medicaments.append(next_medicament_element)

    else:
        current_medicament += 10
        medicaments.append(current_medicament)

if not textiles and medicaments:
    print("Textiles are empty.")

if not medicaments and textiles:
    print("Medicaments are empty.")

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

sorted_created_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))

for item, amount in sorted_created_items:
    if amount != 0:
        print(f"{item} - {amount}")

if medicaments:
    print(f"Medicaments left: {', '.join([str(medicament) for medicament in medicaments[::-1]])}")

if textiles:
    print(f"Textiles left: {', '.join([str(textile) for textile in textiles])}")
