def drawing_function(n):
    if n == 0:
        return

    print("*" * n)
    drawing_function(n - 1)
    print("#" * n)


number = int(input())
drawing_function(number)
