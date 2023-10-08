def result(first, second, third):
    list_with_numbers = [first, second, third]
    counter = 0
    flag = False
    for digits in list_with_numbers:
        if digits < 0:
            counter += 1
        if digits == 0:
            flag = True
    if flag:
        return "zero"
    else:
        if counter == 1 or counter == 3:
            return "negative"
        else:
            return "positive"


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(result(first_number, second_number, third_number))
