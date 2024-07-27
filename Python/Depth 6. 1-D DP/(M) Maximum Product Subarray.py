from typing import List

# My Brute Force Solution
# Time -- O(n^2)
# Space -- O(1)
# Expected it to be O(n^2) and too slow and it was. But at least a good
# start. Just could NOT figure out how to code up the recurrence relation.
# Feeling extremely defeated right now........ AGGHH
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProd = nums[0]
        for i in range(len(nums)):
            curProd = 1
            for factor in nums[i:]:
                curProd *= factor
                maxProd = max(maxProd, curProd)
        return maxProd


# NeetCode Solution
# Time -- O(n)
# Space -- O(1)
# I stumbled upon this concept of needing to know if we encountered
# negatives but just couldn't quite put it into code.
# Essentially by tracking both the current maximum and current minimum
# product subarrays, we can can incorporate the facts that double negatives
# cancel out through tracking it in the min prod subarray.
class NeetCodeSolution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1, 1

        for n in nums:

            tmp = curMax * n  # need to use old value of curMax, keep in tmp var

            # , n) also covers 0ed out (n * curMax, n * curMin)
            curMax = max(n * curMax, n * curMin, n)  # , n) covers [-1, 8], else -1 dominates in curMax, no 8
            curMin = min(tmp, n * curMin, n)  # covers [-1, -8], else -1 dominates in curMin, no -8
            res = max(res, curMax)
        return res

