def insertion_sort(nums):
    for idx in range(len(nums)):
        curr_idx = idx
        while curr_idx > 0 and nums[curr_idx] < nums[curr_idx - 1]:
            nums[curr_idx], nums[curr_idx - 1] = nums[curr_idx - 1], nums[curr_idx]
            curr_idx -= 1

    return " ".join(str(x) for x in nums)


numbers = [int(x) for x in input().split()]
print(insertion_sort(numbers))
