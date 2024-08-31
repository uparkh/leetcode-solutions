from typing import List
from collections import defaultdict

# My Original Solution -- 21 minutes
# Time -- O(n * sum(nums))
# Space -- O(n * sum(nums))
# It's not the most optimal solution with true dynamic programming,
# but hey, I'd rather have a working memoized recursive solution to present
# at an interview and then work from there to bring it to a tabulation sol'n.
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # recursive memoized sol'n
        dp = {}
        def dfs(i, cur_sum, _nums, _target):
            if i == len(nums):
                return int(cur_sum == _target)
            if (i, cur_sum) in dp:
                return dp[(i, cur_sum)]
            dp[(i, cur_sum)] = dfs(i + 1, cur_sum + _nums[i], _nums, _target) + \
                               dfs(i + 1, cur_sum - _nums[i], _nums, _target)
            return dp[(i, cur_sum)]
        
        return dfs(0, 0, nums, target)


# NeetCode Solution
# well... to my surprise his solution is the exact same as mine...
# is there truly no DP way of doing this? seems not right...
class NeetCodeSolution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # (index, total) -> # of ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(
                i + 1, total - nums[i]
            )
            return dp[(i, total)]

        return backtrack(0, 0)

# 7Ibby Solution
# This dude was in the comment section for the NC Target Sum video and
# has a pretty elegant bottom-up solution. I get the intuition behind
# it. I thought this would be exponential time, but I have to remember
# that iterating through a triangularly growing list is still O(n^2)
# since 1 + 2 + 3 + ... + n-1 + n == n(n+1)/2

# Hi, big fan here. I solved this problem in a different way and it runs 
# quite efficiently. I just use a dictionary (initialized with 1 zero so that
# the first number in the nums array has something to compare against) and
# iterate over the nums array, and then I use another dictionary to store all
# the ways the numbers in the dp dictionary, "n", can change given the number
# from the nums array, "new_dp[n+/-num]", while keeping track of how many ways
# that new number can be made "dp[n]". Then all you have to do is return
# dp[target] since it holds how many ways that number can be achieved.
class IbbySolution:
    def findTargetSumWays(self, nums, target):
        dp = defaultdict(int)
        dp[0] = 1


        for num in nums:
            new_dp = defaultdict(int)
            for n in dp:
                new_dp[n+num] += dp[n]
                new_dp[n-num] += dp[n]

            dp = new_dp


        return dp[target]
