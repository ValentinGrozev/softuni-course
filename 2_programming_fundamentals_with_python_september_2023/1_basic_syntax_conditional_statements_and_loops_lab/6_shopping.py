budget = int(input())
user_input = input()

cost = 0

while user_input != "End":
    product_price = int(user_input)
    cost += product_price
    if cost > budget:
        print("You went in overdraft!")
        break

    user_input = input()

else:
    print("You bought everything needed.")