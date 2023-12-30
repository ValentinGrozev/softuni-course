from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

presents = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
crafted_presents = {}

while materials and magic:
    current_material = materials[-1]
    current_magic = magic[0]
    if current_material == 0 and current_magic == 0:
        materials.pop()
        magic.popleft()
        continue
    if current_material == 0:
        materials.pop()
        continue
    if current_magic == 0:
        magic.popleft()
        continue
    total_magic = current_material * current_magic
    if total_magic in presents:
        materials.pop()
        magic.popleft()
        crafted_present = presents[total_magic]
        if crafted_present not in crafted_presents:
            crafted_presents[crafted_present] = 0
        crafted_presents[crafted_present] += 1
    elif total_magic < 0:
        materials.pop()
        magic.popleft()
        materials.append(current_material + current_magic)
    elif total_magic > 0:
        magic.popleft()
        materials[-1] += 15

if "Doll" in crafted_presents.keys() and "Wooden train" in crafted_presents.keys() or \
        "Teddy bear" in crafted_presents.keys() and "Bicycle" in crafted_presents.keys():
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for toy, amount in sorted(crafted_presents.items()):
    print(f"{toy}: {amount}")
