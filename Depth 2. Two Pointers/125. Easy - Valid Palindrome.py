# My solution is quite easy to read, but it does use O(n) extra memory. I could have avoided that
# by just iterating over the original string, skipping any non-alphanumeric characters, needing
# no extra memory.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        operand = ''.join(c.lower() for c in s if c.isalnum())
        # print(operand)
        for i in range(len(operand)//2):
            if operand[i] != operand[-i-1]:
                return False
        return True
    
#NeetCode Solution, alnum checking is done via lexicographic comparison.
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l, r = 0, len(s) - 1
#         while l < r:
#             while l < r and not self.alphanum(s[l]):
#                 l += 1
#             while l < r and not self.alphanum(s[r]):
#                 r -= 1
#             if s[l].lower() != s[r].lower():
#                 return False
#             l += 1
#             r -= 1
#         return True

#     # Could write own alpha-numeric function
#     def alphanum(self, c):
#         return (
#             ord("A") <= ord(c) <= ord("Z")
#             or ord("a") <= ord(c) <= ord("z")
#             or ord("0") <= ord(c) <= ord("9")
#         )


print(Solution().isPalindrome(".,"))
