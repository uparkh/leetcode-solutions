import heapq
from typing import List

# My Original Solution -- 10 minutes
# Pretty simple, just use max heap.
# Time: O(n * log(n))
# Space : O(n) -- making auxiliary negated array
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = [-s for s in stones]
        heapq.heapify(stones_heap)
        while len(stones_heap) > 1:
            s1 = -heapq.heappop(stones_heap)
            s2 = -heapq.heappop(stones_heap)
            if s1 == s2:
                continue
            heapq.heappush(stones_heap, -abs(s1 - s2))
        if stones_heap:
            return -stones_heap[0]
        return 0

# NeetCode Solution
# cleaner, less symbols with some logic skipping
# - max heap, so second stone weight <= first stone weight (logically)
#   second stone wiehgt > first stone weight (negation world)
class NeetCodeSolution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])

