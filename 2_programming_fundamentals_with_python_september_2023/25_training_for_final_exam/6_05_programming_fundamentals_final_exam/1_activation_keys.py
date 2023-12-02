def contain_check(raw_activation_key, substring):
    if substring in raw_activation_key:
        print(f"{raw_activation_key} contains {substring}")
    else:
        print("Substring not found!")
    return raw_activation_key


def flip_letters_to_upper_or_lower(raw_activation_key, upper_or_lower, start_index, end_index):
    if upper_or_lower == "Upper":
        key_to_change = raw_activation_key[start_index:end_index].upper()
        raw_activation_key = raw_activation_key[:start_index] + key_to_change + raw_activation_key[end_index:]
        print(raw_activation_key)
    elif upper_or_lower == "Lower":
        key_to_change = raw_activation_key[start_index:end_index].lower()
        raw_activation_key = raw_activation_key[:start_index] + key_to_change + raw_activation_key[end_index:]
        print(raw_activation_key)
    return raw_activation_key


def slice_letters(raw_activation_key, start_index, end_index):
    raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
    print(raw_activation_key)
    return raw_activation_key


def main():

    raw_activation_key = input()
    command = input().split(">>>")

    while command[0] != "Generate":
        action = command[0]
        if action == "Contains":
            substring = command[1]
            raw_activation_key = contain_check(raw_activation_key, substring)
        elif action == "Flip":
            upper_or_lower = command[1]
            start_index = int(command[2])
            end_index = int(command[3])
            raw_activation_key = flip_letters_to_upper_or_lower(raw_activation_key, upper_or_lower,
                                                                start_index, end_index)
        elif action == "Slice":
            start_index = int(command[1])
            end_index = int(command[2])
            raw_activation_key = slice_letters(raw_activation_key, start_index, end_index)

        command = input().split(">>>")

    print(f"Your activation key is: {raw_activation_key}")


main()
