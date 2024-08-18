# My Original (Almost) Solution -- 40 minutes
# This passed almost all test cases first try, but I just could not figure
# out this one edge case, and it's too complex of an edge case for me
# to figure out, and I want to move on. I am pretty proud of being able
# to get really close to a supremely optimized solution. This problem
# built on the Distinct Subsequences problem, for the DP sol'n.

# Okay, I immediately figured it out after glancing at the NeetCode solution...
# when the letters are the same, just take the diagonal subproblem result
# directly, otherwise there's incorrect logic with considering the cardinal
# subproblems and then adding one operation to them. 
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N, M = len(word1), len(word2)
        dp = [m for m in range(M, -1, -1)]
        for i in range(N-1, -1, -1):
            cur = [0] * (M + 1)
            cur[-1] = N - i
            for j in range(M-1, -1, -1):
                cur[j] = dp[j+1] if word1[i] == word2[j] \
                        else 1 + min(dp[j], dp[j+1], cur[j+1])
            dp = cur
        return dp[0]


# NeetCode Solution
# No clue what the hell he's doing with 'inf' here, I mean I guess
# it makes sense, because taking the min bypasses these values for the first
# iter, but I think it's less clean, and I purposely initialized them to
# values that make sense (to get reconstruct word2 from empty word1, only
# insertions are required)
class NeetCodeSolution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])
        return int(dp[0][0])


