string_information = input().split()

inspected_number = ""
position_of_element_in_alphabetical = 0
sum_of_all_numbers = 0

for element in range(len(string_information)):
    needed_element = (string_information[element])
    inspected_number = needed_element[1:-1]
    if needed_element[0].isupper():
        position_of_element_in_alphabetical_according_ASCII = ord(needed_element[0])
        position_of_element_in_alphabetical = position_of_element_in_alphabetical_according_ASCII - 64
        sum_of_all_numbers += int(inspected_number) / position_of_element_in_alphabetical
    elif needed_element[0].islower():
        position_of_element_in_alphabetical_according_ASCII = ord(needed_element[0])
        position_of_element_in_alphabetical = position_of_element_in_alphabetical_according_ASCII - 96
        sum_of_all_numbers += int(inspected_number) * position_of_element_in_alphabetical
    if needed_element[-1].isupper():
        position_of_element_in_alphabetical_according_ASCII = ord(needed_element[-1])
        position_of_element_in_alphabetical = position_of_element_in_alphabetical_according_ASCII - 64
        sum_of_all_numbers -= position_of_element_in_alphabetical
    elif needed_element[-1].islower():
        position_of_element_in_alphabetical_according_ASCII = ord(needed_element[-1])
        position_of_element_in_alphabetical = position_of_element_in_alphabetical_according_ASCII - 96
        sum_of_all_numbers += position_of_element_in_alphabetical

print(f"{sum_of_all_numbers:.2f}")
