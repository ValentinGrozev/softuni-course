name_of_the_gifts = input().split()
command = input()

while command != "No Money":
    input_line = command.split()

    if "OutOfStock" == input_line[0]:
        gift = input_line[1]
        for index, gifts in enumerate(name_of_the_gifts):
            if gifts == gift:
                name_of_the_gifts[index] = "None"
    elif "Required" == input_line[0]:
        gift_name = input_line[1]
        gift_index = int(input_line[2])
        for index, gifts in enumerate(name_of_the_gifts):
            if index == gift_index:
                name_of_the_gifts[index] = gift_name
                break
    elif "JustInCase" == input_line[0]:
        gift = input_line[1]
        for gifts in range(len(name_of_the_gifts)):
            name_of_the_gifts[-1] = gift
            break

    command = input()

result = []
for elements in name_of_the_gifts:
    if elements != "None":
        result.append(elements)

print(" ".join(result))
