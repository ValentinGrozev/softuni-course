from collections import deque

cost_of_a_bullet = int(input())
size_of_gun_barrel = int(input())
bullets = ([int(x) for x in input().split()])
locks = deque(int(x) for x in input().split())
prize = int(input())

expense_for_bullets = 0
shoot = 0

while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()
    if current_bullet > current_lock:
        print("Ping!")
        locks.appendleft(current_lock)
    else:
        print("Bang!")
    expense_for_bullets += cost_of_a_bullet
    shoot += 1
    if shoot == size_of_gun_barrel and bullets:
        print("Reloading!")
        shoot = 0

money_earned = prize - expense_for_bullets

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
