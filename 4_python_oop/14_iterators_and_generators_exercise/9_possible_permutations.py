from itertools import permutations


def possible_permutations(numbers):
    n = permutations(numbers)
    for permutation in n:
        yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]
