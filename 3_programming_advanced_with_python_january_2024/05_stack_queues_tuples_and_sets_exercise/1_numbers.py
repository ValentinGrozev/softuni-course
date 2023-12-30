def add_first(first_set, number_list):
    first_set.update((int(x) for x in number_list))
    return first_set


def add_second(second_set, number_list):
    second_set.update((int(x) for x in number_list))
    return second_set


def remove_first(first_set, number_list):
    first_set.difference_update((int(x) for x in number_list))
    return first_set


def remove_second(second_set, number_list):
    second_set.difference_update((int(x) for x in number_list))
    return second_set


def check_subset(first_set, second_set):
    result = first_set.issubset(second_set) or second_set.issubset(first_set)
    return result


def main():
    first_set = set([int(x) for x in input().split()])
    second_set = set([int(x) for x in input().split()])
    number_of_commands = int(input())

    for command in range(number_of_commands):
        current_command = input().split()
        if current_command[0] + " " + current_command[1] == "Add First":
            add_first(first_set, current_command[2:])
        elif current_command[0] + " " + current_command[1] == "Add Second":
            add_second(second_set, current_command[2:])
        elif current_command[0] + " " + current_command[1] == "Remove First":
            remove_first(first_set, current_command[2:])
        elif current_command[0] + " " + current_command[1] == "Remove Second":
            remove_second(second_set, current_command[2:])
        elif current_command[0] + " " + current_command[1] == "Check Subset":
            print(check_subset(first_set, second_set))

    first_set = sorted(first_set)
    second_set = sorted(second_set)
    print(", ".join(str(x) for x in first_set))
    print(", ".join(str(x) for x in second_set))

    # print(*sorted(first_set), sep=", ") --> In that case don't need to sort set beforehand
    # print(*sorted(second_set), sep=", ") --> In that case don't need to sort set beforehand


main()
