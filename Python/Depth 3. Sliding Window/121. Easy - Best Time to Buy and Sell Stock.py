# My First Attempt - O(n^2) Solution
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         if len(prices) <= 1: return 0

#         maxP = 0
#         l, r = 0, 0
#         while l < len(prices) - 1:
#             if l == r:
#                 currMax_i = l+1
#                 for i in range(l+1, len(prices)):
#                     if prices[i] > prices[currMax_i]: currMax_i = i
#                 r = currMax_i
#             else:
#                 maxP = max(maxP, prices[r] - prices[l])
#                 l += 1

        # return maxP


# Notes:
# It seems that a 'sliding window' is an algorithm pattern where there's a left and right side
# of a window that iterates over the list/array/string, and processing is done based on this
# growing and shrinking window.

# Improved Solution - O(n) Solution
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2: return 0

        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
                r = l + 1
            else:
                maxP = max(maxP, prices[r] - prices[l])
                r += 1

        return maxP
        
# NeetCode Solution
# In my solution, I keep track of the lowest encountered value in the left side of the window,
# so does he, but he doesn't encode it in an index, just keeping track of it as he iterates over it.
# Notice that in my solution, R just iterates through the list once, so there's no need to have
# a separate variable tracker for it. But other than that, the fundamental logic is the same as
# mine.

# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         res = 0
        
#         lowest = prices[0]
#         for price in prices:
#             if price < lowest:
#                 lowest = price
#             res = max(res, price - lowest)
#         return res

    
print(Solution().maxProfit([7,1,5,3,6,4]))

