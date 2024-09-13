from typing import List

# My DP Sol'n attempt, apparently bottom-up DP is not easily possible here?
class DPSolution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [[''] for _ in range(len(s) + 1)]
        for l in range(len(s) - 1, -1, -1):
            # print(s[l])
            dp[l] = dp[l+1]
            word_found = False
            for r in range(l+1, len(s)):
                word = s[l:r+1]
                # print(word)
                if word in wordDict:
                    if not word_found:
                        dp[l] = []
                        word_found = True
                    for remainder in dp[l+1]:
                        if remainder:
                            dp[l].append(word + ' ' + remainder)
                        else:
                            dp[l].append(word)
        print(dp)
        return dp[0]


# My Original Recursive Sol'n
# Time: O(2^n) - Exponential
# Space: O(2^n) - Exponential
# Guess a top-down memoization approach truly is the optimal solution...
# I only see one mode in the LeetCode time complexity distribution, and it's the top-down 
# memoization approach, so any other variance in runtime is random.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache = {}  # (i, j) -> concated strs

        def dfs(l, r):
            if l >= len(s):
                return []
            if (l, r) in cache:
                return cache[(l, r)]
            while s[l:r] not in wordDict and r <= len(s):
                r += 1
            word = s[l:r]
            if r > len(s):
                return []
            if r == len(s):
                return [word]
            left = dfs(r, r + 1) # take
            right = dfs(l, r + 1) # skip
            cur = []
            for subL in left:
                cur.append(word + ' ' + subL)
            for subR in right:
                cur.append(subR)
            cache[(l, r)] = cur
            return cache[(l, r)]

        return dfs(0, 1)



tc0 = ("catsanddog", ["cat", "cats", "and", "sand", "dog"])
# tc1 = ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
print(Solution().wordBreak(*tc0))

