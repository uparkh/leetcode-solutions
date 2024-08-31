# My Attempt at the Problem
# Tried my best, couldn't even find the recurrence relation. No way I was
# gonna be able to solve this in 30 minutes. Wipe my ego and let's keep going.
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = 0
        cur_text1 = text1
        # print(f'text2: {text2}')
        for c in text2:
            if not cur_text1:
                break
            # print(c, cur_text1)
            search1 = cur_text1.find(c)
            if search1 >= 0:
                cur_text1 = cur_text1[search1+1:]
                res += 1
            # print(search1, res)
        return res

# After seeing some dude in the YT vid comments mentioning 2D Matrix,
# I immediately knew what he was talking about and implemented this non
# functional DP solution. Couldn't quite figure out how to handle duplicates.
class InspiredSolution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N, M = len(text1), len(text2)
        prev_row = [0] * (M + 1)
        for i in range(N-1, -1, -1):
            cur_row = [0] * (M + 1)
            c1 = text1[i]
            for j in range(M-1, -1, -1):
                c2 = text2[j]
                cur_row[j] = max(prev_row[j], cur_row[j+1])
                if c1 == c2:
                    cur_row[j] += 1
            prev_row = cur_row
        return prev_row[0]


# NeetCode Solution

# Ahhh, very clever, looks diagonally in the 2D matrix. Because the equality
# case is literally jsut wrapping the substring.
# Very cool
class NeetCodeSolution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]



