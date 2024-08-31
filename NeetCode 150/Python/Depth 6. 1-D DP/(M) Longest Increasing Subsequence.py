from typing import List

# I just could not figure out the O(n log(n)) solution to this problem.
# I was right there with figuring I needed binary search/binary search tree of
# some kind, but with Python not having a BST built-in, and me not feeling
# like implementing one, I thought there may be some even more clever way
# of doing this problem. I figured out the DP bottom-up relationship, though,
# so I guess that's something! I know the algorithm for DP-ing it up, maybe
# I should code it.. nah I wanna be done with this problem.

# After 4 days on and off thinking about this I think I am ready to give up.
# At least I gave it my all.

# NeetCode Solution
# Makes sense -- always adding 1 or keeping the current LIS to previous
# essentially what I had
class NeetCodeSolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)


# hiepit Solution
# Time -- O(n log(n))
# Space -- O(n), can get to O(1) if overwrite original array (one ptr)
# Yup I intuitively knew some form of BST/Binary Search was at play here
# Essentially when going through [2, 6, 8, 3, 4, 5, 1] with DP, you end with
# 3 subsequence arrays:
# i = 0: [2]
# i = 1: [2, 6]
# i = 2: [2, 6, 8]
# i = 3: [2, 6, 8], [2, 3]
# i = 4: [2, 6, 8], [2, 3, 4]
# i = 5: [2, 6, 8], [2, 3, 4, 5]
# i = 6: [2, 6, 8], [2, 3, 4, 5], [1]
# At each step if nums[i] < subX[i-1], realize we can simply substitute
# in the least possible value to keep the sequence length the same, yet
# allow for expansion of the subsequence. So instead we get:

# i = 0: [2]
# i = 1: [2, 6]
# i = 2: [2, 6, 8]
# i = 3: [2, 3, 8]
# i = 4: [2, 3, 4]
# i = 5: [2, 3, 4, 5]
# i = 6: [1, 3, 4, 5]

# The minimum at any index is always pushed as far backas it can be,
# to allow the longest possible expansion.
# Pretty clever stuff, and while I am regretting I spent all that time 
# trying to figure this out (which would have taken forever), at least I get
# the faster solution. I'd be hard pressed if they ask me this in an interview
# *without* a hint, though >:|

class BisectSolution:  # 68 ms, faster than 93.92%
    def bisect_left(self, arr: List[int], ndl):
        # Find the index of the first element >= x
        l, r = 0, len(arr) - 1
        while l < r:
            i = (l + r) // 2
            if ndl <= arr[i]:
                r = i
            elif ndl > arr[i]:
                l = i + 1
        return r

    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = self.bisect_left(sub, x)
                sub[idx] = x  # Replace that number with x
        return len(sub)


