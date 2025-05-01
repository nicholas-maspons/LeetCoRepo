# 322. Coin Change

class Solution(object):
    def coinChange(self, coins, amount):
        if amount == 0:
            return 0
            
        max_val = amount + 1 
        dp = [max_val] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                if dp[i - coin] != max_val:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == max_val:
            return -1
        else:
            return dp[amount]
