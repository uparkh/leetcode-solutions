from typing import List
import heapq

# My Original Incorrect Solution
# Went with 2 heaps because it felt better than DP in this scenario,
# but knew that this maybe didn't cover all edge cases, and I was right.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        if N == 1:
            return False
        left_heap, right_heap = nums[:N//2], nums[N//2:]

        heapq.heapify(left_heap)
        left_sum = sum(left_heap)

        heapq.heapify(right_heap)
        right_sum = sum(right_heap)
        pl, pr = -1, -2  # previous left / right (before popping)
        
        while left_sum != right_sum and pl != pr:
            if left_sum < right_sum:
                pr = heapq.heappop(right_heap)
                heapq.heappush(left_heap, pr)
                right_sum -= pr
                left_sum += pr
            elif left_sum > right_sum:
                pl = heapq.heappop(left_heap)
                heapq.heappush(right_heap, pl)
                left_sum -= pl
                right_sum += pl
        
        return left_sum == right_sum
        

# NeetCode-Inspired Solution
# Time: O(n * sum(nums))
# Space : O(n * sum(nums))
# Wow, I actually arrived at the set solution and didn't realize it was
# optimal! I guess I really just needed to trust myself more...
# I keep robbing myself of the victory feeling by not even attempting
# to implement any solution I find.
# New policy: Implement whichever solution I find, even if not optimal 
# initially. Optimize later.
class ModdedSolution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = {0, }
        for n in nums:
            for s in list(dp):
                if n + s == target:
                    return True
                dp.add(n + s)
        return False


# NeetCode Solution
class NeetCodeSolution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False

