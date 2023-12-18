# Intuitive, set-based approach, O(n), fails when duplicate substrings are not adjacent.
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         encountered = set()
#         longest = 0
#         for c in s:
#             if c not in encountered:
#                 encountered.add(c)
#             else:
#                 longest = max(longest, len(encountered))
#                 encountered.clear()
#                 encountered.add(c)
#         longest = max(longest, len(encountered))
#         return longest

# My Original Solution, O(n), at worst, 2 passes through the string. Sets are really useful for
# duplicate testing.
# Done in 42 mins.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: return len(s)
        encountered = set()
        l = 0
        longest = 0
        for r, c in enumerate(s):
            if c in encountered:
                # longest = max(longest, r - l)
                while c != s[l] and l < r:
                    encountered.remove(s[l])
                    l += 1
                l += 1
            encountered.add(c)
            longest = max(longest, len(encountered))
        
        return longest


# NeetCode Solution, O(n). I had the same intuition/idea as him, but his code is just a little
# cleaner. The idea being to advance the left pointer of the window until the right side
# duplicate character is not in the window.

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         charSet = set()
#         l = 0
#         res = 0

#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l += 1
#             charSet.add(s[r])
#             res = max(res, r - l + 1)
#         return res
            
print(Solution().lengthOfLongestSubstring("dvdf"))
print(Solution().lengthOfLongestSubstring("a"))

