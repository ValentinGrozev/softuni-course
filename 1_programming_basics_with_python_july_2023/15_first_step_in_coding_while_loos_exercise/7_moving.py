width = int(input())
length = int(input())
height = int(input())
number_of_boxes = input()

volume_room = width * length * height
volume_box = 1
count_boxes = 0

while number_of_boxes != "Done":
    number_of_boxes = int(number_of_boxes)
    count_boxes += number_of_boxes
    volume_boxes = volume_box * count_boxes
    if volume_room <= volume_boxes:
        diff = abs(volume_boxes - volume_room)
        break
    number_of_boxes = input()

volume_boxes = volume_box * count_boxes

if volume_room > volume_boxes:
    diff = abs(volume_boxes - volume_room)
    print(f"{diff} Cubic meters left.")
else:
    diff = abs(volume_boxes - volume_room)
    print(f"No more free space! You need {diff} Cubic meters more.")
