import heapq
from typing import List
import math

# My Original Solution -- 9 minutes
# n == num points, k = num closest points to return
# Time: O(n + k*log(n)) -- heapify & distance calcs + extract closest points
# Space: O(n)
class Solution:
    def kClosest(self, points: List[List[int]],
        k: int)-> List[List[int]]:
        # start
        def distO(pt):
            x, y = pt
            return math.sqrt(x**2 + y**2)
        dists_pts = [(distO(pt), pt) for pt in points]
        heapq.heapify(dists_pts)
        rv = []
        for _ in range(k):
            rv.append(heapq.heappop(dists_pts)[1])
        return rv

# NeetCode Solution
# Pretty much the same thing but just phrased a bit differently
class NeetCodeSolution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append((dist, x, y))
        
        heapq.heapify(minHeap)
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            res.append((x, y))
        return res


