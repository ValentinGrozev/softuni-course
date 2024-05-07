def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums.pop()

    greater_numbers = []
    lower_numbers = []

    for num in nums:
        if num > pivot:
            greater_numbers.append(num)
        else:
            lower_numbers.append(num)

    return quick_sort(lower_numbers) + [pivot] + quick_sort(greater_numbers)


numbers = [int(x) for x in input().split()]
print(*quick_sort(numbers))
