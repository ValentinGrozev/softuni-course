def count_free_chairs(line, room_number):
    [chairs, visitors] = line.split()
    diff = len(chairs) - int(visitors)
    if diff < 0:
        print(f"{diff} more chairs needed in room {room_number}")
    return diff


def is_there_free_chairs(rooms):
    free_chairs = 0
    for room_number in range(1, rooms + 1):
        input_line = input()
        free_chairs += count_free_chairs(input_line, room_number)

    if free_chairs >= 0:
        return f"Game On, {free_chairs} free chairs left"
    else:
        return ''


number_of_rooms = int(input())
print(is_there_free_chairs(number_of_rooms))
