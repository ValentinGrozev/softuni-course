from collections import deque

cups_and_their_capacity = deque([int(cup) for cup in input().split()])
bottles_and_their_capacity = ([int(bottle) for bottle in input().split()])
wasted_water = 0

while cups_and_their_capacity and bottles_and_their_capacity:
    bottle_capacity = bottles_and_their_capacity.pop()
    cup_capacity = cups_and_their_capacity.popleft()

    if bottle_capacity < cup_capacity:
        cups_and_their_capacity.appendleft(cup_capacity - bottle_capacity)
    else:
        wasted_water += bottle_capacity - cup_capacity

if bottles_and_their_capacity:
    print(f"Bottles:", *bottles_and_their_capacity, sep=" ")
if cups_and_their_capacity:
    print(f"Cups:", *cups_and_their_capacity, sep=" ")

print(f"Wasted litters of water: {wasted_water}")
