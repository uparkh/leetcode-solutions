from typing import List

# My Original (Incorrect) Solution
# I just could not figure out the trick. I had some sense that Kadane's
# algorithm should be applied, but I couldn't figure out in which way.
class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_end = 0  # farthest index currently known to be possible
        min_jumps = 0
        real_end = len(nums) - 1

        for i in range(len(nums)-1):
            num = nums[i]
            if i + num > cur_end:
                min_jumps += 1
                cur_end = i + num
            if cur_end >= real_end:
                break
        
        return min_jumps


# NeetCode Solution
# So my intuition was right about tracking the farthest possible jump.
# But I didn't use the sliding window technique, I tracked the farthest
# possible jump with a static window with L = 0, and R iterating thru
# the array.
# All I needed to do was update L to the lowest possible range of jumps.
class NeetCodeSolution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < (len(nums) - 1):
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res

