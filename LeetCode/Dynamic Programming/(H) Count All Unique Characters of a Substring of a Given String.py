from collections import Counter

# My Original Solution -- 33 minutes
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# I'm sure if I was smarter about unique character count, this would be a lot faster
# than summing up the values of the Counter object.
# But this solution is at the very least correct, just slow.
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        cache = {}  # (l, r) interval -> int result to uniqueLetterString
        def dfs(l, r):
            if (l, r) in cache:
                return 0
            if l == r:
                cache[(l, r)] = 1
                return cache[(l, r)]
            cache[(l, r)] = (
                dfs(l, r - 1) + dfs(l + 1, r)
                +
                sum([v == 1 for v in Counter(s[l:r+1]).values()])
            )
            return cache[(l, r)]

        dfs(0, len(s)-1)
        return cache[(0, len(s) - 1)]

# This explanation covers why my brute force above is not fast and how to speed it up:
# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/solutions/1505263/single-pass-o-n-time-and-o-1-space-solution-with-detailed-explanation/?envType=problem-list-v2&envId=dynamic-programming