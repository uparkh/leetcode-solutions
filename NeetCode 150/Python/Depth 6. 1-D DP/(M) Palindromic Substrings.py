# My Original Solution -- 5 minutes
# Time -- O(n^2)
# Memory -- O(1)
# Yeah this one is super straightforward coming off the back of 
# Longest Palindrome Substring...
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # odd palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            # even palindromes
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
        return res

# NeetCode Solution
# Functionally does the exact same thing I'm doing, but he split it up
# to DRY and avoid code duplication.
class NeetCodeSolution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.countPali(s, i, i)
            res += self.countPali(s, i, i + 1)
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res

