def bubble_sort(nums):
    for idx in range(len(nums)):
        for curr_idx in range(idx + 1, len(nums)):
            if nums[idx] > nums[curr_idx]:
                nums[idx], nums[curr_idx] = nums[curr_idx], nums[idx]

    return " ".join(str(x) for x in nums)


numbers = [int(x) for x in input().split()]
print(bubble_sort(numbers))
