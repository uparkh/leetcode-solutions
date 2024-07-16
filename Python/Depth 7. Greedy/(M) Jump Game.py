from typing import List
# My Original Solution
# Time -- O(n)
# Space -- O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur_best = 0  # current best index possible
        for i, n in enumerate(nums):
            cur_best = max(cur_best, i + n)
            if i >= cur_best:  # beyond what is possible
                break
        
        return cur_best >= len(nums) - 1

# NeetCode Solution
# Way simpler to understand, he just inverted the problem and it becomes
# even easier. Iterate backwards and just see if its possible to jump backwards
# that far.
class NeetCodeSolution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

