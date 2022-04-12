def change_money(money, coins):
    import math

    min_count_coins = [0] + [math.inf] * money
    for m in range(1, money+1):
        for coin in coins:
            if coin <= m:
                num_coins = min_count_coins[m-coin] + 1
                if num_coins < min_count_coins[m]:
                    min_count_coins[m] = num_coins

    return min_count_coins[money]
