from typing import List
from collections import defaultdict
import heapq


# My Original Solution -- 25 minutes
# Time Complexity: O(E log V)
# Space Complexity: O(E)
# Immediately applying Prim's algorithm, pretty easy. I used way more space than necessary
# I could have just stored indices of where each vertex is found in the points array as a label.
# But the concept is the same with the NeetCode solution.
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # build adj list
        adj = defaultdict(list)  # (src_x, src_y) -> [(dist, tgt_x, tgt_y), ...]
        for i, src in enumerate(points[:-1]):
            for tgt in points[i+1:]:
                sx, sy = src
                tx, ty = tgt
                mhat = abs(tx - sx) + abs(ty - sy)
                adj[(sx, sy)].append((mhat, tx, ty))
                adj[(tx, ty)].append((mhat, sx, sy))

        starter = tuple(points[0])
        min_heap = []
        for target in adj[starter]:
            heapq.heappush(min_heap, target)

        visited = set()  # set of (x, y) pts
        visited.add(starter)
        res = 0  # cumulate
        # print(f'preloop state| visited:{visited}, mh: {min_heap}')
        while min_heap:
            dst, sx, sy = heapq.heappop(min_heap)
            src = (sx, sy)
            if src in visited:
                continue

            # print(f'res:{res}, dst:{dst}, src:{src}')
            res += dst
            visited.add(src)

            for t_dst, tx, ty in adj[src]:
                if (tx, ty) not in visited:
                    heapq.heappush(min_heap, (t_dst, tx, ty))
        return res


# NeetCode Solution
# Time Complexity: O(E log V)
# Space Complexity: O(E)
class NeetCodeSolution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)}  # i : list of [cost, node]
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Prim's
        res = 0
        visit = set()
        minH = [[0, 0]]  # [cost, point]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res
