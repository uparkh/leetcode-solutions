import math

# My Original Solution -- 5 minutes
# Time: O(1) -- large constant factor in binomial calculation
# Space: O(1)
# This problem was used in the tutorial so I already knew the 2D DP
# bottom-up solution, I figured I'd try implementing the combination/binomial
# solution for fun.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(n + m - 2, m - 1)

# NeetCode Solution
class NeetCodeSolution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for _ in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

        # O(n * m) O(n)

