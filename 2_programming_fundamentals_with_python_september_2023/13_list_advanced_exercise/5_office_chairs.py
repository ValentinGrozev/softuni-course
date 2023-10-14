number_of_rooms = int(input())
free_chairs = 0

for room in range(1, number_of_rooms + 1):
    [chairs, visitors] = input().split()
    if len(chairs) >= int(visitors):
        extra_chairs = len(chairs) - int(visitors)
        free_chairs += extra_chairs
    else:
        needed_chairs = int(visitors) - len(chairs)
        free_chairs -= needed_chairs
        print(f"{needed_chairs} more chairs needed in room {room}")

if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")