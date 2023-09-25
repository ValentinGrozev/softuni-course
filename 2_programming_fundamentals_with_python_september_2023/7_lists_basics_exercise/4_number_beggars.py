money_get = input()
count_of_beggars = int(input())

money_list = money_get.split(", ")
sum_beggar_bring_home = []
sum_beggar_bring_home_2 = [0] * count_of_beggars
current_beggar = 0

if len(money_list) == count_of_beggars:
    for index in range(len(money_list)):
        money = int(money_list[index])
        sum_beggar_bring_home.append(money)
    print(sum_beggar_bring_home)
elif len(money_list) < count_of_beggars:
    diff = count_of_beggars - len(money_list)
    for adds in range(diff):
        number = "0"
        money_list.append(number)
    for index in range(count_of_beggars):
        money = int(money_list[index])
        sum_beggar_bring_home.append(money)
    print(sum_beggar_bring_home)
else:
    for index in range(len(money_list)):
        money = int(money_list[index])
        sum_beggar_bring_home_2[current_beggar] += money
        if current_beggar < count_of_beggars - 1:
            current_beggar += 1
        else:
            current_beggar = 0
    print(sum_beggar_bring_home_2)
