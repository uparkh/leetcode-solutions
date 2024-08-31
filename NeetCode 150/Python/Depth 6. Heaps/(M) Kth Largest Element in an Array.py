import heapq
from typing import List

# My Original Solution -- 5 minutes
# Dicussed in video as better than sorting, but worse avg than QuickSelect algo
# Time: avg - O(n + k * log(n))
# Space: O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_heap = [-n for n in nums]  # O(n)
        heapq.heapify(nums_heap)  # O(n)
        for _ in range(k-1):  # k iters of
            heapq.heappop(nums_heap)  # O(log n)
        return -nums_heap[0]

# NeetCode Solution
# Quick Select "a loose sort-as-you-go binary search traversal"
# Time complexity: O(n) in average, O(n^2) in worst case
class NeetCodeSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1
        while left < right:
            pivot = self.partition(nums, left, right)
            if pivot < k:
                left = pivot + 1  # kth largest in left half
            elif pivot > k:
                right = pivot - 1  # kth largest in left half
            else:  # pivot == k ~> found
                break
        return nums[k]

    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot, fill = nums[right], left
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]  # swap
                fill += 1
        nums[fill], nums[right] = nums[right], nums[fill]  # swap
        return fill  # now at pos where left half < pivot, right half > pivot

