def people_in_wagons(wagons):
    wagons_length = [0] * wagons
    command = input().split()

    while command[0] != "End":
        if command[0] == "add":
            wagons_length[-1] += int(command[1])
        elif command[0] == "insert":
            index = int(command[1])
            people = int(command[2])
            wagons_length[index] += people
        elif command[0] == "leave":
            index = int(command[1])
            people = int(command[2])
            wagons_length[index] -= people
        command = input().split()
    return wagons_length


number_of_wagons = int(input())
print(people_in_wagons(number_of_wagons))