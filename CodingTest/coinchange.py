# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.


# class Solution(object):
#     def coinChange(self, coins: 'List[int]', amount = 'int') -> 'int':
#         dp = [0] + [float('inf') for i in range(amount)]
#         for i in range(1,amount+1):
#             for coin in coins:
#                 if i-coin >= 0:
#                     dp[i] = min(dp[i],dp[i-coin]+1) 
#                     #dp[i] is the fewest number of coins making up amount i 
#                     # then for every coin in coins, dp[i] = min(dp[i-coin]+1)
#             if dp[-1] == float('inf'):
#                 return -1
#         return dp[-1]
                

# 여기서부터
def coinChange(coins, amount) :
    dp = [float('Inf')]*(amount+1)
    dp[0] = 0
    coins.sort()
    for i in range(1,amount+1):
        temp = [float('Inf')]
        for c in coins:
            if i-c<0:
                break
            temp.append(dp[i-c])
        dp[i] = min(temp)+1

    return dp[amount] if dp[amount] != float('Inf') else -1

coins = [1,2,5]
amount = 11
print(coinChange(coins,amount))