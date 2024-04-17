# first solution
def find_index(nums, target, index):
    middle_idx = len(nums) // 2

    if len(nums) == 1 and nums[0] != target:
        return -1

    if nums[middle_idx] == target:
        return middle_idx + index
    elif nums[middle_idx] > target:
        return find_index(nums[:middle_idx], target, index)
    elif nums[middle_idx] < target:
        index += len(nums[:middle_idx])
        return find_index(nums[middle_idx:], target, index)


numbers = [int(num) for num in input().split()]
target_num = int(input())
print(find_index(numbers, target_num, 0))


# second solution
def find_index(left_index, right_index, nums, target):
    middle_idx = (left_index + right_index) // 2

    if left_index > right_index:
        return -1

    if nums[middle_idx] == target:
        return middle_idx
    elif nums[middle_idx] > target:
        right_index = middle_idx - 1
        return find_index(left_index, right_index, nums, target)
    elif nums[middle_idx] < target:
        left_index = middle_idx + 1
        return find_index(left_index, right_index, nums, target)


numbers = [int(num) for num in input().split()]
target_num = int(input())
print(find_index(0, len(numbers) - 1, numbers, target_num))


# third solution
def find_index(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid_idx = (left + right) // 2

        if nums[mid_idx] == target:
            return mid_idx
        if nums[mid_idx] > target:
            right = mid_idx - 1
        else:
            left = mid_idx + 1

    return - 1


numbers = [int(num) for num in input().split()]
target_num = int(input())
print(find_index(numbers, target_num))
