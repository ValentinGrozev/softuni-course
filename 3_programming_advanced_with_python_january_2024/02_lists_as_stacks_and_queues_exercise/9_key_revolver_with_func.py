from collections import deque


def reloading(counter, size_of_gun_barrel, bullets):
    if counter == size_of_gun_barrel and bullets:
        print("Reloading!")
        return True


def is_locked(size_of_bullet, size_of_lock):
    return size_of_bullet > size_of_lock


def final_result(locks, bullets, money_earned):
    if not locks:
        print(f"{len(bullets)} bullets left. Earned ${money_earned}")
    else:
        print(f"Couldn't get through. Locks left: {len(locks)}")


def main():
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
        if is_locked(current_bullet, current_lock):
            print("Ping!")
            locks.appendleft(current_lock)
        else:
            print("Bang!")
        expense_for_bullets += cost_of_a_bullet
        shoot += 1
        if reloading(shoot, size_of_gun_barrel, bullets):
            shoot = 0

    money_earned = prize - expense_for_bullets

    final_result(locks, bullets, money_earned)


main()
