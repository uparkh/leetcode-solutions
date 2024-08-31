from typing import List
# My Original Solution -- 30 minutes
# Time: O(n)
# Space: O(1)
# Drawing out the decision tree is SOOOOO helpful for these DP problems.
# I can straight up see the subproblems and how to construct the solution
# bottom-up.
# It seems that DP is very strongly related to greedy algorithms.
# I think drawing decision trees could have also helped for those type of
# problems.

# The key insight here was to realize that it did not make sense for the house
# robber to skip more than 2 houses at a time, because then there'd always
# be a house he misses and loses money.
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        nums[2] += nums[0]
        for i in range(3, len(nums)):
            nums[i] += max(nums[i-3], nums[i-2])
        return max(nums[-1], nums[-2])


# NeetCode Solution
# Note that the comment explaining the vars really just boils down to
# this recurrence relation:
# max_rob = max( arr[0] + arr[2:n], arr[1:n])
#        "rob this first house"      "or skip it for the remaining houses?"
class NeetCodeSolution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            # Right before this statement:
            # `rob1` == max value from subproblem rob(nums[:i-2])
            #           (does adding `n` create a new maximum?)
            # `rob2` == max value from subproblem rob(nums[:i-1])
            #           (or can we keep the max value from house before?)
            temp = max(n + rob1, rob2)


            rob1 = rob2
            rob2 = temp
        return rob2

