def add_stop(stops, index, additional_stop):
    if index in range(len(stops)):
        stops = stops[:index] + additional_stop + stops[index:]
    return stops


def remove_stop(stops, start_index, end_index):
    if start_index in range(len(stops)) and end_index in range(len(stops)):
        stops = stops[:start_index] + stops[end_index + 1:]
    return stops


def switch_stop(stops, old_stop, new_stop):
    if old_stop in stops:
        stops = stops.replace(old_stop, new_stop)
    return stops


def main():

    stops = input()
    command = input().split(":")

    while command[0] != "Travel":
        action = command[0]
        if action == "Add Stop":
            index = int(command[1])
            additional_stop = command[2]
            stops = add_stop(stops, index, additional_stop)
        elif action == "Remove Stop":
            start_index = int(command[1])
            end_index = int(command[2])
            stops = remove_stop(stops, start_index, end_index)
        elif action == "Switch":
            old_stop = command[1]
            new_stop = command[2]
            stops = switch_stop(stops, old_stop, new_stop)
        print(stops)
        command = input().split(":")

    print(f"Ready for world tour! Planned stops: {stops}")


main()
