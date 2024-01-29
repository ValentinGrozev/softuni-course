from collections import deque

worms = [int(worm) for worm in input().split()]
holes = deque([int(hole) for hole in input().split()])

worms_length = len(worms)
matches = 0

while worms and holes:
    last_worm = worms.pop()
    first_hole = holes.popleft()

    if first_hole == last_worm:
        matches += 1
    else:
        corrected_worm = last_worm - 3
        if corrected_worm > 0:
            worms.append(corrected_worm)

if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if len(worms) == 0 and matches == worms_length:
    print("Every worm found a suitable hole!")

if len(worms) == 0 and matches != worms_length:
    print("Worms left: none")

if worms:
    print(f"Worms left: {', '.join(str(worm) for worm in worms)}")

if holes:
    print(f"Holes left: {', '.join(str(hole) for hole in holes)}")
else:
    print("Holes left: none")
