def push(stack, number):
    stack.append(number)
    return stack


def pop(stack):
    stack.pop()
    return stack


def maximum_number(stack):
    print(max(stack))


def minimum_number(stack):
    print(min(stack))


def final_query(stack):
    reversed_stack = []
    while stack:
        reversed_stack.append(stack.pop())
    reversed_stack = [str(x) for x in reversed_stack]
    return ", ".join(reversed_stack)


def main():
    stack = []
    number_of_queries = int(input())

    for query in range(number_of_queries):
        current_query = input().split()
        if current_query[0] == "1":
            push(stack, int(current_query[1]))
        elif stack:
            if current_query[0] == "2":
                pop(stack)
            elif current_query[0] == "3":
                maximum_number(stack)
            elif current_query[0] == "4":
                minimum_number(stack)
    print(final_query(stack))


main()
