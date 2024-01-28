# first solution:
def fill_the_box(height, length, width, *cubes):
    size_of_the_box = height * length * width
    all_cubes = sum([int(x) for x in cubes if x != "Finish"])
    for cube in cubes:
        if cube == "Finish":
            break
        else:
            size_of_the_box -= cube
            all_cubes -= cube
            if size_of_the_box >= 0:
                continue
            else:
                all_cubes += abs(size_of_the_box)
                return f"No more free space! You have {all_cubes} more cubes."
    return f"There is free space in the box. You could put {size_of_the_box} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))


# second_solution:
# def fill_the_box(height, length, width, *cubes):
#     box_volume = height * length * width
#     all_cubes = sum([int(x) for x in cubes if x != "Finish"])
#
#     filled_in_volume = 0
#     for cube in cubes:
#         if cube != "Finish":
#             if cube < box_volume - filled_in_volume:
#                 filled_in_volume += cube
#             else:
#                 filled_in_volume = box_volume
#                 break
#         else:
#             break
#     if box_volume > filled_in_volume:
#         return f"There is free space in the box. You could put {box_volume - filled_in_volume } more cubes."
#     else:
#         return f"No more free space! You have {all_cubes - filled_in_volume} more cubes."
#
#
# print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
# print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
