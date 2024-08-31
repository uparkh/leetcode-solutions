from typing import List

# My Original Recursive Memoization Solution -- 21 minutes
# Time and Space -- O(m*n)
# This is not a Hard problem, like what?
# I actually immediately saw it, and now I immediately see the DP solution
# as well, I was actually not that many steps away from the DP solution...
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # recursive memoization = O(m*n) time and space
        dp = {}  # (i, j) -> pathlength
        N, M = len(matrix), len(matrix[0])
        def dfs(i, j, prev_n):
            if (i < 0 or i >= N) or (j < 0 or j >= M):
                return 0
            n = matrix[i][j]
            if prev_n >= n:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            dp[(i, j)] = 1 + max(
                dfs(i+1, j, n), dfs(i-1, j, n),
                dfs(i, j+1, n), dfs(i, j-1, n)
            )
            return dp[(i, j)]
        
        res = 0
        for x in range(N):
            for y in range(M):
                res = max(dfs(x, y, -1), res)
 
        return res


# My Incorrect DP Solution -- 15 minutes
# Okay maybe that's harder than I thought. Really the only thing the DP
# solution would optimize is the memory complexity from O(n*m) -> O(m)
# I can very likely figure it out given enough time but it gets much more
# complex and harder to visualize for covering all the base cases so I'm going
# to give up now.
class DPSolution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M = len(matrix[0])
        dp = [0] * M  # aux row = any cells can flow into
        res = 0
        for i, row in enumerate(matrix):
            cur = [1] * M
            for j, num in enumerate(row):
                if j > 0:
                    if row[j-1] > num:
                        cur[j] = 1 + cur[j-1]
                    elif row[j-1] < num:
                        cur[j-1] += 1
                if i > 0:
                    prev_row = matrix[i-1]
                    if prev_row[j] > num:
                        cur[j] = max(cur[j], 1 + dp[j])
                    elif prev_row[j] < num:
                        dp[j] += 1
                res = max(res, cur[j], dp[j], cur[j-1])
            dp = cur
        
        return res


# NeetCode Solution
# Okay well this is my recursive memoization sol'n. And so is almost every
# other solution on the LeetCode page. Maybe some problems really only can
# be solved with recursive memoization...
class NeetCodeSolution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}  # (r, c) -> LIP

        def dfs(r, c, prevVal):
            if r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prevVal:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))
            dp[(r, c)] = res
            return res

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())


