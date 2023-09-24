number = input()

prime_number_sum = 0
non_prime_number_sum = 0
flag = False

while number != "stop":
    current_number = int(number)
    if current_number < 0:
        print("Number is negative.")
        number = input()
        continue

    if current_number == 1:
        prime_number_sum += current_number
    if current_number > 1:
        for i in range(2, current_number):
            if (current_number % i) == 0:
                flag = True
                break
    if flag:
        non_prime_number_sum += current_number
        flag = False
    else:
        prime_number_sum += current_number

    number = input()

print(f"Sum of all prime numbers is: {prime_number_sum}")
print(f"Sum of all non prime numbers is: {non_prime_number_sum}")