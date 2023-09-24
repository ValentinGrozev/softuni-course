upper_limit_for_hundreds = int(input())
upper_limit_for_tens = int(input())
upper_limit_for_units = int(input())

is_non_prime_number = False

for first_number in range(1, upper_limit_for_hundreds + 1):
    for second_number in range(1, upper_limit_for_tens + 1):
        if 2 <= second_number <= 7:
            for tmp in range(2, second_number):
                if second_number % tmp == 0:
                    is_non_prime_number = True
                    break
            if is_non_prime_number:
                is_non_prime_number = False
                continue
        else:
            continue
        for third_number in range(1, upper_limit_for_units + 1):
            if first_number % 2 == 0 and third_number % 2 == 0:
                print(f"{first_number} {second_number} {third_number}")
