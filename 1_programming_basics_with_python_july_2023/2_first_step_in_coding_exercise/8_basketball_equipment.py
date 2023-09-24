tax_per_year = int(input())

basket_shoes = tax_per_year - (tax_per_year * 0.4)
basket_suit = basket_shoes - (basket_shoes * 0.2)
basket_ball = basket_suit / 4
basket_acc = basket_ball / 5

total_cost = tax_per_year + basket_shoes + basket_suit + basket_ball + basket_acc

print(total_cost)





