type_project = input()
number_of_rows = int(input())
number_of_columns = int(input())

all_seats = number_of_rows * number_of_columns
income = 0

if type_project == "Premiere":
    income = all_seats * 12
elif type_project == "Normal":
    income = all_seats * 7.50
elif type_project == "Discount":
    income = all_seats * 5.00
print(f"{income:.2f} leva")