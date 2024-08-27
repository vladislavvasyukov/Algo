from collections import defaultdict


def solution(coins, amount):
    if len(coins) == 0 or amount == 0:
        return []

    # Инициализируем массив для хранения минимального количества монет для каждой суммы
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Для суммы 0 нужно 0 монет

    # Заполняем массив dp
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Если не найдено решение, возвращаем пустой список
    if dp[amount] == float('inf'):
        return []

    # Восстанавливаем набор монет
    tmp = defaultdict(int)
    while amount > 0:
        for coin in coins:
            if amount >= coin and dp[amount] == dp[amount - coin] + 1:
                tmp[coin] += 1
                amount -= coin
                break

    return [tmp.get(coin, 0) for coin in coins]


"""

# import requests
# import mysql.connector
# import pandas as pd
from collections import defaultdict
from math

def solution2(coins, target_amount):
    if target_amount == 0 or len(coins) == 0:
        return []

    data = defaultdict(int)
    current_index_coin = len(coins) - 1
    while target_amount or current_index_coin >= 0:
        # [][-1] -> raise
        if target_amount < coins[current_index_coin]:
            current_index_coin -= 1
            continue

        target_amount -= coins[current_index_coin]
        data[coins[current_index_coin]] += 1

    if target_amount > 0:
        return []

    return [data[coin] for coin in coins]


def solution(coins, target_amount):
    if target_amount == 0 or len(coins) == 0:
        return []

    # data = {}
    # min_coins_value = [None for _ in range(target_amount + 1)]
    # for money in range(1, target_amount + 1):


    for i, coin in enumerate(coins): # [1, 9, 10]
        tmp = solution(coins, target - coins)
        tmp[i] += 1





        curr_num = min_coins_value[money - coin] + 1
        if curr_name < min_coins_value[money]:

            min_coins_value[money] = curr_name # {1: 0, 3: 1, 5: 0}

    return [] # here we need to use data





НУЖНО ПОПРОБОВАТЬ ПОСТРОИТЬ ДЕРЕВО
"""


def test1():
    coins = [1, 2, 3, 5]
    target_amount = 37
    assert solution(coins, target_amount) == [0, 1, 0, 7]


def test2():
    coins = [1, 2, 3, 5]
    target_amount = 200
    assert solution(coins, target_amount) == [0, 0, 0, 40]


def test3():
    coins = [1, 2, 3, 5]
    target_amount = 0
    assert solution(coins, target_amount) == []


def test4():
    coins = []
    target_amount = 100
    assert solution(coins, target_amount) == []


def test5():
    coins = [1, 9, 10]
    target_amount = 18
    assert solution(coins, target_amount) == [0, 2, 0]


if __name__ == '__main__':
    test1()
    test2()
    test3()
    test4()
    test5()
