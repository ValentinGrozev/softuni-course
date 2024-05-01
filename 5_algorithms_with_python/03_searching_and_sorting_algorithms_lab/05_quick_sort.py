def quick_sort(start_index, end_index, nums):
    if start_index >= end_index:
        return

    pivot_index = start_index
    left_pointer = start_index + 1
    right_pointer = end_index

    while left_pointer <= right_pointer:
        if nums[left_pointer] > nums[pivot_index] > nums[right_pointer]:
            nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
        if nums[left_pointer] <= nums[pivot_index]:
            left_pointer += 1
        if nums[right_pointer] >= nums[pivot_index]:
            right_pointer -= 1

    nums[pivot_index], nums[right_pointer] = nums[right_pointer], nums[pivot_index]
    quick_sort(start_index, right_pointer - 1, nums)
    quick_sort(left_pointer, end_index, nums)


numbers = [int(x) for x in input().split()]
quick_sort(0, len(numbers) - 1, numbers)

print(*numbers)
