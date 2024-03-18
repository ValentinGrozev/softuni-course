def squares(number: int):
    n = 1
    while n <= number:
        yield n * n
        n += 1


print(list(squares(5)))
