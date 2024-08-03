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
        

