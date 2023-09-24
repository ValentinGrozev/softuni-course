first_number_max_range = int(input())
second_number_max_range = int(input())
third_number_max_range = int(input())

is_non_prime_number = False

for first in range(1, first_number_max_range + 1):
    for second in range(1, second_number_max_range + 1):
        if 2 <= second <= 7:
            for tmp in range(2, second):
                if second % tmp == 0:
                    is_non_prime_number = True
                    break
            if is_non_prime_number:
                is_non_prime_number = False
                continue
        else:
            continue
        for third in range(1, third_number_max_range + 1):
            if first % 2 == 0 and third % 2 == 0:
                print(f"{first} {second} {third}")