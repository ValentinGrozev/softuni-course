def rounded_numbers(list_with_numbers: list):
    final_list = []
    for number in list_with_numbers:
        number = float(number)
        final_list.append(round(number))
    return final_list


list_of_numbers_as_string = input().split()
print(rounded_numbers(list_of_numbers_as_string))