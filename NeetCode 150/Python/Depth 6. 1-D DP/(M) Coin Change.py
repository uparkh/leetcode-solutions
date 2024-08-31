from typing import List

# My Original Incorrect Solution
# I just knew I am not gonna be getting this one right...
# I don't see the vision, the recurrence relation isn't clear, and
# I have no clue how to code this up. These problems are so difficult man...
# No clue how to use DP here.

# From NC video: I realize I STILL did not make a honest decision tree.
# I tried forcing a decision tree from a sorted list of coins. I need
# to be thinking of ALL possible decisions, not where I want to start.

# Also from NC vid: The subproblem here is "value remaining".
# If there are 9 cents remaining, and any coin can be chosen, then
# it doesn't matter which coins you chose before that, there's gonna be
# repeated/cached work for optimal way to get 9 cents.
# Again, THINK ABOUT INVERTING THE GOAL!!!

# KEY point: tabulate from lower amounts -> needed amonut
# dp[0] = ??  # amt of coins to satisfy 0 remaining amount
# dp[1] = ??  # amt of coins to satisfy 1 remaining amount
# dp[2] = ??  # amt of coins to satisfy 2 remaining amount
# ...

# dp[x] = min([1 + dp[x-c] for c in coins])

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)  # maybe something else faster later
        ncoins = 0
        curval = 0
        for c in coins:
            while curval + c < amount:
                curval += c
                ncoins += 1
        return ncoins


# My Solution After Viewing NC's Explanation
class ModdedSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for amt_rem in range(1, amount+1):
            for c in coins:
                # print(dp, amt_rem, c)
                if amt_rem - c >= 0:
                    dp[amt_rem] = min(dp[amt_rem], 1 + dp[amt_rem - c])
        if dp[amount] == float('inf'):
            return -1
        return int(dp[amount])


# NeetCode's Solution
# Pretty much the same as my modded solution, he just used `amount + 1` as
# 'infinity'.
class NeetCodeSolution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1

