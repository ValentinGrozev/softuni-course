def number_increment(numbers):
    def increase():
        increased = []
        for number in numbers:
            increased.append(number + 1)
        return increased

    return increase()


print(number_increment([1, 2, 3]))