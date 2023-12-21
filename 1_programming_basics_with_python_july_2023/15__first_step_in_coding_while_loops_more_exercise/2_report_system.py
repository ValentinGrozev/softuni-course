targeted_sum = int(input())
information = input()
card_payment = 0
card_payments_done = 0
cash_payment = 0
cash_payments_done = 0
total_collected_sum = 0
number_of_transactions = 0

while information != "End":
    item_price = int(information)
    number_of_transactions += 1
    if number_of_transactions % 2 != 0:
        if item_price > 100:
            print("Error in transaction!")
        else:
            cash_payment += item_price
            cash_payments_done += 1
            total_collected_sum += item_price
            print("Product sold!")

    else:
        if item_price < 10:
            print("Error in transaction!")
        else:
            card_payment += item_price
            card_payments_done += 1
            total_collected_sum += item_price
            print("Product sold!")

    if total_collected_sum >= targeted_sum:
        break

    information = input()

if total_collected_sum >= targeted_sum:
    print(f"Average CS: {(cash_payment / cash_payments_done):.2f}")
    print(f"Average CC: {(card_payment / card_payments_done):.2f}")
else:
    print("Failed to collect required money for charity.")
