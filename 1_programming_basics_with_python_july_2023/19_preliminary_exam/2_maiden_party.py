price_for_maiden_party = float(input())
number_of_love_messages = int(input())
number_of_wax_roses = int(input())
number_of_keychains = int(input())
number_of_caricatures = int(input())
number_of_lucky_surprises = int(input())

price_for_love_message = 0.60
price_for_wax_rose = 7.20
price_for_keychain = 3.60
price_for_caricature = 18.20
price_for_lucky_surprise = 22

income_from_love_messages = number_of_love_messages * price_for_love_message
income_from_wax_roses = number_of_wax_roses * price_for_wax_rose
income_from_keychains = number_of_keychains * price_for_keychain
income_from_caricatures = number_of_caricatures * price_for_caricature
income_from_lucky_surprises = number_of_lucky_surprises * price_for_lucky_surprise
all_income = income_from_love_messages + income_from_wax_roses + income_from_keychains + income_from_caricatures + \
             income_from_lucky_surprises

counter_of_all_sells = number_of_love_messages + number_of_wax_roses + number_of_keychains + number_of_caricatures + \
                       number_of_lucky_surprises

if counter_of_all_sells >= 25:
    all_income = all_income * (1 - 0.35)
    final_income = all_income * 0.90
else:
    all_income = all_income
    final_income = all_income * 0.90

if final_income >= price_for_maiden_party:
    diff = abs(final_income - price_for_maiden_party)
    print(f"Yes! {diff:.2f} lv left.")
else:
    diff = abs(final_income - price_for_maiden_party)
    print(f"Not enough money! {diff:.2f} lv needed.")



