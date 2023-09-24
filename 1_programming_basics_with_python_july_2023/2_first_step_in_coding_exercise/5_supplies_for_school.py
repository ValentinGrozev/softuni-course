package_with_pens = int(input())
package_with_markers = int(input())
detergent = int(input())
discount = int(input())

price_for_package_pens = 5.80
price_for_package_markers = 7.20
price_for_lit_of_detergent = 1.20

total_price_pens = package_with_pens * price_for_package_pens
total_price_markers = package_with_markers * price_for_package_markers
total_price_detergent = detergent * price_for_lit_of_detergent

total_price_all = total_price_pens + total_price_markers + total_price_detergent
discount_sum = total_price_all * (discount / 100)
final_price = total_price_all - discount_sum

print(final_price)