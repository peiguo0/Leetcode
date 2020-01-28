class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        
        return -1 if dp[amount] == float('inf') else dp[amount]
    
'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Solution: DP, init with float('inf'), which means unreachable nodes, traverse all coins to figure out the minimal steps
Time: O(n*m)
Space" O(n)
'''
