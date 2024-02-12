from collections import deque

size_of_eggs = deque([int(x) for x in input().split(", ")])
size_of_piece_of_paper = deque([int(x) for x in input().split(", ")])

size_of_box = 50
box_filled = 0

while size_of_eggs and size_of_piece_of_paper:
    current_egg = size_of_eggs.popleft()

    if current_egg == 13:
        first_element = size_of_piece_of_paper.popleft()
        last_element = size_of_piece_of_paper.pop()
        size_of_piece_of_paper.appendleft(last_element)
        size_of_piece_of_paper.append(first_element)
        continue

    elif current_egg <= 0:
        continue

    else:
        current_piece_of_paper = size_of_piece_of_paper.pop()

        result = current_egg + current_piece_of_paper

        if result <= size_of_box:
            box_filled += 1


if box_filled > 0:
    print(f"Great! You filled {box_filled} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if size_of_eggs:
    print(f"Eggs left: {', '.join(str(egg) for egg in size_of_eggs)}")

if size_of_piece_of_paper:
    print(f"Pieces of paper left: {', '.join(str(paper) for paper in size_of_piece_of_paper)}")
