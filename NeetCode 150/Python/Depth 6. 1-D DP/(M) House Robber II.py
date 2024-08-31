from typing import List

# No Original Solution
# I just could not think of how to incoroporate the circular housing situation
# I was on the right track when I thought to simply just consider only the
# subarray to the right of the first index, or to the left of the last index.
# But I couldn't quite put it together. I need to be thinking more discretely
# about the recurrence relation between the superproblem and the subproblem.


# NeetCode Solution
# Time -- O(n)
# Space -- O(1)
# Reuses the House Robber I solution. The circular nature only imposes the
# restriction of only being able to include the first or the last index.
# I am worrying too much about the exact details of each step plays out.
# Need to be able to take the "recursive leap of faith".
class NeetCodeSolution:
    def rob(self, nums: List[int]) -> int:
        # nums[0] for case when len(nums) == 1
        # choose right subarray of first idx or left subarr of last idx
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):  # HRI algo
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

