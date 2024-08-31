from typing import List

# My Original Solution -- 40 minutes
# Time -- O(n * amount)
# Space -- O(amount)
# Really proud of myself for being able to apply unbounded knapsack!
# I instantly recognized the application here, and after drawing it out,
# it became super super manageable to implement. Really satisfying to see
# it work!
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # (c, cur_amt) -> ways to get that amt for coin c 
        dp = [int(amt_rem % coins[0] == 0) for amt_rem in range(amount + 1)]
        # print(f'Row 0: {dp}')
        # dp = {}  # (c, cur_amt) -> ways to get to that amt num
        # for i, c in enumerate(coins[1:]):
        for c in coins[1:]:
            cur_row = [0] * (amount + 1)
            for amt_rem in range(amount+1):
                cur_row[amt_rem] = dp[amt_rem]
                if amt_rem >= c:
                    cur_row[amt_rem] += cur_row[amt_rem - c]
            dp = cur_row
            # print(f'Row {i+1}: {dp}')

        return dp[-1]


# NeetCode Solutions
# I really should have started with memoization first, but I instantly
# saw the hidden unbounded knapsack problem so I went for the most optimized
# solution first.
# I do realize that he has an even better optimization:
# he doesn't preset the first row. Recognize that the row-by-row loop
# will populate that first row as needed, without expensive modulo operations.
class NeetCodeSolution:
    def change(self, amount: int, coins: List[int]) -> int:
        # MEMOIZATION
        # Time: O(n*m)
        # Memory: O(n*m)
        cache = {}

        def dfs(i, a):
            if a == amount:
                return 1
            if a > amount:
                return 0
            if i == len(coins):
                return 0
            if (i, a) in cache:
                return cache[(i, a)]

            cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return cache[(i, a)]

        return dfs(0, 0)

        # DYNAMIC PROGRAMMING
        # Time: O(n*m)
        # Memory: O(n*m)
        dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
        dp[0] = [1] * (len(coins) + 1)
        for a in range(1, amount + 1):
            for i in range(len(coins) - 1, -1, -1):
                dp[a][i] = dp[a][i + 1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]

        # DYNAMIC PROGRAMMING
        # Time: O(n*m)
        # Memory: O(n) where n = amount
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for a in range(1, amount + 1):
                nextDP[a] = dp[a]
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]

        

