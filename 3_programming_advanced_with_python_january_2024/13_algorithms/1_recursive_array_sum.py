def sum_of_elements(numbers, index=0):
    if index == len(numbers) - 1:
        return numbers[index]
    return numbers[index] + sum_of_elements(numbers, index + 1)


input_numbers = [int(number) for number in input().split(" ")]

print(sum_of_elements(input_numbers))
