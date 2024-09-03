import math


# My Original Solution -- 18 minutes
# Time Complexity: O(n*sqrt(n))
# Space Complexity: O(n)
# Idea: dp[i] = min(dp[i], dp[i-j*j]+1) for all j in range(1, sqrt(i)+1)
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        max_perf_root = math.floor(math.sqrt(n))
        for i in range(1, n + 1):
            cur_min = n
            for perfect_root in range(1, max_perf_root + 1):
                psq = perfect_root**2
                if i - psq < 0:
                    break
                if dp[i - psq] < cur_min:
                    cur_min = dp[i - psq]
            dp[i] = cur_min + 1

        return dp[n]
