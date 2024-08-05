from typing import List

# My Original Incorrect Solution -- 22 minutes
# I had some intuition on applying the 2D matrix stuff here,
# but there was no way I was gonna get it within a reasonable time.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * 3  # can only either buy or sell or cooldown
        # track max profit for each case
        # 0 == buy  # has val for next sell
        # 1 == sell  # can only report this price
        # 2 == cooldown  # cant report this, simply just value on cd
        for p in prices:
            cur_row = [0] * 3
            cur_row[0] = dp[2] + p if dp[2] else 0
            cur_row[1] = dp[0] if dp[0] and not dp[2] else 0
            cur_row[2] = dp[1] if dp[1] else 0
            dp = cur_row
        
        return dp[1]

# NeetCode Solution
# Time -- O(n)
# Space -- O(n) # only 2 states/index = buying or selling
# Interesting, so maybe there isn't any bottom-up solution to this.
# Maybe I should start with recursive memoized solutions...
# Come to think of it, I can always start with a recursive memoized sol'n
# in an interview and then ask the interviewer if that's okay or if
# I should go for the optimized true Dynamic Programming solution.
class NeetCodeSolution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2

        dp = {}  # key=(i, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)

