numbers_count = int(input())

max_diff = 0
prev_sum = 0
is_first_iter = True


for _ in range(numbers_count):
    first = int(input())
    second = int(input())
    number_sum = first + second

    if is_first_iter:
        is_first_iter = False
        prev_sum = number_sum

    if max_diff < abs(number_sum - prev_sum):
        max_diff = abs(number_sum - prev_sum)
    prev_sum = number_sum

if max_diff == 0:
    print(f"Yes, value={prev_sum}")
else:
    print(f"No, maxdiff={max_diff}")
