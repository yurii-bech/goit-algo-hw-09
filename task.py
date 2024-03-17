def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            result[coin] = amount // coin
            amount %= coin
    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coins_used = [[] for _ in range(amount + 1)]

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coins_used[i] = coins_used[i - coin] + [coin]

    result = {}
    for coin in coins_used[amount]:
        result[coin] = result.get(coin, 0) + 1
    return result

# Приклад використання функцій
amount = 113
print("Жадібний алгоритм:")
print(find_coins_greedy(amount))
print("Динамічне програмування:")
print(find_min_coins(amount))