def coin_calculator(current_coins, total_sum):
    used_coins = {}
    current_coins = sorted(current_coins, reverse=True)
    index = 0

    result = ''

    for coin in current_coins:
        if total_sum - coin < 0 and len(current_coins) - 1 > index:
            continue
        else:
            count_of_coin = total_sum // coin
            total_sum -= count_of_coin * coin
            used_coins[coin] = count_of_coin

        index += 1

    if total_sum == 0:
        result += f"Number of coins to take: {sum(used_coins.values())}\n"
    else:
        return "Error"

    for coin, coin_counter in used_coins.items():
        result += f"{coin_counter} coin(s) with value {coin}\n"

    return result


coins = [int(coin) for coin in input().split(", ")]
desired_sum = int(input())

print(coin_calculator(coins, desired_sum))