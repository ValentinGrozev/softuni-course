number_of_queries = int(input())
stack = []

command_func = {
    1: lambda x: stack.append(x[1]),
    2: lambda x: stack.pop() if stack else None,
    3: lambda x: print(max(stack)) if stack else None,
    4: lambda x: print(min(stack)) if stack else None,
}

for _ in range(number_of_queries):
    numbers = ([int(number) for number in input().split()])
    command = numbers[0]
    command_func[command](numbers)

stack.reverse()

print(*stack, sep=", ")
