def accommodate_new_pets(capacity, weight_limit, *pet_info):
    accommodated_pets = {}
    text_to_print = ''
    no_capacity_left = False

    for pet, weight in pet_info:
        if capacity == 0:
            no_capacity_left = True
            break

        if capacity > 0 and weight <= weight_limit:
            if pet not in accommodated_pets:
                accommodated_pets[pet] = 0
            accommodated_pets[pet] += 1
            capacity -= 1

    if not no_capacity_left:
        text_to_print += f"All pets are accommodated! Available capacity: {capacity}.\n"
    else:
        text_to_print += f"You did not manage to accommodate all pets!\n"

    sorted_pets_in_hotel = sorted(accommodated_pets.items(), key=lambda x: x[0])

    text_to_print += "Accommodated pets:\n"

    for pet, count in sorted_pets_in_hotel:
        text_to_print += f"{pet}: {count}\n"

    return text_to_print


print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
