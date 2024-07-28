from typing import List

# My Original Solution -- 4 hours
# Time -- O(n^2)
# Space -- O(n)
# I forced myself to actually find the recursive top-down relationship
# and NOT look at the solution after 45 minutes on it. And it paid off.
# I have been struggling to put the intuition I felt into code for the last
# 4 problems and decided that I was gonna persevere and actually build
# the neural pathways for coding up a bottom-up solution, and I am SO
# INCREDIBLY PROUD of myself for actually managing to come up with this
# elegant solution.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        for j in range(len(s)):
            if s[:j+1] in wordDict:
                dp[j] = True
            else:
                for i in dp.keys():
                    if s[i+1:j+1] in wordDict:
                        dp[j] = True
                        break
        return len(s) - 1 in dp


# NeetCode Solution
# He approached it slightly differently.
# (1) From right to left, but that's reversible easily
# (2) Instead of checking different viable subranges, he checks
#     for if any combination of words can build the current range he is
#     checking.
# Functionally the recurrence relation is the same: any state depends on
# different combinations of the child state solving the subproblem.
class NeetCodeSolution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]

