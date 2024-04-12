def generate01(index, vector_list):
    if index == len(vector_list):
        print(''.join(str(num) for num in vector_list))
        return
    for number in range(0, 2):
        vector_list[index] = number
        generate01(index + 1, vector_list)


n = int(input())
vector = [0] * n
generate01(0, vector)
