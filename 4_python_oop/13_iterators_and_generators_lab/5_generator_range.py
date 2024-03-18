# First option:
def genrange(start: int, end: int):
    yield from list(range(start, end + 1))


print(list(genrange(1, 10)))


# Second option:
def genrange(start: int, end: int):
    current_index = start

    while current_index <= end:
        yield current_index
        current_index += 1


print(list(genrange(1, 10)))