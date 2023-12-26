numbers = input().split()
reverse_numbers_stack = []

while numbers:
    reverse_numbers_stack.append(numbers.pop())

print(" ".join(reverse_numbers_stack))
