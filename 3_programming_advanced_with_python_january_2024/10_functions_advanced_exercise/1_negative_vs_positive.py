def positive_and_negative_sums(any_numbers):
    positives_sum = 0
    negatives_sum = 0
    for number in any_numbers:
        if number >= 0:
            positives_sum += number
        else:
            negatives_sum += number

    def check_which_is_bigger():
        if abs(positives_sum) > abs(negatives_sum):
            return "The positives are stronger than the negatives"
        else:
            return "The negatives are stronger than the positives"

    return f"{negatives_sum}\n{positives_sum}\n{check_which_is_bigger()}"


numbers = [int(x) for x in input().split()]
print(positive_and_negative_sums(numbers))
