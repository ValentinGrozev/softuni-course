def nested_loops_to_recursion(index, vector_list, n):
    if index == len(vector_list):
        print(" ".join(str(x) for x in vector_list))
        return
    for number in range(1, n+1):
        vector_list[index] = number
        nested_loops_to_recursion(index + 1, vector_list, n)


number_of_loops = int(input())
vector = [0] * number_of_loops
nested_loops_to_recursion(0, vector, number_of_loops)