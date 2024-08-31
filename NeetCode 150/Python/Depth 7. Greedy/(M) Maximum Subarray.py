from typing import List

# Kadane's Algorithm
# Time -- O(n)
# Space -- O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0
        for n in nums:
            cur_sum = max(cur_sum, 0) + n
            max_sum = max(max_sum, cur_sum)
        return max_sum
