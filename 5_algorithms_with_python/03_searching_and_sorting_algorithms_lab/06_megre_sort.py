def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    if len(nums) == 2:
        if nums[0] > nums[1]:
            nums[0], nums[1] = nums[1], nums[0]
        return nums

    mid_element = len(nums) // 2
    left_part = nums[:mid_element]
    right_part = nums[mid_element:]

    left_result = merge_sort(left_part)
    right_result = merge_sort(right_part)

    left_pointer = 0
    right_pointer = 0
    sorted_numbers = []

    while left_pointer < len(left_result) and right_pointer < len(right_result):
        if left_result[left_pointer] > right_result[right_pointer]:
            sorted_numbers.append(right_result[right_pointer])
            right_pointer += 1
        else:
            sorted_numbers.append(left_result[left_pointer])
            left_pointer += 1

    if left_pointer < len(left_result):
        sorted_numbers += left_result[left_pointer:]

    if right_pointer < len(right_result):
        sorted_numbers += right_result[right_pointer:]

    return sorted_numbers


numbers = [int(x) for x in input().split()]
result = merge_sort(numbers)
print(' '.join(str(num) for num in result))
