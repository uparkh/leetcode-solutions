# My Original Solution - O(log n)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# When doing it in normal array, condition to lower range is (med < l) or (med < r)

# Case 1
# [120, 130, 0, 1, 2, 3, 4, 5, 6, 7, 44, 55, 66, 77, 88, 99, 100, 110]
#  0    1    2  3  4  5  6  7  8  9  10  11  12  13  14  15  16   17

# Case 2
# [44, 55, 66, 77, 88, 99, 100, 110, 120, 130, 0, 1, 2, 3, 4, 5, 6, 7]
#  0   1   2   3   4   5   6    7    8    9   10 11 12 13 14 15 16 17

# Add new condition for this, knowing the rotations are ALWAYS clockwise:
# only change l and r if they correspond to the lowest element value.
#   - well scratch that, because since this is sorted, the lowest of the 2 is always going to be
#     on the right side, so only condition for right shifting is (nums[med] < nums[r])
# if (nums[med] > nums[l]) -> bring l to med + 1
# obviously keep track of the lowest medians encountered in the res variable


class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = float("infinity")
        l, r = 0, len(nums) - 1
        while l <= r:
            med = (l + r) // 2
            res = min(nums[med], res)
            if (nums[med] <= nums[r]):
                r = med - 1
            elif (nums[med] >= nums[l]):
                l = med + 1
        return res

# NeetCode Solution - O(log n)
# Tiny bit more optimized. I realize that you don't have to do "or equal than" checking, because
# right before the action that causes (l == r), median will already have been recorded.

# Additionally, we don't have to do the condition of testing if nums[med] is bigger than left side.
# Since it's a rotated SORTED array, we already know for a fact that if nums[med] isn't less than
# nums[r], it MUST be greater than the left side. So we can save on that comparison.

# His conditions are also different. His asks whether the right side is the smaller than the median.
# If so, then that means that the right half range contains the min (case 2), if not, then the left
# range contains the min.
# My solution asks whether the median value is the biggest of the l and r and med, or the smallest,
# and adjusts the ranges accordingly.
# What I can't understand is why mine performs in 55% while his performs in 99% time.
# Okay, nevermind, it seems to be quite random what the time and memory performance turns out to be.

# Ohhhh wait actually I understand why. The distributions for runtime and memory seem to be normal,
# meaning that there is some element of randomness definitely present.
# If there actually was some fundamental algorithm optimization missing, then I would see 
# 2 distinct "pockets" in the histogram. But it seems to average one value, while being distributed,
# so in these cases computer hardware randomness comes into play.

# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         start , end = 0 ,len(nums) - 1 
#         curr_min = float("inf")
        
#         while start  <  end :
#             mid = (start + end ) // 2
#             curr_min = min(curr_min,nums[mid])
            
#             # right has the min 
#             if nums[mid] > nums[end]:
#                 start = mid + 1
                
#             # left has the  min 
#             else:
#                 end = mid - 1 
                
#         return min(curr_min,nums[start])

print(Solution().findMin([120, 130, 0, 1, 2, 3, 4, 5, 6, 7, 44, 55, 66, 77, 88, 99, 100, 110]))
