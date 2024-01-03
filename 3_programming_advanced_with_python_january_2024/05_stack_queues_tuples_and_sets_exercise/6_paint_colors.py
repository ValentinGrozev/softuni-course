from collections import deque

text = deque(input().split())

main_colors = ["red", "yellow", "blue"]
secondary_colors = {"orange": ["red", "yellow"], "purple": ["red", "blue"], "green": ["yellow", "blue"]}

created_colors = []

while len(text) > 0:
    if len(text) > 1:
        first_string = text.popleft()
        last_string = text.pop()
        if (first_string + last_string) in main_colors or (first_string + last_string) in secondary_colors:
            created_colors.append(first_string + last_string)
        elif (last_string + first_string) in main_colors or (last_string + first_string) in secondary_colors:
            created_colors.append(last_string + first_string)
        else:
            middle_point = len(text) // 2
            if len(first_string) > 1:
                text.insert(middle_point, first_string[:-1])
            if len(last_string) > 1:
                text.insert(middle_point, last_string[:-1])
    elif len(text) == 1:
        last_string = text.pop()
        if last_string in main_colors or last_string in secondary_colors:
            created_colors.append(last_string)


for color in created_colors:
    if color in secondary_colors:
        for el in secondary_colors[color]:
            if el not in created_colors:
                created_colors.remove(color)

print(created_colors)
