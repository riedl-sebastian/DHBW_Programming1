# Coin Sums Project Euler

def coin_sums(total, coins):
    ways = [1] + [0]*total
    for coin in coins:
        for i in range(coin, total+1):
            ways[i] += ways[i-coin]
    return ways[total]

coins = [1, 2, 5, 10, 20, 50, 100, 200]
print(coin_sums(200, coins))
