def binary_search(num, target):
    left = 0
    right = len(num) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_el = num[mid_idx]

        if mid_el == target:
            return mid_idx
        elif mid_el < target:
            left = mid_idx + 1
        elif mid_el > target:
            right = mid_idx - 1

    return -1


numbers = [int(x) for x in input().split()]
searched_number = int(input())

print(binary_search(numbers, searched_number))
