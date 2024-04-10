def sum_numbers(numbers, index):
    if index == len(numbers) - 1:
        return numbers[index]
    return numbers[index] + sum_numbers(numbers, index + 1)


num_list = [int(x) for x in input().split()]
print(sum_numbers(num_list, 0))
