def reverse_array(index, numbers):
    if index == len(numbers) // 2:
        print(' '.join(numbers))
        return
    numbers[index], numbers_list[len(numbers) - 1 - index] = numbers_list[len(numbers) - 1 - index], numbers[index]
    return reverse_array(index + 1, numbers)


numbers_list = input().split()
reverse_array(0, numbers_list)
