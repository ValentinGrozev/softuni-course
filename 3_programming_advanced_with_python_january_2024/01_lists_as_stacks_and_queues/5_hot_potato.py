from collections import deque

children_names = deque(input().split())
number_of_toss = int(input()) - 1

while len(children_names) != 1:
    children_names.rotate(-number_of_toss)
    print(f"Removed {children_names.popleft()}")

print(f"Last is {children_names.pop()}")
